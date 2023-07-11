from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


from .models import TestPaper, TestQuestion
from .serializers import (
        TestPaperSerializer,
        TestQuestionSerializer,
        PartialTestPaperSerializer
        )
from qp.models import QuestionPaper


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def start_test(request):
    data = request.data
    user = request.user
    qp = QuestionPaper.objects.get(id=data["qp_id"])
    new_testpaper = TestPaper.objects.create(user=user, question_paper=qp)
    new_testpaper.save()
    qns = qp.questions.all()
    for qn in qns:
        tq = TestQuestion.objects.create(
            test_paper=new_testpaper,
            question=qn,
            type=qn.type,
            marks=qn.marks,
        )
        tq.save()
        if qn.type == "MCQ" or qn.type == "SCQ":
            for option in qn.choices.all():
                tq.choices.add(option)
                tq.save()
        elif qn.type == "Numeric":
            tq.num_min = qn.num_min
            tq.num_max = qn.num_max
            tq.save()
        elif qn.type == "Text":
            tq.text_answer = qn.text_answer
            tq.save()
        new_testpaper.test_questions.add(tq)
        new_testpaper.save()

    serialized = PartialTestPaperSerializer(new_testpaper, many=False)
    return Response(serialized.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_qn(request, id):
    qn = TestQuestion.objects.get(id=id)
    serialized = TestQuestionSerializer(qn, many=False)
    return Response(serialized.data)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def submit_test(request):
    data = request.data
    testpaper = TestPaper.objects.get(id=data["id"])
    if not testpaper:
        return Response(
                "Test Paper not found",
                status=status.HTTP_404_NOT_FOUND
                )
    if testpaper.user != request.user:
        return Response(
            "You are not allowed to submit this test",
            status=status.HTTP_401_UNAUTHORIZED,
        )
    if testpaper.submitted:
        return Response(
            "You have already submitted this test",
            status=status.HTTP_401_UNAUTHORIZED,
        )
    user_test_questions = data["test_questions"]
    for qn in user_test_questions.keys():
        test_qn = TestQuestion.objects.get(id=qn)
        if test_qn.type == "MCQ" or test_qn.type == "SCQ":
            for choice in user_test_questions[qn]:
                test_qn.user_choices.add(choice)
                test_qn.save()
        elif test_qn.type == "Numeric":
            test_qn.user_num_answer = user_test_questions[qn]
            test_qn.save()
        elif test_qn.type == "Text":
            test_qn.user_text_answer = user_test_questions[qn]
            test_qn.save()
    testpaper.submitted = True
    testpaper.save()
    testpaper.evaluate()
    serialized = TestPaperSerializer(testpaper, many=False)
    return Response(serialized.data, status=status.HTTP_200_OK)
