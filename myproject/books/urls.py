from django.urls import path
from . import views

urlpatterns = [
    # /books/
    path('', views.index.as_view(), name='index'),
    # registration
    path('register/',views.UserformView.as_view(),name='userform'),
    # /books/id
    path('<pk>/', views.details.as_view(), name='details'),
    
]

