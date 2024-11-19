from django.apps import AppConfig

class GradeSystemConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'grade_system'

    def ready(self):
        import grade_system.signals  

