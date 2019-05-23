## CRUD Operations
from rest_framework.views import APIView
from ..models import Campaign
from .serializer import CampaignSerializer
from rest_framework.response import Response
from rest_framework import status
## CREATE ##

## DELETE ##

## UPDATE ##

## RETRIEVE ##
'''
List all Campaigns , Create a new Campaign
'''
class CampaignList(APIView):
    def get(self,request,format=None):
        camp = Campaign.objects.all()
        serializer = CampaignSerializer(camp,many=True)
        return Response(serializer.data)
    
    def post(self,request,format=None):
        serializer = CampaignSerializer(data=request.data)
        if  serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CampaignDetail(APIView):
    def get_object(self,pk):
        try:
            return Campaign.objects.get(pk=pk)
        except Campaign.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    '''
    to retrieve campaign
    '''
    def get(self,request,pk,format=None):
        camp = self.get_object(pk)
        serializer = CampaignSerializer(camp)
        return Response(serializer.data)
    '''
    to update campaign
    '''
    def put(self,request,pk,format=None):
        camp = self.get_object(pk)
        serializer = CampaignSerializer(camp,data=request.data)
        if  serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    '''
    to delete campaign
    '''
    def delete(self,request,pk,format=None):
        camp = self.get_object(pk)
        camp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
