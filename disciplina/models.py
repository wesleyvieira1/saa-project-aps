from django.db import models

class Disciplina(models.Model):
    nome_disciplina = models.CharField(max_length=40)
