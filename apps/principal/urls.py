from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='principal/home.html'),
         name='index'), 
    #url(r'^$', views.index, name='index'), # func View
]