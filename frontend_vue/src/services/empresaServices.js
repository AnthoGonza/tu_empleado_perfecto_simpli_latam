import axios from 'axios'
export default {
  obtenerListadoEmpresa () {
      return axios({
          url     : process.env.VUE_APP_DOMAIN_ENV + '/api/tu_empleado_perfecto/empresa/obtenerListadoEmpresa',
          method  : 'get'
      })
  },
  guardarDatosEmpresa (data) {
      return axios({
          url     : process.env.VUE_APP_DOMAIN_ENV + '/api/tu_empleado_perfecto/empresa/guardarDatosEmpresa',
          data    : data,
          method  : 'post'
      })
  },
}
