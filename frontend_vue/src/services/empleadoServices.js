import axios from 'axios'
export default {
  obtenerListadoEmpleadoPorEmpresaId (empresa_id) {
      return axios({
          url     : process.env.VUE_APP_DOMAIN_ENV + '/api/tu_empleado_perfecto/empleado/obtenerListadoEmpleadoPorEmpresaId?empresa_id=' + empresa_id,
          method  : 'get'
      })
  },
  guardarDatosEmpleado (data) {
      return axios({
          url     : process.env.VUE_APP_DOMAIN_ENV + '/api/tu_empleado_perfecto/empleado/guardarDatosEmpleado',
          data    : data,
          method  : 'post'
      })
  },
}
