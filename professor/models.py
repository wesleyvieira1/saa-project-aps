from django.db import models

from usuario.models import Usuario

class Professor(models.Model):
    
    nome_professor = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    '''def __str__(self):
        return self.Usuario.departamento==2'''
