from django.contrib.auth.models import BaseUserManager

class UsuarioManager(BaseUserManager):
    def create_user(self, email, nome, password):
        if not email:
            raise ValueError("Insira um email válido")
        usuario = self.model(
            nome = nome,
            email = self.normalize_email(email)
        )
        usuario.set_password(password)
        usuario.save()
        return usuario