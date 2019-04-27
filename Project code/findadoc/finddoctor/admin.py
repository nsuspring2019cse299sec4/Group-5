from django.contrib import admin
from .models import UserProfile, Doctor, Disease, Symptom, Apponiment
# Register your models here.

admin.site.site_header = "FindAdoc Admin Portal"
admin.site.site_title = "Admin Portal"

admin.site.register(UserProfile)
admin.site.register(Doctor)
admin.site.register(Disease)
admin.site.register(Symptom)
admin.site.register(Apponiment)

