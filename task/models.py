from django.db import models

# Create your models here.


class Task(models.Model):
    STATUS = (
        ('Todo', 'Todo'),
        ('In progress', 'In progress'),
        ('Done', 'Done'),
        ('Cancelled', 'Cancelled')

    )
    user = models.ForeignKey('auth.User', models.CASCADE)
    title = models.CharField(max_length=221, db_index=True)
    created_date = models.DateTimeField(auto_now_add=True)
    content = models.TextField(blank=True, null=True)
    status = models.CharField(choices=STATUS, max_length=20, default='Todo')







