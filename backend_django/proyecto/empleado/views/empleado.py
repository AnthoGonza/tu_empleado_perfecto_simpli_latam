import re
from django.db.transaction          import atomic
from rest_framework                 import viewsets, exceptions
from rest_framework.permissions     import IsAuthenticated
from rest_framework.decorators      import action
from rest_framework.response        import Response
from rest_framework.generics        import get_object_or_404
from ..services.empleadoService     import EmpleadoService

class EmpleadoViewset(viewsets.GenericViewSet):
    @atomic
    @action(detail=False, methods=['GET'], url_path='obtenerListadoEmpleadoPorEmpresaId')
    def obtenerListadoEmpleadoPorEmpresaId(self, request, *args, **kwargs) -> Response:
        """
            @url: http://{{host}}:{{port}}/api/tu_empleado_perfecto/empleado/obtenerListadoEmpleadoPorEmpresaId
            @succesful_response: HTTP 200 (OK)
            @description: Trae todas las empleados
        """

        if request.query_params.get('empresa_id', None) is None:
            return Response({'message': 'identificador empresa no se recibio'})
        
        empresa_id  = request.query_params.get('empresa_id', None)
        service     = EmpleadoService()
        resp        = service.obtenerListadoEmpleadoPorEmpresaId(empresa_id)
        
        return Response(resp)
     
    @atomic
    @action(detail=False, methods=['POST'], url_path='guardarDatosEmpleado')
    def guardarDatosEmpleado(self, request, *args, **kwargs) -> Response:
        """
            @url: http://{{host}}:{{port}}/api/tu_empleado_perfecto/empleado/guardarDatosEmpleado
            @succesful_response: HTTP 200 (OK)
            @description: Agrega/actualiza datos empleado
        """

        data_param  = request.POST.dict()
        service     = EmpleadoService()
        resp        = service.guardarDatosEmpleado(data_param)
        
        return Response(resp)

        
        

        


        
        


    





