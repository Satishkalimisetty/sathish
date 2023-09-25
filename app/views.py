from django.shortcuts import render

# Create your views here.
from app.models import *
  

def display_topics(request):

    QSTO=topic.objects.all()

    d={'QSTO':QSTO}
    return render(request,'display_topics.html',d)

def display_webpage(request):
    QSWO=webpage.objects.all()

    d={'QSWO':QSWO}
    return render(request,'display_webpage.html',d)

def display_accessrecord(request):
    QSAO=accessrecord.objects.all()

    d={'QSAO':QSAO}
    return render(request,'display_accessrecord.html',d)

def insert_topic(request):
    na=input("enter topic_name")
    to=topic.objects.get_or_create(topic_name=na)[0]
    to.save()
    QSTO=topic.objects.all()

    d={'QSTO':QSTO}
    return render(request,'display_topics.html',d)

def insert_webpage(request):
    na=input("enter topic_name")
    n=input('enter name :')
    u=input('enter url :')
    to=topic.objects.get(topic_name=na)
    wo=webpage.objects.get_or_create(topic_name=to,name=n,url=u)[0]
    wo.save()
    QSWO=webpage.objects.all()

    d={'QSWO':QSWO}
    return render(request,'display_webpage.html',d)
     
def insert_accessrecord(request):
    na=input("enter name:")
    da=input("enter date:")
    au=input("enter author name:")
    em=input("enter email:")
    wo=webpage.objects.get(name=na)
    ao=accessrecord.objects.get_or_create(name=wo,date=da,author=au,email=em)[0]
    ao.save()
    QSAO=accessrecord.objects.all()

    d={'QSAO':QSAO}
    return render(request,'display_accessrecord.html',d)
     

