from django.urls   import path

from posting.views import *

urlpatterns = [
    path('/posting', Posting.as_view()),
]