from django import forms
#from django.core.exceptions import ValidationError

class BidForm(forms.Form):
    bid = forms.IntegerField(label="Enter your bid", required=True)
    
