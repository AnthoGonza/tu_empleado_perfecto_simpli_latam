from rest_framework                     import status
from datetime                           import datetime
from ..models.empleado                  import Empleado
from empresa.models.empresa             import Empresa
from ..serializers.empleadoSerializer   import EmpleadoSerializer
from django.db                          import transaction

class EmpleadoService:

    def __init__(self):
        self.data = {}
        self.codigo = 0
        self.msg = ''
        self.name = ''
    
    def obtenerListadoEmpleadoPorEmpresaId(self, empresa_id):
        resp        = {}
        mensaje     = ''
        titulo      = ''
        codigo      = 0
        status_resp = ''
        icono       = 'warning'
        data        = []

        try:
            empleado_resultado  = Empleado.objects.filter(empresaid = empresa_id).order_by('id')
            data_serializer     = EmpleadoSerializer(empleado_resultado, many=True)
            
            titulo      = 'Datos obtenidos exitosamente'
            mensaje     = 'Proceso finalizado'
            icono       = 'success'
            codigo      = 1
            data        = data_serializer.data
            status_resp = status.HTTP_200_OK
        except Exception as e:
            titulo      = 'Se encontró un invonveniente al obtener datos'
            mensaje     = str(e)
            icono       = 'warning'
            codigo      = 0
            status_resp = status.HTTP_500_INTERNAL_SERVER_ERROR
        finally:
            resp['status']  = status_resp
            resp['code']    = codigo
            resp['titulo']  = titulo
            resp['mensaje'] = mensaje
            resp['icono']   = icono
            resp['data']    = data
        return resp
        
    
    def guardarDatosEmpleado(self, data_param):
        resp        = {}
        mensaje     = ''
        titulo      = ''
        codigo      = 0
        status_resp = ''
        icono       = 'warning'

        try:
            id              = int(data_param['id'])
            fecha_registro  = datetime.today().date()
            empresa_id      = int(data_param['empresa_id'])
            rut             = int(data_param['rut'])
            dv              = data_param['dv']
            nombres         = data_param['nombres']
            apellido_uno    = data_param['apellido_uno']
            apellido_dos    = data_param['apellido_dos']
            email           = data_param['email']

            empresa_instance = Empresa.objects.filter(id = empresa_id).get()
            ##VALIDANDO DE QUE RUT NO ESTEA REGISTRADO PARA OTRO EMPLEADO
            empleado_validacion = Empleado.objects.exclude(id = id).filter(rut = rut)
            if empleado_validacion.exists() == False:
                if id == 0:
                    Empleado.objects.create(
                        fecharegistro   = fecha_registro,
                        empresaid       = empresa_instance,
                        rut             = rut, 
                        dv              = dv, 
                        nombres         = nombres, 
                        apellidouno     = apellido_uno,  
                        apellidodos     = apellido_dos,  
                        email           = email
                    )  
                    codigo      = 1
                    titulo      = 'Datos guardados exitosamente'
                    icono       = 'success'
                else:
                    empleado_instance = Empleado.objects.filter(id = id)
                    if empleado_instance.exists():
                        empleado_instance               = empleado_instance.get()
                        empleado_instance.rut           = rut
                        empleado_instance.dv            = dv
                        empleado_instance.nombres       = nombres
                        empleado_instance.apellidouno   = apellido_uno
                        empleado_instance.apellidodos   = apellido_dos
                        empleado_instance.email         = email
                        empleado_instance.save()
                        codigo      = 1
                        titulo      = 'Datos guardados exitosamente'
                        icono       = 'success'
                    else:
                        codigo      = 0
                        titulo      = 'No se encontró identificador empleado'
            else:
                codigo      = 0
                titulo      = 'RUT ya está asignado a otro empleado'

            mensaje     = 'Proceso finalizado'
            status_resp = status.HTTP_200_OK
        except Exception as e:
            titulo      = 'Se encontró un invonveniente al guardar datos'
            mensaje     = str(e)
            icono       = 'warning'
            codigo      = 0
            status_resp = status.HTTP_500_INTERNAL_SERVER_ERROR
        finally:
            resp['status']  = status_resp
            resp['code']    = codigo
            resp['titulo']  = titulo
            resp['mensaje'] = mensaje
            resp['icono']   = icono
        return resp