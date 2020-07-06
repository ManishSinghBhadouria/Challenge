from django.shortcuts import render,redirect
from .models import Registration,Location,Weather
from django.contrib import messages


# Create your views here.

def home(request):
    allrecord = Registration.objects.all()
    return render(request, 'index.html',{'allrecord': allrecord})


def delete(request,id):
    Registration.objects.filter(id=id).delete()
    return redirect("home")


def register(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        email = request.POST['email']
        last_name = request.POST['lname']
        if Registration.objects.filter(email=email).exists():
            messages.info(request, 'Email Already Exist !!!!')
            return redirect('home')
        user = Registration(first_name=first_name ,email=email, last_name=last_name)
        user.save()
        messages.info(request, 'Registered Successfully!!!!')
        return redirect('home')        
    return redirect('home')


def iploc1(request):
    if request.method == 'POST':
        city = request.POST['city']
        state = request.POST['state']
        country = request.POST['country']
        user = Location(city=city,state=state,country=country)
        user.save()
        messages.info(request, 'Inserterd Successfully!!!!')
        return redirect('iploc')        
    return redirect('home')



def update(request,id):
    info= Registration.objects.get(id=id)
    context={'user':info}
    return render(request,'update.html',context)


def update1(request):
    if request.method == 'POST':
        first_name = request.POST['fname']
        email = request.POST['email']
        last_name = request.POST['lname']
        if Registration.objects.filter(email=email).update(first_name=first_name , last_name=last_name):
            messages.info(request, 'Updated Successfully !!!!')
            return redirect('home')       
    return redirect('home')



def iploc(request): 
    import geocoder
    allrecord = Location.objects.all()
    g = geocoder.ip('me')
    from geopy.geocoders import Nominatim
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.reverse(g.latlng, exactly_one=True)
    address = location.raw['address']
    city = address.get('city', '')
    state = address.get('state', '')
    country = address.get('country', '')

    a=str(city)
    b=str(state)
    c=str(country)
    return render(request,'location.html',{'allrecord':allrecord,'a':a,'b':b,'c':c})


def weather_data(request): 
    import requests, json  
    allrecord = Weather.objects.all()
    api_key = "a930aa35ee42cf74b1a2ea7b4fdf4dec"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    import geocoder
    g = geocoder.ip('me')
    from geopy.geocoders import Nominatim
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.reverse(g.latlng, exactly_one=True)
    address = location.raw['address']
    city = address.get('city', '')
    city_name = str(city) 
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
    response = requests.get(complete_url) 
    x = response.json()
    if x["cod"] != "404": 
        y = x["main"] 
        current_temperature = y["temp"] 
        Celsius = current_temperature - 273.15
        current_pressure = y["pressure"]  
        current_humidiy = y["humidity"] 
        z = x["weather"] 
        weather_description = z[0]["description"] 
        return render(request,'weather.html',{'allrecord':allrecord,'Celsius':Celsius,'city_name':city_name,'current_temperature':current_temperature,'current_pressure':current_pressure,'current_humidiy':current_humidiy,'weather_description':weather_description})
    else: 
        messages.info(request, 'Unable To Find Current Valid City !!!!')
        return redirect('home')
    messages.info(request, 'Unable To Find Current Valid City !!!!')
    return redirect('home')


def weather_data1(request):
    if request.method == 'POST':
        city = request.POST['city']
        temp = request.POST['temp']
        temp1 = request.POST['temp1']
        humi = request.POST['humi']
        press = request.POST['press']
        desc = request.POST['desc']
        user = Weather(city=city,temp=temp,temp1=temp1,humi=humi,press=press,sdesc=desc)
        user.save()
        messages.info(request, 'Inserterd Successfully!!!!')
        return redirect('weather_data')        
    return redirect('weather_data')
