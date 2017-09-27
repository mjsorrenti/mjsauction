from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.item_list_view, name='items-list'), #Main page should be a list view of all items in the auction
    url(r'^item/(?P<pk>\d+)$', views.item_detail_view, name='item-detail'), #Details page for each auction item
    url(r'^userpage/$', views.user_page_view, name='user-page'), #Summary page for the logged in user
    
]