from django.urls import path
from .views import assistent

urlpatterns = [
    path('', view=assistent, name='assistent')
]
