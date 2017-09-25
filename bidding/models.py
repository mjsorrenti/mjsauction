from django.db import models
from django.urls import reverse  # Add ability to reverse lookup URLs for model instances
from django.contrib.auth.models import User  # Allow linking of auction items to site users

# Create your models here.

class AuctionItem(models.Model):
    """
    Model for the individual items up for bidding
    """
    
    item_number = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=1000, null=True, blank=True)
    #image = models.ImageField(null=True, blank=True)
    current_bid = models.IntegerField(default=0)
    current_bidder = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    bidding_open = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('item-detail', args=[str(self.item_number)])
    
    class Meta:
        ordering = ["item_number"]