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
    bidding_open = models.BooleanField(default=False)
    
    #These next two fields should be used only if bids are being input manually via the Admin site; they should be removed if bids are being managed via the app front end and the Bid model below
    current_bid = models.IntegerField(default=0)
    current_bidder = models.ForeignKey('Bidder', on_delete=models.SET_NULL, null=True, blank=True)
        
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('item-detail', args=[str(self.item_number)])
    
    def bidder_name(self):
        if self.current_bidder:
            return self.current_bidder.first_name + ' ' + self.current_bidder.last_name
        else:
            return ''
    
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
        
        
#The Bidder model is used if bids will be entered to the current_bid field of the AuctionItem model via the admin site; it should not be necessary if all bids are entered by users through the app front end
class Bidder(models.Model):
    """
    Model for bidders independent of site users
    """
    
    number = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(null=True, blank=True)
    
    def __str__(self):
        return str(self.number)

    def bid_items(self):
        bid_list = []
        for item in self.auctionitem_set.all():
            bid_list.append(item.name)
        return ', '.join(bid_list)
            

        
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