from django.conf.urls import url
from topics import views

app_name = 'topics'

urlpatterns = [
    url('work/',views.work,name='work'),
    url('bio/',views.bio,name='bio'),
    url('contact/',views.contact,name='contact'),
    url('profilio/',views.profilio,name='profilio'),
    url('maps/',views.maps,name='maps'),
    url('graphics/',views.graphics,name='graphics'),
    url('3d/',views.three_d,name='three_d'),
    url('current/',views.current,name='current'),
    url('past/',views.past,name='past'),
    url('wny/',views.wny,name='wny'),
    url('pops/',views.pops,name='pops'),
    url('museum/',views.museum,name='museum'),
    url('latino/',views.latino,name='latino'),
    url('scraper/',views.scraper,name='scraper'),
    url('city/',views.city,name='city'),
    url('bike/',views.bike,name='bike'),
    url('bike_amount/',views.bike_amount,name='bike_amount'),
    url('dotsurvey/',views.dotsurvey,name='dotsurvey'),
    url('dotsurvey/',views.dotsurvey,name='dotsurvey'),
    url('DOT/',views.DOT,name='DOT'),
    url('trips/',views.trips,name='trips'),
    url('json/',views.json,name='json'),
    url('citi_zone/',views.citi_zone,name='citi_zone'),
    url('coding/',views.coding,name='coding'),

]

