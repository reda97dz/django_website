from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Run(models.Model):
    ACTIVITY_CHOICES = (
        ('run', 'Run'),
        ('hike', 'Hike')
    )
    activity = models.CharField(max_length=20, choices=ACTIVITY_CHOICES, default='run')
    name = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    distance = models.FloatField()
    duration = models.FloatField()
    pace = models.FloatField()
    date = models.DateField()
    
    class Meta:
        ordering = ('-date',)
    
    def __str__(self):
        return '{}/{}/{}{}{}'.format(self.name, self.distance, self.created.day, self.created.month,  self.created.year)
    
    def get_absolute_url(self):
        return reverse('workout:run_details', args=[self.pk])
    