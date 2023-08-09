from django.apps import AppConfig


class SignalappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'signalapp'
    def ready(self):
        import signalapp.signals
