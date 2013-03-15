from django.conf.urls.defaults import patterns,url

urlpatterns = patterns('apps.www.views',
	url(r'^add/post/$','add_post_view',name= "Vista_agregar_post"),
)
