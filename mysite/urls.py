from django.urls import path, include

urlpatterns = [
    path('post', include('posting.urls'))
]
