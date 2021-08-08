from django.urls import path
from . import views
urlpatterns = [

    path('',views.sign_up.as_view(),name='signup'),
    path('login',views.user_login.as_view(),name='login'),
    path('profile',views.user_profile,name='profile'),
    path('logout',views.user_logout.as_view(),name='logout'),

]