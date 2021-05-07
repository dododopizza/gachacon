from django.db import models

class Search(models.Model):
    req = models.TextField(blank=True, null=True)