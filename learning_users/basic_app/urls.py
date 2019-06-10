from basic_app import views
from django.conf.urls import url,include

#TEMPLATE URLs

app_name ='basic_app'

urlpatterns =[
    url(r'^register/$', views.register, name ='register')

]
