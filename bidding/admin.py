from django.contrib import admin

# Register your models here.

from .models import AuctionItem

class AuctionItemAdmin(admin.ModelAdmin):
    list_display = ('item_number', 'name', 'current_bid', 'current_bidder','bidding_open')
    list_filter = ('current_bid', 'current_bidder')

admin.site.register(AuctionItem, AuctionItemAdmin)

