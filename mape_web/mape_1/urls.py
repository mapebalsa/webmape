from django.conf.urls import patterns, url
from mape_1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns = [
url(r'^$', views.index, name = "index" ),
url(r'^productos/', views.category, name='categoria'),
#url(r'^about/$', views.about, name='about'),
#url(r'^categoria/(?P<category_name_slug>[\w\-]+)/$', views.category_1, name='categoria_1'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)