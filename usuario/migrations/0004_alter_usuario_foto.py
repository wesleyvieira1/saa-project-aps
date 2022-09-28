# Generated by Django 4.1.1 on 2022-09-28 17:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0003_alter_usuario_foto_alter_usuario_historico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='foto',
            field=models.ImageField(blank=True, upload_to='documents/%d/%m/%Y', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg', 'jpeg'])]),
        ),
    ]
