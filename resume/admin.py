# from django.contrib import admin
# from django.conf.urls import url
from django.contrib.admin import AdminSite
# from django.template.response import TemplateResponse
from django.urls import path
from django.shortcuts import render, redirect
from .resumeparser import ResumeParser

from .models import *



# class MyModelAdmin(admin.ModelAdmin):
class MyModelAdmin(AdminSite):
    header = 'NEW HEAD HERE'
    def get_urls(self):
        urls = super().get_urls()
        additional_urls = [
            path('upload/', self.admin_view(self.upload)),
            path('process/', self.admin_view(self.process)),
        ]
        return additional_urls + urls

    def upload(self, req):
        return render(req, 'resume/upload.html')

    def process(self, req):
        if not req.FILES:
            return redirect('/admin/upload')
        else:
            resume_file = req.FILES['resume']
            parsed_resume = ResumeParser(resume_file).extract_text().normalize().split_sections()
            try:
                resume = parsed_resume.clean_sections()
                header = resume.sections['HEADER']
                experience = resume.sections['EXPERIENCE']
                skills = resume.sections['SKILLS & ABILITIES']
                resume = Resume.objects.create(name=header['name'], title=header['title'], email=header['email'], phone=header['phone'], location=header['location'], blurb=header['blurb'])
                resume.save()
                ActiveResume.objects.all().delete()
                ActiveResume.objects.create(resume=resume)
                for social in header['socials']:
                    try:
                        if 'linkedin' in social:
                            s = SocialMedia.objects.create(name='LinkedIn', link=social)
                            s.save()
                        if 'github' in social:
                            s = SocialMedia.objects.create(name='GitHub', link=social)
                            s.save()
                        s.resume.add(resume)
                    except Exception as e:
                        print(f'SOCIALS ERROR: {e}')
                for job in experience:
                    print(f'### ADDING JOB: {job}')
                    job_obj = Job.objects.create(start=job['start'], end=job['end'], title=job['title'], employer=job['company'])
                    job_obj.save()
                    for bullet in job['bullets']:
                        print('### ADDING BULLET')
                        bullet_obj = Bullet.objects.create(text=bullet, job=job_obj)
                        bullet_obj.save()
                    job_obj.resume.add(resume)
            except Exception as e:
                print(f'ERROR: {e}')
                return redirect('/admin', e)
        return redirect('/admin')

    
my_model_admin = MyModelAdmin(name='myadmin')

# Register your models here.
my_model_admin.register(Resume)
my_model_admin.register(Job)
my_model_admin.register(Bullet)
my_model_admin.register(Skill)
my_model_admin.register(SocialMedia)
my_model_admin.register(ActiveResume)