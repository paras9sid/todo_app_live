from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
PRIORITY_CHOICES = (
    ("High","High"),
    ("Medium","Medium"),
    ('Low','Low'),
)


class TaskToDo(models.Model):
    featured_image = models.ImageField(upload_to='uploads/%Y/%m/%d')
    name = models.CharField(max_length=50)
    task = models.CharField(max_length=50)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Low')
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = 'Task Todo'
    
    def __str__(self):
        return self.name + ' ' + self.task