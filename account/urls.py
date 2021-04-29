from django.urls import path

from account.views import *

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('register/', RegistrationView.as_view()),
    path('get_role/', GetRole.as_view()),

]