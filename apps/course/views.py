from django.shortcuts import render
from django.views.decorators.csrf import ensure_csrf_cookie

from .models import Section, Question, Reading


@ensure_csrf_cookie
def home(request):
    data = {
        'sections': Section.objects.all(),
        'question': Question.objects.all(),
    }
    return render(request, 'course/index.html', data)
