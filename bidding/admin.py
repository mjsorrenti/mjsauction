from django.contrib import admin

# Register your models here.

from .models import AuctionItem, Bid

admin.site.site_header = 'BPS Auction Admin Panel'

@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    list_display = ('id', 'item', 'amount', 'bidder', 'winning_bid')
    list_filter = ('item', 'bidder')
       
class BidInline(admin.TabularInline):
    model = Bid
    extra = 0
    can_delete = False

@admin.register(AuctionItem)
class AuctionItemAdmin(admin.ModelAdmin):
    list_display = ('item_number', 'name', 'high_bid', 'high_bidder','bidding_open')
    list_display_links = ('item_number', 'name')
    #list_editable = ('bidding_open',)
    inlines = [BidInline]
    
    
    actions = ['close_bidding', 'open_bidding']
    
    def close_bidding(self, request, queryset):
        queryset.update(bidding_open = False)
    close_bidding.short_description = "Close bidding on selected items"
    
    def open_bidding(self, request, queryset):
        queryset.update(bidding_open = True)
    open_bidding.short_description = "Open bidding on selected items"
