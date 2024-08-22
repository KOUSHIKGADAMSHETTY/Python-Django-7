from django.urls import path
from vehicle import views
urlpatterns = [
    path('c',views.find),
    path('a',views.addinfo,name='addinfo'),
    path('v',views.user,name='user info'),
    path('f',views.users,name='find user'),
    path('auth',views.Ausers,name='user by Auth()')
]