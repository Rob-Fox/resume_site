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
            path('upload/', self.admin_view(self.upload), name='upload'),
            path('process/', self.admin_view(self.process)),
            path('clear/', self.admin_view(self.clear), name='clear')
        ]
        return additional_urls + urls

    def clear(self, req):
        ActiveResume.objects.all().delete()
        SocialMedia.objects.all().delete()
        Resume.objects.all().delete()
        Job.objects.all().delete()
        Bullet.objects.all().delete()
        Skill.objects.all().delete()
        return redirect('/admin')

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
                social_group = []
                job_group = []
                bullet_group = []
                skill_group = []
                for social in header['socials']:
                    try:
                        if 'linkedin' in social:
                            social_obj = SocialMedia(name='LinkedIn', link=social)
                            social_group.append(social_obj)
                        if 'github' in social:
                            social_obj = SocialMedia(name='GitHub', link=social)
                            social_group.append(social_obj)
                    except Exception as e:
                        print(f'SOCIALS ERROR: {e}')
                for job in experience:
                    job_obj = Job(start=job['start'], end=job['end'], title=job['title'], employer=job['company'])
                    job_group.append(job_obj)
                    for bullet in job['bullets']:
                        bullet_obj = Bullet(text=bullet, job=job_obj)
                        bullet_group.append(bullet_obj)
                for skill in skills:
                    skill_object = Skill(category=skill['category'], skill_name=skill['skill'])
                    skill_group.append(skill_object)
                SocialMedia.objects.bulk_create(social_group)
                for social in social_group:
                    social_obj.resume.add(resume)
                Job.objects.bulk_create(job_group)
                for job in job_group:
                    job.resume.add(resume)
                Bullet.objects.bulk_create(bullet_group)
                Skill.objects.bulk_create(skill_group)
                for skill in skill_group:
                    skill.resume.add(resume)
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