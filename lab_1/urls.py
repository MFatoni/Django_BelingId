from django.urls import re_path
from .views import index
from .views import portofolio
#url for app
urlpatterns = [
    re_path(r'^$', index, name='index'),
    re_path(r'^$', portofolio, name='portofolio'),
]
