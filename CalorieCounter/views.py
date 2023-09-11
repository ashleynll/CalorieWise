from django.shortcuts import render

#0okBIYMy7j0d0kmZZK8Cpw==qnuhxTfcx3XPxQL4
# Create your views here.
def home(request):
    import requests
    import json
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(api_url + query, headers= {'X-Api-Key': '0okBIYMy7j0d0kmZZK8Cpw==qnuhxTfcx3XPxQL4'}) #send in request to api url and query 
        try:
            api = json.loads(api_request.content) #fetch the content
            # print(api_request.content)
        except Exception as e:
            api = "An error has occured"
            print(e)
        return render(request, 'home.html',{'api':api})
    else:
        return render(request, 'home.html',{'query':'Enter a valid query'})




