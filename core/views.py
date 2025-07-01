import os
import cv2
import numpy as np
import easyocr

from django.shortcuts import render, redirect
from django.conf import settings
from .forms import QuestionForm, AnswerUploadForm
from .models import StudentAnswer, Question

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity



def home(request):
    return redirect('upload_answer')

def upload_question(request):
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('upload_question')
    return render(request, 'upload_question.html', {'form': form})

def upload_answer(request):
    form = AnswerUploadForm(request.POST, request.FILES or None)
    if form.is_valid():
        answer = form.save()

        image_path = os.path.join(settings.MEDIA_ROOT, str(answer.answer_image))

# Preprocess the image using OpenCV
        img = cv2.imread(image_path)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# OCR using EasyOCR on processed image
        reader = easyocr.Reader(['en'])
        result = reader.readtext(thresh, detail=0)
 
        extracted = ' '.join(result)
        answer.extracted_text = extracted

        ideal = answer.question.ideal_answer

        if ideal.strip() and extracted.strip():
            tfidf = TfidfVectorizer().fit_transform([ideal, extracted])
            similarity = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
            score = round(similarity * 100, 2) 
        else:
            score = 0.0

        answer.score = score
        answer.save()

        return redirect('upload_answer')
    return render(request, 'upload_answer.html', {'form': form})
def view_answers(request):
    answers = StudentAnswer.objects.all()
    return render(request, 'view_answers.html', {'answers': answers})

def dashboard(request):
    questions = Question.objects.all()
    answers = StudentAnswer.objects.all()
    return render(request, 'dashboard.html', {'questions': questions, 'answers': answers})
