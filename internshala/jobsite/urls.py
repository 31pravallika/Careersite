from django.urls import path
from . import views
from django.contrib.auth.views import LoginView
# from .views import CandidateLoginView, EmployerLoginView
urlpatterns=[
    path('',views.index,name='index'),
   path('login',views.login,name='login'),
    
    # path('Jlogin', LoginView.as_view(template_name='Jlogin.html'), name='Jlogin'),
    # path('Elogin', LoginView.as_view(template_name='Elogin.html'), name='Elogin'),
    path('jobs',views.jobs,name='jobs'),
    path('register',views.register,name='register'),
    path('hire',views.hire,name='hire'),
    path('logout',views.logout,name='logout'),
    path('chome',views.chome,name='chome')
]