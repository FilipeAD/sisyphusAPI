from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    email = models.EmailField(max_length=50, unique=True)
    username = models.CharField(max_length= 50)
    
    class Genders(models.TextChoices):
        Male = 'Male'
        Female = 'Female'

    sex = models.CharField(choices=Genders.choices, default=Genders.Male)
    activity = models.CharField(  validators=[
            MinValueValidator(1),
            MaxValueValidator(6)
        ])
    age = models.IntegerField(
        validators=[
            MinValueValidator(18, message="Must be 18 or older."),
            MaxValueValidator(100, message="Must be 100 or younger.")
        ]
    )
    height = models.FloatField()
    weight = models.FloatField()
    calorieIntake = models.IntegerField(help_text="Daily calorie Intake")
    
     
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.email



class Exercises(models.Model):
    exercise_id = models.AutoField(primary_key=True)
    name = models.CharField(help_text='exercise name')
    type = models.CharField(help_text='exercise type')
    muscle = models.CharField(help_text='muscle group')
    equipment = models.CharField(help_text='needed equipment')
    difficulty = models.CharField(help_text='exercise difficulty')
    instructions = models.TextField(help_text='exercise instructions')

    class Meta:
        ordering = ['exercise_id']


    def __str__(self):
        return self.name



class TrainingPlan(models.Model):
    plan_id = models.AutoField(primary_key=True)
    exercises = models.ManyToManyField(Exercises)
    userfk = models.ForeignKey(UserProfile, on_delete=models.CASCADE)


    class Meta:
        ordering = ['plan_id']

  
    def __str__(self):
        return self.plan_id



