from django.contrib import admin
from .models import UserProfile, Exercises, TrainingPlan

admin.site.register(UserProfile)
admin.site.register(Exercises)
admin.site.register(TrainingPlan)

# Register your models here.
