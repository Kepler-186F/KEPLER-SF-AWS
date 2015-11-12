---
layout: post
title: "Django Micro-services template "
date: 2015-11-07 11:24:22 -0500
comments: true
categories:
---
This post wrap up a hello-world demo for django Microservices web app, and shold serve well as a template.

First, What is Pattern: Microservices Architecture:

refer below from http://microservices.io/patterns/microservices.html

Context
You are developing a server-side enterprise application. It must support a variety of different clients including desktop browsers, mobile browsers and native mobile applications. The application might also expose an API for 3rd parties to consume. It might also integrate with other applications via either web services or a message broker. The application handles requests (HTTP requests and messages) by executing business logic; accessing a database; exchanging messages with other systems; and returning a HTML/JSON/XML response.

The application has either a layered or hexagonal architecture and consists of different types of components:

Presentation components - responsible for handling HTTP requests and responding with either HTML or JSON/XML (for web services APIS)
Business logic - the application’s business logic
Database access logic - data access objects responsible for access the database
Application integration logic - messaging layer, e.g. based on Spring integration.
There are logical components corresponding to different functional areas of the application.

The motivations are :

There is a team of developers working on the application
New team members must quickly become productive
The application must be easy to understand and modify
You want to practice continuous deployment of the application
You must run multiple copies of the application on multiple machines in order to satisfy scalability and availability requirements
You want to take advantage of emerging technologies (frameworks, programming languages, etc)

So what is Microservice Architecture:
{% img /images/img/4.jpg %}



Reference ends here. Now start my demo code. Below is how I plan to do it:
{% img /images/img/5.png %}



Tier one app. It's an empty app, only has Settings.py and url.py is important. You start your whole application by bootstraping this app python manage.py runserver from here.


settings.py
```
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'keplerapp_tbcheck',
    'keplerapp_tbmodel',
)
```


url.py
```
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'keplerweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^demo/', include(keplerapp_tbcheck.urls)),
    url(r'^$', include(keplerapp_tbcheck.urls)),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', include(admin.site.urls))
)
```


Now go to another tier one app, tbcheck. This app serves as view app, with all template, tamplate tag, css stuff there
url.py
```
urlpatterns = patterns('',
    url(r'', 'keplerapp_tbcheck.views.service_check'),
    url(r'template', 'keplerapp_tbcheck.views.service_default')
)
```

views.py
```
from keplerapp_tbmodel.models import Employee

def service_check(request):
    emp = Employee()
    emp.truncate()
    emp.prepare_data()

    sec_orglist = map(lambda x:x.EmpName,emp.get_Name_by_OrgID(2))

    context={}
    context['sec_orglist']=sec_orglist
    context['dictionary_key_A']='value of dictionary key A: 10230'
    return render_to_response('keplerapp_tbcheck/intro_index.html', context)

def service_default(request):
    #return HttpResponse("defalt page 404")
    return render_to_response('keplerapp_tbcheck/intro_index.html', {})
```

At last is tier two app. tbmodel

Only has models.py in it. It is just another package.

```
from django.db import models
from datetime import datetime

class Employee(models.Model):
	EmpID = models.AutoField(primary_key=True,blank=True)
	OrgId = models.CharField(max_length=50, db_index=True)#PNC
	EmpLevelCode = models.IntegerField(db_index=True,blank=True,null=True)#6
	EmpName = models.CharField(max_length=100)#Gender
	EmpGender = models.CharField(max_length=50,blank=True,null=True)#F
	EmpHire_dttm = models.DateTimeField(blank=True,null=True)
	upd_dttm = models.DateTimeField(auto_now=True)

	def __unicode__(self):
		return u'System: %s'%self.EmpName

	class Meta:
		app_label = 'keplerapp_tbmodel'
		db_table = u'employee'

	#Return a Generic object
	@classmethod
	def get_Name_by_EmpID(cls,EmpID):
		return cls.objects.filter(EmpID=EmpID)

	@classmethod
	def get_Name_by_OrgID(cls,OrgId):
		return cls.objects.filter(OrgId=OrgId)

	@classmethod
	def truncate(cls):
		cls.objects.all().delete()

	@classmethod
	def prepare_data(cls):
		Employee(OrgId='2',EmpLevelCode=1,EmpName='Ethan W').save()
		Employee(OrgId='2',EmpLevelCode=1,EmpName='Tom H').save()
		Employee(OrgId='2',EmpLevelCode=2,EmpName='Eric G').save()
		Employee(OrgId='3',EmpLevelCode=1,EmpName='Larry E').save()
		Employee(OrgId='3',EmpLevelCode=2,EmpName='Larry P').save()
```


now when we run it, we first pip install all view, model app as package to site-package places. Then bootstrap the first app to start.

To access code and see hello world in 5 sec, just go to this link:
```
https://github.com/Template-EthanFavoriate/TEMPLATE_MICROSERVICE
git@github.com:Template-EthanFavoriate/TEMPLATE_MICROSERVICE.git
```
