from django.contrib import admin

from .models import Question, Choice, QuestionPaper, ImageContent


admin.site.register(QuestionPaper)

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(ImageContent)
