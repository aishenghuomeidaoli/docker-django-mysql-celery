# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.


class MathTask(models.Model):
    TASK_TYPE = (
        ('add', 'x + y'),
        ('minus', 'x - y'),
        ('multiply', 'x * y'),
        ('divide', 'x / y'),
    )
    STATUS = (
        ('created', u'just created'),
        ('pending', u'pending for operated'),
        ('success', u'task success'),
        ('failed', u'task failed'),
    )
    task_type = models.CharField(max_length=16, choices=STATUS)
    x = models.FloatField()
    y = models.FloatField()
    result = models.FloatField(null=True)
    status = models.CharField(max_length=16, choices=STATUS, default='created')
    is_valid = models.BooleanField(default=True)
    create_time = models.DateTimeField(u'create time', auto_now_add=True)
    update_time = models.DateTimeField(u'update time', auto_now=True)

    class Meta:
        db_table = 'math_task'
        ordering = ['-create_time']