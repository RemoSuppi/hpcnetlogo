""" Models for Django """

from django.db import models


# Create your models here.

class Job(models.Model):
    """ MOdels """
    file_first = models.FileField(upload_to='uploads/%Y_%m_%d/', verbose_name='Model')
    file_second = models.FileField(upload_to='uploads/%Y_%m_%d/', verbose_name='Experiment')
    file_third = models.FileField(upload_to='uploads/%Y_%m_%d/', blank=True)
    file_forth = models.FileField(upload_to='uploads/%Y_%m_%d/', blank=True)
    experiment_name = models.CharField(max_length=100)
    model_name = models.CharField(max_length=10)
    cluster_number = models.CharField(max_length=2, verbose_name='Cluster Queue: *|Node_Number')
    e_e = models.BooleanField(default=False, verbose_name='Run separate repetitions?')
    email = models.EmailField()
    hostname = models.CharField(max_length=100, default='cluster name.domain o Ip')
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    add_time = models.DateTimeField(auto_now_add=True)
    result = models.TextField(blank=True)
    state = models.BooleanField(default=False)
    latest_run = models.IntegerField(default=1)
