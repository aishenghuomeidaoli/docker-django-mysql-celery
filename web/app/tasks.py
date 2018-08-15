# Create your tasks here
from __future__ import absolute_import, unicode_literals

import time
from celery import shared_task

from .models import MathTask


@shared_task
def math(task_id):
    try:
        row = MathTask.objects.get(id=task_id, is_valid=True, status='created')
        row.status = 'pending'
        row.save()

        time.sleep(10)
        task_type = row.task_type
        try:
            row.status = 'success'
            if task_type == 'add':
                row.result=row.x + row.y
            elif task_type == 'minus':
                row.result=row.x - row.y
            elif task_type == 'multiply':
                row.result=row.x * row.y
            elif task_type == 'divide':
                row.result=row.x / row.y
            else:
                row.status='failed'
        except Exception:
            row.status='failed'
        row.save()

    except MathTask.DoesNotExist:
        return
