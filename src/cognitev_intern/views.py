from django.http import JsonResponse
from django.shortcuts import render
from django.db.models import Count
from RestfulAPI.models import Campaign

def home(request):
        
    ## All Data (Country , Category)
    #all_data = Campaign.objects.values('country','category').distinct()
    return render(request,'home.html',{})

def get_data(request):
    ## countries Number 
    country_data = Campaign.objects.values('country').distinct()
    category_data = Campaign.objects.values('category').distinct()
    #print(category_data)

    lists = list()
    for i in range(country_data.count()):
        lists.append(list(country_data[i].values()))

    listOfCountries = []
    for i in lists:
        for j in i:
            listOfCountries.append(j)

    lists = list()
    for i in range(category_data.count()):
        lists.append(list(category_data[i].values()))

    listOfCategories = []
    for i in lists:
        for j in i:
            listOfCategories.append(j)



    egy_tech_counter = Campaign.objects.all().filter(country='EGY',category='Technology').count()
    egy_sports_counter = Campaign.objects.all().filter(country='EGY',category='Sports').count()
    USA_tech_counter = Campaign.objects.all().filter(country='USA',category='Technology').count()
    USA_sports_counter = Campaign.objects.all().filter(country='USA',category='Sports').count()






    final_data = {
        'list_country':listOfCountries,
        'list_category':listOfCategories,
        'egy_tech_counter':egy_tech_counter,
        'egy_sports_counter':egy_sports_counter,
        'usa_tech_counter':USA_tech_counter,
        'usa_sports_counter':USA_sports_counter,
    } 
    return JsonResponse(final_data)