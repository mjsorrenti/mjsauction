from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.ItemsListView.as_view(), name='items-list'), #Main page should be a list view of all items in the auction
    url(r'^item/(?P<pk>\d+)$', views.item_detail_view, name='item-detail'), #Details page for each auction item
    #url(r'^item/(?P<pk>\d+)/accepted$', views.item_bid_accepted, name='bid-accepted'), #Page to display when a new bid has been accpeted on an item
    
]