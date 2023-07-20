from django.urls import path
from .views import IndexView
from .views import upgrade_me

app_name = 'protected'
urlpatterns = [
    path('', IndexView.as_view(), name='index'), 
    path('upgrade/', upgrade_me, name = 'upgrade')
]