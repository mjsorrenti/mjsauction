from django.shortcuts import render
from django.views import generic
from .models import AuctionItem
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
#from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required

from .forms import BidForm
from .forms import SelectItemForm

# Create your views here.

#class ItemsListView(generic.ListView):
#    model = AuctionItem

def item_list_view(request):
    model = AuctionItem.objects.all();
    
    if request.method == 'POST':
        form = SelectItemForm(request.POST)
        
        if form.is_valid():
            pk = form.cleaned_data['item_number']
            
            return HttpResponseRedirect(reverse('item-detail', args=[pk]))
    else:
        form = SelectItemForm()
        
    return render(request, 'bidding/auctionitem_list.html', {'form':form, 'auctionitem_list':model})


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
            
                return render(request, 'bidding/auctionitem_detail.html', {'auctionitem':item, 'acceptedbid':True})
        
            else:
                return render(request, 'bidding/auctionitem_detail.html', {'form':form, 'auctionitem':item, 'lowbid':True})
    
    else:
        form = BidForm()
    
    return render(request, 'bidding/auctionitem_detail.html', {'form':form, 'auctionitem':item})


@login_required
def user_page_view(request):
    total_bid=0  #Tally the total currently owed 
    bidding_closed = True  #Assume bidding is closed on all items
    user_high_bids = AuctionItem.objects.filter(current_bidder=request.user)
    
    for item in user_high_bids:
        total_bid += item.current_bid
        #If bidding is still open on any items, do not show payment info on the summary
        if item.bidding_open:
            bidding_closed = False
        
    return render(request, 'bidding/user_page.html', context={'high_bids':user_high_bids, 'total_bid':total_bid, 'bidding_closed':bidding_closed,})