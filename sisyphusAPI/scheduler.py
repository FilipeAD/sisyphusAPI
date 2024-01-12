import logging
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.executors.pool import ProcessPoolExecutor, ThreadPoolExecutor
from django_apscheduler.jobstores import register_events, register_job

from django.conf import settings

from pprint import pprint
import requests
import json
from datetime import datetime, timedelta

from rest_framework.response import Response
from rest_framework import status
from APIapp.serializers import ExerciseSerializer 
from APIapp.models import Exercises



def fetchexerciseAPI():
  
    muscle_groups = [ 'abdominals', 
                    'abductors', 
                    'adductors', 
                    'biceps', 
                    'calves', 
                    'chest',
                    'forearms',
                    'glutes',
                    'hamstrings',
                    'lats',
                    'lower_back',
                    'middle_back',
                    'neck',
                    'quadriceps',
                    'traps',
                    'triceps'
                    ]
    
    for muscle in muscle_groups:
        offset = 0
        
        while True:
            api_url = 'https://api.api-ninjas.com/v1/exercises?muscle={}&offset={}'.format(muscle, offset)
        
            response = requests.get(api_url, headers={'X-Api-Key': 'b9jGthrmp3JZxgUsYKy4KA==6pyIKaRO50A5sMVx'})

            if response.status_code == requests.codes.ok:
                
                api_data = response.json()

                print(f"Muscle Group: {muscle}, Data Length: {len(api_data)}, Offset: {offset}")

                for data_item in api_data:
                    
                    serializer = ExerciseSerializer(data=data_item)

                    if serializer.is_valid():

                        exercise_query = Exercises.objects.filter(name=data_item.get('name'))

                        if exercise_query.exists():
                            exercise = exercise_query.first()
                            exercise.muscle_group = muscle
                            exercise.difficulty = data_item.get('difficulty')
                            exercise.equipment = data_item.get('equipment')
                            exercise.instructions = data_item.get('instructions')
                            exercise.type = data_item.get('type')
                            exercise.save()
                        else:
                            exercise = Exercises.objects.create(
                                name=data_item.get('name'),
                                muscle=muscle,
                                difficulty=data_item.get('difficulty'),
                                equipment= data_item.get('equipment'),
                                instructions=data_item.get('instructions'),
                                type=data_item.get('type')

                            )

                    else:
                        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                    
                if len(api_data) < 10:
                    break
                
                offset += 10

            else:   
                return Response({"error": "Error occurred", "status_code": response.status_code, "response_text": response.text}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
    return Response({ "data": 'exercises for all muscle_groups successfully added' }, status=status.HTTP_200_CREATED);
        


scheduler = BackgroundScheduler(settings.SCHEDULER_CONFIG)



def start():
    if settings.DEBUG:
      	# Hook into the apscheduler logger
        logging.basicConfig()
        logging.getLogger('apscheduler').setLevel(logging.DEBUG)

    # Adding this job here instead of to crons.
    # This will do the following:
    # - Add a scheduled job to the job store on application initialization
    # - The job will execute a model class method at midnight each day
    # - replace_existing in combination with the unique ID prevents duplicate copies of the job
    scheduler.add_job(fetchexerciseAPI, 'interval', days=30)

    # Add the scheduled jobs to the Django admin interface
    register_events(scheduler)

    scheduler.start()

