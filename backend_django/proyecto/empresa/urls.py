# from django.urls import include, path

from posixpath import basename
import re
from rest_framework import routers
from django.urls import include,re_path as url

from empresa.views import empresa

empresa_router = routers.SimpleRouter(trailing_slash=False)

empresa_router.register(r'empresa', empresa.EmpresaViewset , basename='re_empresa')

app_name = 'empresa'

urlpatterns = [
    url('tu_empleado_perfecto/', include(empresa_router.urls)),
]