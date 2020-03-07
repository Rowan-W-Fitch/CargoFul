from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    #return HttpResponse("why is bars gay?")
    return render(request, 'shipper/index.html') # this renders the html code within the templates\shipper\ dir
    
