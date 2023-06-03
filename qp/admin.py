from django.contrib import admin

from .models import (
        Question,
        Choice,
        QuestionPaper
        )




admin.site.register(QuestionPaper)

admin.site.register(Question)
admin.site.register(Choice)
