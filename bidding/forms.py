from django import forms
from django.core.exceptions import ValidationError
from .models import AuctionItem

class BidForm(forms.Form):
    bid = forms.IntegerField(label="Enter your bid", required=True)
    

class SelectItemForm(forms.Form):
    item_number = forms.IntegerField(label="Item number", required=True)
    
    def clean_item_number(self):
        data = self.cleaned_data['item_number']
        
        # Ensure the item number exists
        if data < 1 or data > len(AuctionItem.objects.all()):
            raise ValidationError('That item number doesn\'t exist')
                
        return data
    