from django.db import models

class Annotated(models.Model):
    name = models.CharField(max_length=200, null=True)
    text = models.TextField(blank=True)
    annotations = models.JSONField(blank=True)
    
    
    def __str__(self):
        return str(self.name)