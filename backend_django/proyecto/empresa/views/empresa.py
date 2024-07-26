import re
from django.db.transaction          import atomic
from rest_framework                 import viewsets, exceptions
from rest_framework.permissions     import IsAuthenticated
from rest_framework.decorators      import action
from rest_framework.response        import Response
from rest_framework.generics        import get_object_or_404
from ..services.empresaService      import EmpresaService

    
class EmpresaViewset(viewsets.GenericViewSet):
    @atomic
    @action(detail=False, methods=['GET'], url_path='obtenerListadoEmpresa')
    def obtenerListadoEmpresa(self, request, *args, **kwargs) -> Response:
        """
            @url: http://{{host}}:{{port}}/api/tu_empleado_perfecto/empresa/obtenerListadoEmpresa
            @succesful_response: HTTP 200 (OK)
            @description: Trae todas las empresas
        """

        service = EmpresaService()
        resp    = service.obtenerListadoEmpresa()
        
        return Response(resp)
     
    @atomic
    @action(detail=False, methods=['POST'], url_path='guardarDatosEmpresa')
    def guardarDatosEmpresa(self, request, *args, **kwargs) -> Response:
        """
            @url: http://{{host}}:{{port}}/api/tu_empleado_perfecto/empresa/guardarDatosEmpresa
            @succesful_response: HTTP 200 (OK)
            @description: Agrega/actualiza datos empresa
        """

        data_param  = request.POST.dict()
        service     = EmpresaService()
        resp        = service.guardarDatosEmpresa(data_param)
        
        return Response(resp)

        
        

        


        
        


    





