from django.apps import AppConfig


class BaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'base'
    
    def ready(self):
        # Import your signals here to register them when the app is ready
        import base.signals  # Make sure 'base' matches your app name and signals.py file location