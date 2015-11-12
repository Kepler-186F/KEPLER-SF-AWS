from django.conf.urls import patterns,include,url


urlpatterns = patterns('',
    # Examples:
	#url(r'^all/$','kepler_responsor_app.views.hello'),

	url(r"^getGoogleSuggestion/.*$",'kepler_responsor_app.views.googleSuggestion'),
	#url(r"^get/'.*'$",'kepler_responsor_app.views.getany'),
	url(r"^get/.*$",'kepler_responsor_app.views.getany'),
	url(r"^",'kepler_responsor_app.views.getany'),
	#url(r"^getSuggestion/.*$",'kepler_responsor_app.views.googleSuggestion'),
)
