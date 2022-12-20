# Generated by Django 4.1.3 on 2022-12-19 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Secret',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('classification', models.TextField()),
                ('secret', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserClearanceLevel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.TextField()),
                ('clearanceLevel', models.TextField()),
            ],
        ),
    ]