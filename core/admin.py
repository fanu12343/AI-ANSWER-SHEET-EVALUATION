from django.contrib import admin
from .models import Teacher, Question, StudentAnswer, Evaluation

admin.site.register(Teacher)
admin.site.register(Question)
admin.site.register(StudentAnswer)
admin.site.register(Evaluation)
