# Generated by Django 4.1.1 on 2022-10-20 01:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0006_usuario_senha'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='senha',
        ),
    ]