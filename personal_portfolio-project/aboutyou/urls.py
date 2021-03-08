from django.urls import path
from aboutyou import views 

app_name = 'aboutyou'

urlpatterns = [
    path('', views.about_you, name="about_you"),
    path('<int:aboutyou_id>/', views.detail, name = 'detail'),
]