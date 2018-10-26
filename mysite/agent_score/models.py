# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class agent_score(models.Model):
    agent_id = models.CharField(max_length=20)
    observe_score = models.CharField(max_length=100)
    evaluate_score = models.CharField(max_length=100)
    predict_score = models.CharField(max_length=100)

    class Meta:
        db_table = 'agent_score'