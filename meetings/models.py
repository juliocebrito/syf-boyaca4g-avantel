from django.db import models
from . import choices

# Create your models here.


class Meeting(models.Model):
    date = models.DateTimeField()
    type_meeting = models.CharField(max_length=255, choices=choices.TYPE_MEETINGS_CHOICES,
                                    default=choices.TYPE_MEETINGS_CHOICES[0][0])
    state = models.BooleanField(default=True, editable=False)
    sub_state = models.BooleanField(default=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'meeting'
        verbose_name_plural = 'meetings'

    def __str__(self):
        return str(self.date)


class Point(models.Model):
    meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    comments = models.TextField()
    point_state = models.CharField(max_length=255, choices=choices.STATE_POINT_CHOICES,
                                   default=choices.STATE_POINT_CHOICES[0][0])
    state = models.BooleanField(default=True, editable=False)
    sub_state = models.BooleanField(default=True, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created_at',)
        verbose_name = 'point'
        verbose_name_plural = 'points'

    def __str__(self):
        return self.name
