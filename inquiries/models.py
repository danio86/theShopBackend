from django.db import models
from django.contrib.auth.models import User
from properties.models import Property


class Inquiry(models.Model):
    """
    Inquiry model, related to User and Property
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.content