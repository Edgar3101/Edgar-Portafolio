from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .models import Initial, Secondary , social_media, my_work
from portafolios.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError

def home(request):
    home_view= Initial.objects.all()
    secondary_views= Secondary.objects.all()
    social_media_views = social_media.objects.all()
    template = loader.get_template('portafolios/index.html')
    context = {
        'home_view': home_view,
        'secondary_views' : secondary_views,
        'social_media_views' : social_media_views,
    }
    return HttpResponse(template.render(context, request))
def about_me(request):
    about_me_views= Initial.objects.all()
    social_media_views = social_media.objects.all()
    template = loader.get_template('portafolios/about_me.html')
    context= {
        'about_me_views': about_me_views,
        'social_media_views' : social_media_views,
    }
    return HttpResponse(template.render(context, request))
def my_recent_work(request):
    my_work_views= my_work.objects.all()
    social_media_views = social_media.objects.all()
    template = loader.get_template('portafolios/Recent_work.html')
    context= {
        'my_work_views': my_work_views,
        'social_media_views' : social_media_views,
    }
    return HttpResponse(template.render(context, request))


def contacts(request):
    social_media_views = social_media.objects.all()
    template = loader.get_template('portafolios/contacts.html')
    context= {
        'social_media_views' : social_media_views,
    }
    return HttpResponse(template.render(context, request))

def navbar(request):
    home_view= Initial.objects.all()
    template = loader.get_template('portafolios/navbar.html')
    context = {
        'home_view': home_view,
    }
    return HttpResponse(template.render(context, request))


    



    
# Create your views here.
