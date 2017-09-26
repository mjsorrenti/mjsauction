from django.shortcuts import render
from django.views import generic
from .models import AuctionItem
from django.shortcuts import get_object_or_404
#from django.http import HttpResponseRedirect
#from django.core.urlresolvers import reverse
#from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required

from .forms import BidForm

# Create your views here.

class ItemsListView(generic.ListView):
    model = AuctionItem
    
# class ItemDetailView(generic.DetailView):
#    model = AuctionItem

def item_detail_view(request, pk):
    item = get_object_or_404(AuctionItem, pk = pk)
    
    # If this is a POST request then process the Form data
    if request.method == 'POST':
        form = BidForm(request.POST)
        
        if form.is_valid():
            if form.cleaned_data['bid'] > item.current_bid:
                item.current_bid = form.cleaned_data['bid']
                item.current_bidder = request.user
                item.save()
            
                return render(request, 'bidding/bid_accepted.html')
        
            else:
                return render(request, 'bidding/auctionitem_detail.html', {'form':form, 'auctionitem':item, 'lowbid':True})
    
    else:
        form = BidForm()
    
    return render(request, 'bidding/auctionitem_detail.html', {'form':form, 'auctionitem':item})


@login_required
def user_page_view(request):
    user_high_bids = AuctionItem.objects.filter(current_bidder=request.user)
    
    return render(request, 'bidding/user_page.html', {'high_bids':user_high_bids})