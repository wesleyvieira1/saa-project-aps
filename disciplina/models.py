from django.db import models

from professor.models import Professor

class Disciplina(models.Model):
    nome_disciplina = models.CharField(max_length=40)
    nome_professor = models.ManyToManyField(Professor)
    ano = models.DateField()
