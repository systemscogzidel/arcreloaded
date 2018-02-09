from django.conf.urls import url
from django.contrib import admin
from new_app import views
urlpatterns = [
    url(r'^admin/', admin.site.urls),   
    url(r'^$', views.sitesetting, name='index'),

]