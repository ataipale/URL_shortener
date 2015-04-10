from django.conf.urls import include, url


from . import views

urlpatterns = [
	url(r'^$', views.IndexView.as_view()),
	url(r'^success/(?P<unique_id>[0-9a-zA-z]+)/$', views.SuccessView.as_view()),
	url(r'^(?P<unique_id>[0-9a-zA-z]+)$', views.ShortLinkRedirectView.as_view())
]
