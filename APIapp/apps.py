from django.apps import AppConfig
from django.conf import settings


class ApiappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'APIapp'

    def ready(self):
        from sisyphusAPI import scheduler
        if settings.SCHEDULER_AUTOSTART:
        	scheduler.start()