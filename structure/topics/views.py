from django.shortcuts import render
from topics.forms import form_data,form_data2
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'topics/index.html')

def bio(request):
    return render(request,'topics/bio.html')

def work(request):
    return render(request,'topics/work.html')

def contact(request):

    if request.method == "POST":
        form = form_data(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'You have been Signed Up!')
            return contact(request)
    form = form_data()
    return render(request,'topics/contact.html',{'form':form})

def profilio(request):
    return render(request,'topics/profilio.html')

def maps(request):
    return render(request,'topics/maps.html')

def graphics(request):
    return render(request,'topics/graphics.html')

def three_d(request):
    return render(request,'topics/three_d.html')

def current(request):
    return render(request,'topics/current.html')

def past(request):
    return render(request,'topics/past.html')

def wny(request):
    return render(request,'topics/wny.html')

def pops(request):
    return render(request,'topics/pops.html')

def museum(request):
    return render(request,'topics/museum.html')

def latino(request):
    return render(request,'topics/latino.html')

def scraper(request):
    return render(request,'topics/scraper.html')

def bike(request):
    return render(request,'topics/bike.html')

def bike_amount(request):
    return render(request,'topics/bike_amount.html')

def dotsurvey(request):
    return render(request,'topics/survey_amounts.html')

def DOT(request):
    return render(request,'topics/DOT.html')

def trips(request):
    return render(request,'topics/trips.html')

def json(request):
    return render(request,'topics/citi_users.json')

def citi_zone(request):
    return render(request,'topics/citi_zones.html')

def coding(request):
    return render(request,'topics/coding_portfolio.html')

def city(request):

    if request.method == "POST":
        form = form_data(request.POST)
        form2 = form_data2(request.POST)
        if form.is_valid():
            form.save(commit=True)
            messages.success(request, 'You have been Signed Up!',extra_tags='signup')
            return city(request)
        form2 = form_data2(request.POST)
        if form2.is_valid():
            form2.save(commit=True)
            messages.success(request, 'Thanks for the recommendation!',extra_tags='recommendation')
            return city(request)
    form = form_data()
    form2 = form_data2()

    return render(request,'topics/city.html',{'form':form,'form2':form2})



