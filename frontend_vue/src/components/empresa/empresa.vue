<template>
    <app-header />
    <main class="px-1">
        <div class="card">
            <div class="card-header">
                <div class="row py-2"> 
                    <div class="col-xl-6 col-md-6 col-sm-6" align="left">
                        <label class="mb-0 mt-1">Listado empresas</label>                    
                    </div>
                    <div class="col-xl-6 col-md-6 col-sm-6" align="right">
                        <button @click="abrirModalEmpresa(null)" class="btn btn-primary btn-sm"><i class="fa fa-plus" aria-hidden="true"></i> Nueva empresa</button>
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
                                <th scope="col">Nombre</th>
                                <th scope="col">Dirección</th>
                                <th scope="col">Telefono</th>
                                <th class="col-2">Acciones</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr v-if="this.tabla_empresa.items.length > 0" v-for="item in this.tabla_empresa.items" :key="item.id" >
                                    <td scope="row">{{item.id}}</td>
                                    <td>{{item.rut + "-" + item.dv}}</td>
                                    <td>{{item.nombre}}</td>
                                    <td>{{item.direccion}}</td>
                                    <td>{{item.telefono}}</td>
                                    <td>
                                        <button class="btn btn-primary btn-sm" @click="abrirModalEmpresa(item)"> <i class="fa fa-pencil"></i> Editar</button>
                                        <button class="btn btn-danger btn-sm ml-1" @click="confirmarEliminarEmpresa(item.id)"> <i class="fa fa-trash-o"></i> Eliminar</button>
                                    </td>
                                </tr>
                                <tr v-else>
                                    <td colspan="6" align="center">No hay datos para mostrar</td>
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
        tabindex="-1" role="dialog" id="modalVisualizarEmpresa">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title"><i class="fa fa-building" aria-hidden="true" data-v-30de9f9c=""></i>Datos empresa</h5>
            </div>
            <div class="modal-body">
                <div class="row">
                    <div class="col-12 mb-4">
                        <div class="form-group">
                            <label class="titulo" align="left">Rut*</label>
                            <input  @keypress="validaCaracteresRut($event)" @keyup="validaFormatoRut($event)" type="text" class="form-control sm" id="validationCustom03" v-model="form.rut.valor"  required>
                        </div>
                    </div>
                    <div class="col-12 mb-4">
                        <div class="form-group">
                            <label class="titulo" align="left">Nombre*</label>
                            <input type="text" class="form-control sm" id="validationCustom03" v-model="form.nombre.valor" required>
                        </div>
                    </div>
                    <div class="col-12 mb-4">
                        <div class="form-group">
                            <label class="titulo" align="left">Dirección*</label>
                            <input type="text" class="form-control sm" id="validationCustom03" v-model="form.direccion.valor" required>
                        </div>
                    </div>
                    <div class="col-12 mb-4">
                        <div class="form-group">
                            <label class="titulo" align="left">Telefono*</label>
                            <input type="text" class="form-control sm" id="validationCustom03" v-model="form.telefono.valor" required>
                        </div>
                    </div>
                </div>
            </div>
            <div class="modal-footer">
                <button type="button" class="btn btn-primary" @click="guardarDatosEmpresa()"><i class="fa fa-floppy-o" aria-hidden="true"></i> Guardar</button>
                <button type="button" class="btn btn-secondary"  @click="cerrarModalEmpresa()"><i class="fa fa-times" aria-hidden="true"></i> Cerrar</button>
            </div>
            </div>
        </div>
    </div>
</template>

<script>
    import header               from '@/components/layout/header.vue'
    import empresaServices      from '@/services/empresaServices.js'
    import { defineComponent }  from 'vue';

    window.onbeforeunload = function () { window.history.forward(1) }

    export default defineComponent({
        name : 'empresa',
        components: {
            "app-header" : header
        },
        data() {
            return {
                form: {
                    id: 0,
                    rut :  {
                        
                        valor   : "",
                        estado  : ""
                    },
                    nombre       :  {
                        valor   : "",
                        estado  : ""
                    },
                    direccion   :  {
                        valor   : "",
                        estado  :    ""
                    },
                    telefono   :  {
                        valor   : "",
                        estado  :    ""
                    },
                    mostrar : false
                },
                tabla_empresa : {
                    loading         : true,
                    filter          : null,
                    fields        : {
                        id          : { label: 'ID'},
                        rut         : { label: 'RUT'},
                        direccion   : { label: 'Dirección'},
                        telefono    : { label: 'Telefono'},
                        accion      : { label: 'Acciones'}
                    },
                    items         : [],
                }
            }
        },
        mounted() {
            this.init();
        },
        methods: {
            init(){
                console.log("process.env.DOMAIN_ENV: " + process.env.DOMAIN_ENV);
                this.obtenerListadoEmpresa();
                //this.imagen_logo = import.meta.env.VITE_DOMAIN_ENV + '/public/assets/images/logo_3.png';
                
            },
            obtenerListadoEmpresa(){
                this.tabla_empresa.loading  = true;
                this.tabla_empresa.items    = [];
                const swal = this.$swal({
                    title               : 'Obteniendo listado empresa...Por favor espere',
                    text                : '...',
                    icon                : 'info',
                    showConfirmButton   : false,
                    allowOutsideClick   : false,
                    allowEscapeKey  : false
                });
                empresaServices.obtenerListadoEmpresa().then(res => {
                    return res.data
                }).then(data=> {
                    console.log(data);
                    if(data.code == 1){
                        data.data.forEach(dato => {
                            this.tabla_empresa.items.push(dato);
                        });
                    }
                    this.tabla_empresa.loading  = false;
                    
                    swal.close()
                }).catch((err) => {
                    console.log(err);
                    this.$swal('Ocurrió un problema al llamar a la api', 'Favor ver detalle por consola', 'error')
                    this.tabla_empresa.loading = false;
                    swal.close()
                });
            },
            abrirModalEmpresa(data){
                console.log(data);
                if (data == null) {
                    this.form.id                = 0;
                    this.form.rut.valor         = "";
                    this.form.nombre.valor      = "";
                    this.form.direccion.valor   = "";
                    this.form.telefono.valor    = "";
                } else {
                    this.form.id                = data.id;
                    this.form.rut.valor         = data.rut + "-" + data.dv;
                    this.form.nombre.valor      = data.nombre;
                    this.form.direccion.valor   = data.direccion;
                    this.form.telefono.valor    = data.telefono;
                }
                this.form.mostrar   = true;
            },
            guardarDatosEmpresa(){
                if (this.form.rut.valor == "" || this.form.nombre.valor == "" ||this.form.direccion.valor == "" || this.form.telefono.valor == ""){
                    this.$swal("Tiene campos pendiente que completar", "Validación encontrada", "warning");
                } else if (this.form.rut.valor.length < 3 || !this.validarRut(this.form.rut.valor.split("-")[0], this.form.rut.valor.split("-")[1]) ) {
                    this.$swal("RUT ingresado no está correcto", "Validación encontrada", "warning");
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
                            bodyFormData.set('rut'          , this.form.rut.valor.split("-")[0]);
                            bodyFormData.set('dv'           , this.form.rut.valor.split("-")[1]);
                            bodyFormData.set('nombre'       , this.form.nombre.valor);
                            bodyFormData.set('direccion'    , this.form.direccion.valor);
                            bodyFormData.set('telefono'     , this.form.telefono.valor);

                            this.$swal({
                                title: 'Guardando información ingresada...Por favor espere',
                                text: '...',
                                icon: 'info',
                                showConfirmButton: false,
                                allowOutsideClick: false,
                                allowEscapeKey: false
                            })
                            return empresaServices.guardarDatosEmpresa(bodyFormData);
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
                                    this.cerrarModalEmpresa()
                                    this.obtenerListadoEmpresa()
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
            cerrarModalEmpresa(){
                this.form.mostrar = false;
            },
            validaCaracteresRut($event) {
                //1, 2, 3, 4, 5, 6, 7, 8, 9, 0, K, k
                if (($event.keyCode >= 48 && $event.keyCode <= 57) || $event.keyCode == 107 || $event.keyCode == 75) {
                    return true
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
            confirmarEliminarEmpresa(){
                this.$swal('Estará listo para el próximo SPRINTS', 'Mensaje informativo', 'info');
            }
        }
    })
</script>
<style scoped lang="css">
    @import 'empresa.css';
</style>

