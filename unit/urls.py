from django.urls import path
from .views import polling_unit_result

urlpatterns = [
    path('', polling_unit_result, name='polling_unit_result'),
]
