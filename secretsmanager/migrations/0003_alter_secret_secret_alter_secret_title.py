# Generated by Django 4.1.3 on 2023-02-08 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secretsmanager', '0002_alter_secret_secret_alter_secret_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='secret',
            name='secret',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='secret',
            name='title',
            field=models.TextField(),
        ),
    ]
