from django.shortcuts import render
from django.db.models import Prefetch
from django.views.decorators.http import require_http_methods
from .models import *

# Create your views here.
def index(req):
    try:
        content = {'resume': Resume.objects.prefetch_related('jobs__bullets', 'skills', 'socials').get(uuid=ActiveResume.objects.all().first().resume.uuid)}
        content['skills'] = {}
        for skill in content['resume'].skills.all():
            if skill.category in content['skills'].keys():
                content['skills'][skill.category].append(skill)
            else:
                content['skills'][skill.category] = [skill]
    except Exception as e:
        print(f'### EXCEPTION: {e}')
        content = None
    return render(req, 'resume/index.html', content)