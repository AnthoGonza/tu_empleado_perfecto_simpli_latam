# from django.urls import include, path

from posixpath import basename
import re
from rest_framework import routers
from django.urls import include,re_path as url

from empleado.views import empleado

empleado_router = routers.SimpleRouter(trailing_slash=False)

empleado_router.register(r'empleado', empleado.EmpleadoViewset , basename='re_empleado')

app_name = 'empleado'

urlpatterns = [
    url('tu_empleado_perfecto/', include(empleado_router.urls)),
]