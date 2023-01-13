# Generated by Django 4.1.5 on 2023-01-12 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Todo', 'Todo'), ('In progress', 'In progress'), ('Done', 'Done'), ('Cancelled', 'Cancelled')], default='Todo', max_length=20),
        ),
    ]
