# Generated by Django 4.1.3 on 2024-06-29 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.CharField(max_length=69)),
                ('bio', models.CharField(max_length=69)),
            ],
        ),
    ]
