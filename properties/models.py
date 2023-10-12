from django.db import models
from django.contrib.auth.models import User


# class Image(models.Model):
#     property = models.ForeignKey(Property, on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='property_images/')

class Property(models.Model):
    """
    Property model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """

    image_filter_choices = [
        ('_1977', '1977'),
        ('brannan', 'Brannan'),
        ('earlybird', 'Earlybird'),
        ('hudson', 'Hudson'),
        ('inkwell', 'Inkwell'),
        ('lofi', 'Lo-Fi'),
        ('kelvin', 'Kelvin'),
        ('normal', 'Normal'),
        ('nashville', 'Nashville'),
        ('rise', 'Rise'),
        ('toaster', 'Toaster'),
        ('valencia', 'Valencia'),
        ('walden', 'Walden'),
        ('xpro2', 'X-pro II')
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
    status = models.CharField(max_length=10, choices=[('Available', 'Available'), ('Sold', 'Sold')])
    sold_date = models.DateField(null=True, blank=True)
    property_type = models.CharField(
            max_length=20,
            choices=[
                ('Loft', 'Loft'),
                ('Flat', 'Flat'),
                ('Villa', 'Villa'),
                # Add more choices as needed
            ],
        )
    num_interests = models.PositiveIntegerField(default=0)
    image = models.ImageField(
        upload_to='images/', default='../default_post_rgq6aq', blank=True
    )
    image_filter = models.CharField(
    max_length=32, choices=image_filter_choices, default='normal'
    )
    # images = models.ManyToManyField(Image)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'