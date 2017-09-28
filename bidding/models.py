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
    #current_bid = models.IntegerField(default=0)
    #current_bidder = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    bidding_open = models.BooleanField(default=True)
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('item-detail', args=[str(self.item_number)])
    
    def high_bid(self):
        """
        Gets the current high bid value on this item
        """
        high_bid = 0
        
        for bid in self.bid_set.all():
            if bid.amount > high_bid:
                high_bid = bid.amount
                
        return high_bid
    
    def high_bidder(self):
        """
        Gets the current high bid value on this item
        """
        high_bid = 0
        high_bidder = ''
        
        for bid in self.bid_set.all():
            if bid.amount > high_bid:
                high_bid = bid.amount
                high_bidder = bid.bidder
                
        return high_bidder
    
    
    class Meta:
        ordering = ["item_number"]
        
        
class Bid(models.Model):
    """
    Model to capture all bids
    """
    
    item = models.ForeignKey(AuctionItem, on_delete=models.SET_NULL, null=True)
    bidder = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    amount = models.IntegerField()
    
    def __str__(self):
        return str(self.id)
    
    def winning_bid(self):
        if self.amount == self.item.high_bid():
            return True
        else:
            return False
    winning_bid.boolean = True