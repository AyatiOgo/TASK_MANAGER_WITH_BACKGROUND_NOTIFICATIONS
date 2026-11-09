from django.db import models

# Create your models here.
class TaskModel(models.Model):

    title = models.CharField(max_length=200)
    description = models.CharField(max_length=3000, null=True, blank=True )
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

