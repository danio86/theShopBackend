from django.db import models
from django.contrib.auth.models import User
from properties.models import Property


class Sold(models.Model):
    """
    Sold model, related to 'owner' and 'property'.
    'owner' is a User instance and 'property' is a Property instance.
    'unique_together' makes sure a user can't put the sales status on sold the same property twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(
        Property, related_name='sold', on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'property']

    def __str__(self):
        return f'{self.owner} {self.property}'