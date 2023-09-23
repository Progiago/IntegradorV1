from django.apps import AppConfig


class UsuarioConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'usuario'
    
    def ready(self, *args, **kwargs):
        import usuario.signals    #noqa
        super_ready = super().ready(*args, **kwargs)
        return super_ready

