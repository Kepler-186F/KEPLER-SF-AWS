from django.shortcuts import render
from django.http import HttpResponse
from xml.dom import minidom
import urllib
# Create your views here.

#Unified Url fetch function
def getsource(url):
    connection=urllib.urlopen(url)
    result=connection.read()
    return result

#handled all request
def getany(request):
    result = request.path
    print request.get_full_path()
    #print request.get_full_path().find('/get/')
    url = request.get_full_path()[1:]
    if (request.get_full_path().find('/get/')!=-1):
        url = request.get_full_path()[5:]
    #print request
    print url
    result=getsource(url)
    #print result
    return HttpResponse(result)

#handle googlesearch request
def googleSuggestion(request):
    #expect request is  localhost:7000/getGoogleSuggestion/Hello
    gettarget=request.path[21:]
    url='http://google.com/complete/search?output=toolbar&q='+gettarget
    #print url
    result=getsource(url)
    doc = minidom.parseString(result)

    suggestions = doc.getElementsByTagName("CompleteSuggestion")
    list=[]
    for suggestion in suggestions:
    	#print suggestion
    	target=suggestion.getElementsByTagName("suggestion")[0].toxml()
    	#print target[17:-2]
    	list.append(target[18:-3])
    #print list
    return HttpResponse(','.join(list))
