# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('file_first', models.FileField(verbose_name='Model', upload_to='uploads/%Y_%m_%d/')),
                ('file_second', models.FileField(verbose_name='Experiment', upload_to='uploads/%Y_%m_%d/')),
                ('file_third', models.FileField(upload_to='uploads/%Y_%m_%d/', blank=True)),
                ('file_forth', models.FileField(upload_to='uploads/%Y_%m_%d/', blank=True)),
                ('experiment_name', models.CharField(max_length=100)),
                ('model_name', models.CharField(max_length=10)),
                ('cluster_number', models.CharField(max_length=2, verbose_name='Cluster Queue: *|Node_Number')),
                ('e_e', models.BooleanField(default=False, verbose_name='Run separate repetitions?')),
                ('email', models.EmailField(max_length=254)),
                ('hostname', models.CharField(max_length=100, default='cluster name.domain o Ip')),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
                ('result', models.TextField(blank=True)),
                ('state', models.BooleanField(default=False)),
                ('latest_run', models.IntegerField(default=1)),
            ],
        ),
    ]
