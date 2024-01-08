# Generated by Django 4.2.7 on 2023-12-29 17:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('APIapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='activity',
            field=models.CharField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(6)]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='age',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(18, message='Must be 18 or older.'), django.core.validators.MaxValueValidator(100, message='Must be 100 or younger.')]),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='calorieIntake',
            field=models.IntegerField(help_text='Daily calorie Intake', null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='height',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='weight',
            field=models.FloatField(null=True),
        ),
    ]
