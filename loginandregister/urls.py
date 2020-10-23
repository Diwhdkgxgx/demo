from firstweek.urls import path
from loginandregister.views import *

urlpatterns = [
    path('login/', login, name = 'login'),
    path('register/', regisiter, name = 'register'),
    path('main/',main, name='main'),
]
