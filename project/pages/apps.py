from django.apps import AppConfig


class PagesConfig(AppConfig):
    name = 'pages'

    def ready(self):
        from scheduler import updater
        updater.start()