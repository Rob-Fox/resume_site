from django.db import models
from django.core.validators import MinLengthValidator
import uuid

# Create your models here.
class Resume(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    title = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, blank=False, null=False)
    phone = models.CharField(max_length = 24, blank=False, null=False)
    location = models.CharField(max_length=254, blank=False, null=False)
    blurb = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class Job(models.Model):
    start = models.DateField()
    end = models.DateField(blank=True, null=True)
    title = models.CharField(max_length=100, blank=False, null=False)
    employer = models.CharField(max_length=100)
    resume = models.ManyToManyField(Resume, related_name='jobs')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Bullet(models.Model):
    text = models.TextField()
    job = models.ForeignKey(Job, related_name='bullets', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Skill(models.Model):
    category = models.CharField(max_length=25)
    skill_name = models.CharField(max_length=25)
    resume = models.ManyToManyField(Resume, related_name='skills')

class SocialMedia(models.Model):
    name = models.CharField(max_length=32)
    link = models.URLField(blank=False, null=False, unique=True)
    resume = models.ManyToManyField(Resume, related_name='socials')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class ActiveResume(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE)