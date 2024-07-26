import axios from 'axios'
export default {
  obtenerListadoEmpresa () {
      return axios({
          url     : 'http://localhost:5000/api/tu_empleado_perfecto/empresa/obtenerListadoEmpresa',
          method  : 'get'
      })
  },
  guardarDatosEmpresa (data) {
      return axios({
          url     : 'http://localhost:5000/api/tu_empleado_perfecto/empresa/guardarDatosEmpresa',
          data    : data,
          method  : 'post'
      })
  },
}
