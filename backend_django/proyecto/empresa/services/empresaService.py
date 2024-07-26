from rest_framework                     import status
from datetime                           import datetime
from ..models.empresa                   import Empresa
from ..serializers.empresaSerializer    import EmpresaSerializer
from django.db                          import transaction

class EmpresaService:

    def __init__(self):
        self.data = {}
        self.codigo = 0
        self.msg = ''
        self.name = ''
    
    def obtenerListadoEmpresa(self):
        resp        = {}
        mensaje     = ''
        titulo      = ''
        codigo      = 0
        status_resp = ''
        icono       = 'warning'
        data        = []

        try:
            empresa_resultado   = Empresa.objects.order_by('id')
            data_serializer     = EmpresaSerializer(empresa_resultado, many=True)
            
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
        
    
    def guardarDatosEmpresa(self, data_param):
        resp        = {}
        mensaje     = ''
        titulo      = ''
        codigo      = 0
        status_resp = ''
        icono       = 'warning'

        try:
            id              = int(data_param['id'])
            fecha_registro  = datetime.today().date()
            rut             = data_param['rut']
            dv              = data_param['dv']
            nombre          = data_param['nombre']
            direccion       = data_param['direccion']
            telefono        = int(data_param['telefono'])

            ##VALIDANDO DE QUE RUT NO ESTEA REGISTRADO PARA OTRA EMPRESA
            empresa_validacion = Empresa.objects.exclude(id = id).filter(rut = rut)
            if empresa_validacion.exists() == False:
                if id == 0:
                    Empresa.objects.create(
                        fecharegistro   = fecha_registro,
                        rut             = rut, 
                        dv              = dv, 
                        nombre          = nombre, 
                        direccion       = direccion,  
                        telefono        = telefono
                    )  
                    codigo      = 1
                    titulo      = 'Datos guardados exitosamente'
                    icono       = 'success'
                else:
                    empresa_instance = Empresa.objects.filter(id = id)
                    if empresa_instance.exists():
                        
                        empresa_instance = empresa_instance.get()
                        empresa_instance.rut        = rut
                        empresa_instance.dv         = dv
                        empresa_instance.nombre     = nombre
                        empresa_instance.direccion  = direccion
                        empresa_instance.telefono   = telefono
                        empresa_instance.save()
                        codigo      = 1
                        titulo      = 'Datos guardados exitosamente'
                        icono       = 'success'
                    else:
                        codigo      = 0
                        titulo      = 'No se encontró identificador empresa'
            else:
                codigo      = 0
                titulo      = 'RUT ya está asignado a otra empresa'

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