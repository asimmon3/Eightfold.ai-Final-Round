from django.urls import path
from aboutme import views 

app_name = 'aboutme'

urlpatterns = [
    path('', views.about_me, name="about_me"),
    path('<int:aboutme_id>/', views.detail, name = 'detail'),
]