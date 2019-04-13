from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True, default='Test')
    address = models.CharField(max_length=50, null=True, blank=True, default='Test')
    phone = models.CharField(max_length=50, null=True, blank=True, default='Test')

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def __str__(self):
        return self.get_full_name()

"""
    def save(self, **kwargs):
        if(self.first_name):
            self.user.first_name = self.first_name
        super(UserProfile, self).save()
"""

class Doctor(UserProfile):

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])
		post_save.connect(create_profile, sender=User)

class Disease(models.Model):
    name = models.CharField(max_length=50)
    detail = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    treatment = models.CharField(max_length=100, default='Test')
    doctors = models.ManyToManyField(Doctor, blank=True, default='Test')

    def __str__(self):
        return self.name

class Symptom(models.Model):
    name = models.CharField(max_length=50)
    detail = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Apponiment():
    pass
