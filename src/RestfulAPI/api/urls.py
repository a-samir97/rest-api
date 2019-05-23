from django.contrib import admin
from django.urls import path,include
from RestfulAPI.api.views import CampaignDetail,CampaignList

urlpatterns = [
    path('campaign/', CampaignList.as_view(),name='list'),
    path('campaign/<int:pk>',CampaignDetail.as_view(),name='detail'),
]