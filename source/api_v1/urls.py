from django.urls import path

from .views import (
    json_echo_view,
    get_csrf_token,
    add,
    subtract,
    multiply,
    divide,
)
app_name = 'api_v1'

urlpatterns = [
    path('echo/', json_echo_view),
    path("get-csrf-token/", get_csrf_token),
    path('add/', add, name='add'),
    path('subtract/', subtract, name='subtract'),
    path('multiply/', multiply, name='multiply'),
    path('divide/', divide, name='divide')
]