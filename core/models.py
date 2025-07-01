from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name

class Question(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    text = models.TextField()
    ideal_answer = models.TextField(default="")

class StudentAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=100)
    answer_image = models.ImageField(upload_to='answer_sheets/')
    extracted_text = models.TextField(blank=True,null=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    score = models.FloatField(default=0.0)

    def __str__(self):
        return f"{self.student_name} - {self.question.text[:30]}"

class Evaluation(models.Model):
    student_answer = models.OneToOneField(StudentAnswer, on_delete=models.CASCADE)
    extracted_text = models.TextField(blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    feedback = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.student_answer.student_name} - Score: {self.score}"
