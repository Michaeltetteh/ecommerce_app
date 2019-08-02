from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'main'

    # initialize signals
    def ready(self):
        from . import signals
