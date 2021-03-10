from django.urls import path
from why import views 

app_name = 'why'

urlpatterns = [
    path('', views.why, name="why"),
]