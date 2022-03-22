from django.urls import path
from .views import home, download_page



urlpatterns = [
    path('', home, name='home'),
    path('download', download_page, name='download')
]