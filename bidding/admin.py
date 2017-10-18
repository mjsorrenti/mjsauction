from django.contrib import admin, messages
from django.conf import settings

# Import email capabilities from sendgrid
import sendgrid
from sendgrid.helpers.mail import *

# Register your models here.

from .models import AuctionItem, Bid, Bidder

admin.site.site_header = 'BPS Auction Admin Panel'

#The Bid model is used to track bids placed through the app front end; it might not be used if bids are entered directly into the current_bid field of the AuctionItem model via the Admin pages
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
    #list_display = ('item_number', 'name', 'high_bid', 'high_bidder','bidding_open')
    list_display = ('item_number', 'name', 'current_bidder', 'current_bid', 'bidding_open')
    list_display_links = ('item_number', 'name')
    list_editable = ('current_bidder', 'current_bid')
    #inlines = [BidInline]
    list_filter = ('current_bidder',)
    
    actions = ['close_bidding', 'open_bidding', 'email_winners']
    
    def close_bidding(self, request, queryset):
        queryset.update(bidding_open = False)
    close_bidding.short_description = "Close bidding on selected items"
    
    def open_bidding(self, request, queryset):
        queryset.update(bidding_open = True)
    open_bidding.short_description = "Open bidding on selected items"

    #email highest bidders on selected items with a link to payment
    def email_winners(self, request, queryset): 
        #This function assumes that bids were entered into the current_bid & current_bidder 
        #fields of the AuctionItem model. If bids are being tracked via the Bid model,
        #this function needs to be rewritten. See the user_page_view function in the vews
        #module for a possible pattern
        
        successful_emails = 0
        
        #raise a notification for any selected bidders who do not have email addresses
        for selected_item in queryset:
            if not selected_item.current_bidder.user.email:
                self.message_user(request, '%s does not have an email address' % selected_item.current_bidder.user, messages.WARNING)
                
        for bidder in Bidder.objects.all():
            #for each bidder in the system, construct the list of selected items on which they 
            #have the current bid
            winning_items = queryset.filter(current_bidder=bidder)
            
            #make sure the bidder has both winning bids and an email address
            if winning_items and bidder.user.email:
                total_bid = 0
                #Open the HTML table tag & set heading
                item_table_html = "<table cellpadding=\"5px\" border=\"1px\"><tr><th>Item</th><th>Bid</th></tr>"
                for item in winning_items:
                    total_bid += item.current_bid
                    #Create new HTML table rows for each item
                    item_table_html += "<tr><td>" + item.name + " </td><td>$" + str(item.current_bid) + "</td></tr>"
                #Add summary row and close the HTML table    
                item_table_html += "<tr style='font-weight: bold;'><td style='text-align: right'>Total: </td><td>$" + str(total_bid) + "</td></tr></table>"
                
                #self.message_user(request, item_table_html)
        
                #send email message via sendgrid
                sg = sendgrid.SendGridAPIClient(apikey=settings.SENDGRID_API_KEY)
                from_email = Email("test@example.com")
                subject = "Will be overridden by template"
                to_email = Email(bidder.user.email)
                content = Content("text/html", item_table_html)
                mail = Mail(from_email, subject, to_email, content)
                mail.personalizations[0].add_substitution(Substitution("-firstname-", bidder.user.first_name))
                mail.template_id = "fd12b8e2-24bf-470c-b780-4d4ccd4e94b9"
                response = sg.client.mail.send.post(request_body=mail.get())
                if response.status_code==202:
                    successful_emails += 1
                
                                      
        self.message_user(request, '%s emails sent successfully' % successful_emails)
        
        
@admin.register(Bidder)
class BidderAdmin(admin.ModelAdmin):
    fields = ('number','user')
    readonly_fields = ('number',)
    list_display = ('number','user','full_name')
    
