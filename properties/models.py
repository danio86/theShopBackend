from django.db import models
from django.contrib.auth.models import User


class Property(models.Model):
    """
    Property model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """

    image_filter_choices = [
        ('_1977', '1977'),
        ('normal', 'Normal'),
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=7, decimal_places=2)
    location = models.CharField(max_length=100)
    num_rooms = models.PositiveSmallIntegerField()
    # status = models.CharField(max_length=10, choices=[('Available', 'Available'), ('Sold', 'Sold')])
    sold_date = models.DateField(null=True, blank=True)
    property_type = models.CharField(
            max_length=20,
            choices=[
                ('Loft', 'Loft'),
                ('Flat', 'Flat'),
                ('Apartment', 'Apartment'),
                ('Farmhouse', 'Farmhouse'),
                ('Condos', 'Condos'),
                ('Townhouse', 'Townhouse'),
                ('Chalet', 'Chalet'),
                ('Studio', 'Studio'),
            ],
        )
    # num_interests = models.PositiveIntegerField(default=0)
    image = models.ImageField(
        upload_to='images/', default='../default_property_rgq6aq', blank=True
    )
    image_filter = models.CharField(
    max_length=32, choices=image_filter_choices, default='normal'
    )

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'