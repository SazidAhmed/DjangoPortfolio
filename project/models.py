from django.db import models
from django.urls import reverse


# Projject model
class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='resume/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={
            'project_id': self.id
        })


# experience model
class Experience(models.Model):
    title = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    details = models.CharField(max_length=350)
    time = models.CharField(max_length=50)

    def __str__(self):
        return self.title


# about model
class About(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=150)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    objective = models.CharField(max_length=350)
    image = models.ImageField(upload_to='resume/images/')

    def __str__(self):
        return self.name

# Interest model
class Interest(models.Model):
    title = models.CharField(max_length=150)

    def __str__(self):
        return self.title

# Skills model
class Skill(models.Model):
    workflow = models.CharField(max_length=150)
    icon = models.CharField(max_length=50)

    def __str__(self):
        return self.workflow


