<template>
    <app-header />
    <main class="px-1">
        <div class="card">
            <div class="card-header">
                <div class="row py-2"> 
                    <div class="col-xl-6 col-md-6 col-sm-6" align="left">
                        <label class="mb-0 mt-2">Listado empleados</label>                    
                    </div>
                    <div class="col-xl-6 col-md-6 col-sm-6" align="right">
                        <div class="input-group">
                            <select class="form-select"  v-model="form.empresa_id" @change="obtenerListadoEmpleadoPorEmpresaId()">
                                <option value="0">Seleccione empresa</option>
                                <option v-for="item in empresa_collection" :key="item.id" v-bind:value="item.id">
                                    {{item.rut + "-" + item.dv + " " + item.nombre}}
                                </option>
                            </select>
                            <button :disabled="form.empresa_id == 0 ? true : false" @click="abrirModalEmpleado(null)" class="btn btn-primary btn-sm"><i class="fa fa-plus" aria-hidden="true"></i> Nuevo empleado</button>
                        </div>
                    </div>
                </div>
            </div>
            <div class="card-body">
                <div class="row">
                    <div class="mb-1 mt-2 col-12" align="right">
                        <table class="table">
                            <thead>
                                <tr>
                                <th scope="col">#</th>
                                <th scope="col">RUT</th>
                                <th scope="col">Nombre completo</th>
                                <th scope="col">Email</th>
                                <th class="col-2">Acciones</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-if="this.tabla_empleado.items.length > 0" v-for="item in this.tabla_empleado.items" :key="item.id" >
                                    <td scope="row">{{item.id}}</td>
                                    <td>{{item.rut + "-" + item.dv}}</td>
                                    <td>{{item.nombres + " " + item.apellidouno + " " + item.apellidodos}}</td>
                                    <td>{{item.email}}</td>
                                    <td>
                                        <button class="btn btn-primary btn-sm" @click="abrirModalEmpleado(item)"><i class="fa fa-pencil"></i> Editar</button>
                                        <button class="btn btn-danger btn-sm ml-1" @click="confirmarEliminarEmpleado(item.id)"> <i class="fa fa-trash-o"></i> Eliminar</button>
                                    </td>
                                </tr>
                                <tr v-else>
                                    <td colspan="5" align="center">No hay datos para mostrar</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    </main>
    <div class="modal" 
        v-if="this.form.mostrar"
        tabindex="-1" role="dialog" id="modalVisualizarEmpleado">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title"><i class="fa fa-users" aria-hidden="true"></i> Datos empleado</h5>
            </div>
            <div class="modal-body">
                <div class="row">
                    <div class="col-12 mb-4">
                        <div class="form-group">
                            <label class="titulo" align="left">Rut*</label>
                            <input @keypress="validaCaracteresRut($event)" maxlength="12" @keyup="validaFormatoRut($event)" type="text" class="form-control sm" id="validationCustom03" v-model="form.rut.valor"  required>
                        </div>
                    </div>
                    <div class="col-12 mb-4">
                        <div class="form-group">
                            <label class="titulo" align="left">Nombre*</label>
                            <input type="text" class="form-control sm" id="validationCustom03" v-model="form.nombres.valor" required>
                        </div>
                    </div>
                    <div class="col-12 mb-4">
                        <div class="form-group">
                            <label class="titulo" align="left">Apellido uno*</label>
                            <input type="text" class="form-control sm" id="validationCustom03" v-model="form.apellido_uno.valor" required>
                        </div>
                    </div>
                    <div class="col-12 mb-4">
                        <div class="form-group">
                            <label class="titulo" align="left">Apellido dos*</label>
                            <input type="text" class="form-control sm" id="validationCustom03" v-model="form.apellido_dos.valor" required>
                        </div>
                    </div>
                    <div class="col-12 mb-4">
                        <div class="form-group">
                            <label class="titulo" align="left">Email*</label>
                            <input type="text" class="form-control sm" id="validationCustom03" v-model="form.email.valor" required>
                        </div>
                    </div>
                </div>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-primary" @click="guardarDatosEmpleado()"><i class="fa fa-pencil"></i> Guardar</button>
                <button type="button" class="btn btn-secondary"  @click="cerrarModalEmpleado()"><i class="fa fa-trash-o"></i> Cerrar</button>
            </div>
            </div>
        </div>
    </div>
</template>

<script>
    import header               from '@/components/layout/header.vue'
    import empresaServices      from '@/services/empresaServices.js'
    import empleadoServices     from '@/services/empleadoServices.js'
    import { defineComponent }  from 'vue';

    window.onbeforeunload = function () { window.history.forward(1) }

    export default defineComponent({
        name : 'empleado',
        components: {
            "app-header" : header
        },
        data() {
            return {
                form: {
                    id          : 0,
                    empresa_id  : 0,
                    rut :  {
                        
                        valor   : "",
                        estado  : ""
                    },
                    nombres       :  {
                        valor   : "",
                        estado  : ""
                    },
                    apellido_uno   :  {
                        valor   : "",
                        estado  :    ""
                    },
                    apellido_dos   :  {
                        valor   : "",
                        estado  :    ""
                    },
                    email   :  {
                        valor   : "",
                        estado  :    ""
                    },
                    mostrar : false
                },
                tabla_empleado : {
                    loading         : true,
                    filter          : null,
                    fields        : {
                        id          : { label: 'ID'},
                        rut         : { label: 'RUT'},
                        direccion   : { label: 'Dirección'},
                        accion      : { label: 'Acciones'}
                    },
                    items         : [],
                },
                empresa_collection: [],
            }
        },
        mounted() {
            this.init();
        },
        methods: {
            init(){
                console.log("process.env.VUE_APP_DOMAIN_ENV: " + process.env.VUE_APP_DOMAIN_ENV);
                this.obtenerListadoEmpresa();
                
            },
            obtenerListadoEmpresa(){
                this.empresa_collection = [];
                const swal = this.$swal({
                    title               : 'Obteniendo listado empresas...Por favor espere',
                    text                : '...',
                    icon                : 'info',
                    showConfirmButton   : false,
                    allowOutsideClick   : false,
                    allowEscapeKey  : false
                });

                empresaServices.obtenerListadoEmpresa().then(res => {
                    return res.data
                }).then(data=> {
                    if(data.code == 1){
                        data.data.forEach(dato => {
                            this.empresa_collection.push(dato);
                        });
                    }
                    
                    swal.close()
                }).catch((err) => {
                    console.log(err);
                    this.$swal('Ocurrió un problema al llamar a la api', 'Favor ver detalle por consola', 'error')
                    swal.close()
                });
            },
            obtenerListadoEmpleadoPorEmpresaId(){
                if (this.form.empresa_id == 0) {
                    this.tabla_empleado.items = [];
                } else {
                    this.tabla_empleado.loading  = true;
                    this.tabla_empleado.items    = [];
                    const swal = this.$swal({
                        title               : 'Obteniendo listado empleado...Por favor espere',
                        text                : '...',
                        icon                : 'info',
                        showConfirmButton   : false,
                        allowOutsideClick   : false,
                        allowEscapeKey  : false
                    });
                    empleadoServices.obtenerListadoEmpleadoPorEmpresaId(this.form.empresa_id).then(res => {
                        return res.data
                    }).then(data=> {
                        console.log(data);
                        if(data.code == 1){
                            data.data.forEach(dato => {
                                this.tabla_empleado.items.push(dato);
                            });
                        }
                        this.tabla_empleado.loading  = false;
                        
                        swal.close()
                    }).catch((err) => {
                        console.log(err);
                        this.$swal('Ocurrió un problema al llamar a la api', 'Favor ver detalle por consola', 'error')
                        this.tabla_empleado.loading = false;
                        swal.close()
                    });
                }
            },
            abrirModalEmpleado(data){
                console.log(data);
                if (data == null) {
                    this.form.id                    = 0;
                    this.form.rut.valor             = "";
                    this.form.nombres.valor         = "";
                    this.form.apellido_uno.valor    = "";
                    this.form.apellido_dos.valor    = "";
                    this.form.email.valor           = "";
                } else {
                    this.form.id                    = data.id;
                    this.form.rut.valor             = data.rut + "-" + data.dv;
                    this.form.nombres.valor         = data.nombres;
                    this.form.apellido_uno.valor    = data.apellidouno;
                    this.form.apellido_dos.valor    = data.apellidodos;
                    this.form.email.valor           = data.email;
                }
                this.form.mostrar   = true;
            },
            guardarDatosEmpleado(){
                const validEmail =  /^\w+([.-_+]?\w+)*@\w+([.-]?\w+)*(\.\w{2,10})+$/;
                if (this.form.rut.valor == "" || this.form.nombres.valor == "" || this.form.apellido_uno.valor == "" || 
                    this.form.apellido_dos.valor == "" || this.form.email.valor == ""){
                    this.$swal("Tiene campos pendiente que completar", "Validación encontrada", "warning");
                } else if (this.form.rut.valor.length < 3 || !this.validarRut(this.form.rut.valor.split("-")[0], this.form.rut.valor.split("-")[1]) ) {
                    this.$swal("RUT ingresado no está correcto", "Validación encontrada", "warning");
                } else if (!validEmail.test(this.form.email.valor)) {
                    this.$swal("Formato Email no está correcto(XXXXX@XXXX.XX)", "Validación encontrada", "warning");
                } else {
                    const swal = this.$swal({
                        text                : '¿Estas seguro de guardar la información ingresada?',
                        icon                : 'warning',
                        showCancelButton    : true,
                        confirmButtonText   : 'Si, guardar',
                        cancelButtonText    : 'No, cancelar',
                        confirmButtonClass  : 'btn btn-success mt-2',
                        cancelButtonClass   : 'btn btn-danger ms-2 mt-2'
                    }).then(result => {
                        if (result.hasOwnProperty('value') && result.value) {
                            var bodyFormData = new FormData();

                            bodyFormData.set('id'           , this.form.id);
                            bodyFormData.set('empresa_id'   , this.form.empresa_id);
                            bodyFormData.set('rut'          , this.form.rut.valor.split("-")[0]);
                            bodyFormData.set('dv'           , this.form.rut.valor.split("-")[1]);
                            bodyFormData.set('nombres'      , this.form.nombres.valor);
                            bodyFormData.set('apellido_uno' , this.form.apellido_uno.valor);
                            bodyFormData.set('apellido_dos' , this.form.apellido_dos.valor);
                            bodyFormData.set('email'        , this.form.email.valor);

                            this.$swal({
                                title: 'Guardando información ingresada...Por favor espere',
                                text: '...',
                                icon: 'info',
                                showConfirmButton: false,
                                allowOutsideClick: false,
                                allowEscapeKey: false
                            })
                            return empleadoServices.guardarDatosEmpleado(bodyFormData);
                        } else {
                            return false;
                        }
                    }).then(results => {
                        return results
                    }).then(res => {
                        if (res) {
                            this.$swal({
                                title               : res.data.titulo,
                                text                : res.data.mensaje,
                                icon                : res.data.icono,
                                confirmButtonColor  : '#556ee6',
                                confirmButtonText   : 'Cerrar alerta'
                            }).then(result => {
                                console.log(result);
                                if (res.data.code == 1) {
                                    this.cerrarModalEmpleado()
                                    this.obtenerListadoEmpleadoPorEmpresaId()
                                }
                            });
                        }
                    })
                    .catch(err => {
                        console.log(err)
                        if (err) {
                            this.$swal('Ocurrió un problema al llamar a la api', 'Favor ver detalle por consola', 'error')
                        } else {
                            swal.close()
                        }
                    });
                }
            },
            cerrarModalEmpleado(){
                this.form.mostrar = false;
            },
            validaCaracteresRut($event) {
                //1, 2, 3, 4, 5, 6, 7, 8, 9, 0, K, k
                if (($event.keyCode >= 48 && $event.keyCode <= 57) || $event.keyCode == 107 || $event.keyCode == 75) {
                    return true;
                } else {
                    return $event.preventDefault();
                }
            },
            validaFormatoRut($event) {
                console.log($event);
                let rut_ingresado   = this.form.rut.valor.trim().replace("-", "");
                let largo           = rut_ingresado.length;
                if(largo > 1) {
                    let rut = rut_ingresado.substring(0, largo - 1);
                    let dv  = rut_ingresado.substring(largo - 1, largo);
                    rut_ingresado = rut + "-" + dv;
                }
                this.form.rut.valor = rut_ingresado;
            },
            validarRut(rut, dig) {
                //RESULVARIABLE TADO
                let exito = false;
                //OBTENIENDO TAMAÑO DEL RUT
                let largo = rut.length;
                //CREANDO TAMAÑO DE ALMACENAMIENTO RUT
                let num = [];
                //ALMACENANDO RUT DIGITO POR DIGITO
                for (let i = 0; i < largo; i++) {
                    num[i] = parseInt(rut.charAt(i) + "");
                }
                //MULTIPLICANDO DE DERECHA A IZQUIERDA LOS NUMERO DE 2 AL 7
                let variable = 2;
                for (let i = largo - 1; i >= 0; i--) {
                    num[i] = num[i] * variable;
                    variable++;
                    if (variable == 8) {
                        variable = 2;
                    }
                }
                //SUMANDO TODA LA CADENA RESTANTE (MULTIPLICADA)
                let suma = 0;
                for (let i = 0; i < largo; i++) {
                    suma += num[i];
                }
                //OBTENIENDO EL MODULO DE LA SUMA
                let resto = suma % 11;
                let dv = 11 - resto;
                //OBTENIENDO DIGITO VERIFICADOR
                if (dv == "10" ) {
                    dv = "k";
                } else if (dv == "11") {
                    dv = "0";
                }
                //COMARANDO SI EL RUT INTRODUCIDO ES VERDADERO O NO
                if (dv == dig.toLowerCase()) {
                    exito = true;
                }
                //RETORNAMOS EL ESTADO DE LA COMPROBACION FINAL
                return exito;
            },
            confirmarEliminarEmpleado(){
                this.$swal('Estará listo para el próximo SPRINTS', 'Mensaje informativo', 'info');
            }
        }
    })
</script>
<style scoped lang="css">
    @import 'empleado.css';
</style>

