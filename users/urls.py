from django.urls import path
from .views import (
HomeView,
Login,
Logout,
Signin,
)

app_name = 'users'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('signin/', Signin.as_view(), name='signin'),
]