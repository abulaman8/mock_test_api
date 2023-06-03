from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status


from .models import TestPaper, TestQuestion
from .serializers import TestPaperSerializer, TestQuestionSerializer
from qp.models import QuestionPaper







@api_view(['POST'])
@permission_classes([IsAuthenticated])
def start_test(request):
    data = request.data
    user = request.user
    qp = QuestionPaper.objects.get(id=data['qp_id'])
    new_testpaper = TestPaper.objects.create(user=user, question_paper=qp)
    new_testpaper.save()
    qns = qp.questions.all()
    for qn in qns:
        tq = TestQuestion.objects.create(test_paper=new_testpaper, question=qn, type=qn.type)
        tq.save()
        if qn.type == 'MCQ' or qn.type == 'SCQ':
            for option in qn.choices.all():
                tq.choices.add(option)
                tq.save()
        elif qn.type == 'Numeric':
            tq.num_min = qn.num_min
            tq.num_max = qn.num_max
            tq.save()
        elif qn.type == 'Text':
            tq.text_answer = qn.text_answer
            tq.save()
        new_testpaper.test_questions.add(tq)
        new_testpaper.save()

    serialized  = TestPaperSerializer(new_testpaper, many=False)
    return Response(serialized.data)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_qn(request, id):
    qn = TestQuestion.objects.get(id=id)
    serialized = TestQuestionSerializer(qn, many=False)
    return Response(serialized.data)




@api_view(['POST'])
@permission_classes([IsAuthenticated])
def submit_test(request):
    data = request.data
    testpaper = TestPaper.objects.get(id=data['id'])
    if testpaper.user != request.user:
        return Response('You are not allowed to submit this test', status=status.HTTP_401_UNAUTHORIZED
                        )
    user_test_questions = data['test_questions']
    test_questions = testpaper.test_questions.all()
    return 0










