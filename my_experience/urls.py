from django.urls import re_path
from .views import my_experience
#url for app
urlpatterns = [
    re_path(r'^$', my_experience, name='my_experience'),
]
