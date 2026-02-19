from django.contrib import admin
# from django.conf.urls import url
from django.contrib.admin import AdminSite
from django.template.response import TemplateResponse
from django.urls import path
from django.shortcuts import render
import pdfplumber, re

from .models import *



# class MyModelAdmin(admin.ModelAdmin):
class MyModelAdmin(AdminSite):
    header = 'NEW HEAD HERE'
    def get_urls(self):
        print('############ GETTING URLS ##################')
        urls = super().get_urls()
        additional_urls = [
            path('upload/', self.admin_view(self.upload_view)),
            path('process/', self.admin_view(self.process_view)),
        ]
        print(f'custom urls: {additional_urls}')
        return additional_urls + urls

    def upload_view(self, req):
        return TemplateResponse(req, 'resume/upload.html')

    def process_view(self, req):
        return render(req, 'resume/process.html')

    
my_model_admin = MyModelAdmin(name='myadmin')

# Register your models here.
my_model_admin.register(Resume)
my_model_admin.register(Job)
my_model_admin.register(Bullet)
my_model_admin.register(Skill)
my_model_admin.register(SocialMedia)
my_model_admin.register(ActiveResume)


class ResumeParser:
    def __init__(self, pdf):
        self.pdf = pdf
        self.headers = [
            'HEADER',
            'EXPERIENCE',
            'SKILLS & ABILITIES'
        ]
        self.text = extract_text()
        self.text = normalize()

    def extract_text(self):
        text = ''
        with pdfplumber.open(self.pdf) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + '\n'
        return text

    def normalize(self):
        text = self.text
        text = text.replace('\r', '\n')
        text = re.sub(r'\n{2,}', '\n', text)
        text = re.sub(r'[ \t]+', ' ', text)
        return text.strip()

    def split_sections(self):
        text = self.text
        lines = text.split('\n')
        sections = {}
        current_section = 'HEADER'
        sections[current_section] = []

        for line in lines:
            cleaned = line.strip().lower()

            if cleaned in self.headers:
                current_section = cleaned
                sections[current_section] = []
            else:
                sections[current_section].append(line)

        for key in sections:
            sections[key] = '\n'.join(sections[key]).strip()

        return sections