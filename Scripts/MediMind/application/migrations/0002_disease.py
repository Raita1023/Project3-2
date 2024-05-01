# Generated by Django 5.0.3 on 2024-05-01 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('avoid_foods_and_drinks', models.TextField()),
                ('examination_preparation', models.TextField()),
            ],
        ),
    ]