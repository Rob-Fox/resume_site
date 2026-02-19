from django.shortcuts import render
from django.db.models import Prefetch
# from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from .models import *

# Create your views here.
def index(req):
    try:
        content = Resume.objects.prefetch_related('jobs__bullets', 'skills', 'socials').get(uuid=ActiveResume.objects.all.first().resume.uuid)
    except Exception as e:
        content = None
    
    return render(req, 'resume/index.html', content)