from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UpdateEvent(models.Model):
	transaction_id = models.CharField(max_length=100)
	no_of_hours = models.IntegerField(default=0)
	job_number_choice = models.IntegerField(default=0)
