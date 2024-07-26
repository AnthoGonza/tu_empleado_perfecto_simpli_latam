<template>
    <div class="row mb-4">
        <div class="col-12">
            <nav class="navbar navbar-expand-lg navbar-light bg-light px-4">
                <img id="logo" :src="require('@/assets/logo_tu_empleado_perfecto.png')">
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                </button>
            
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                    <ul class="navbar-nav mr-auto px-3">
                        <li class="nav-item active">
                            <a class="nav-link" href="mis-empresas">
                                <i class="fa fa-building" aria-hidden="true"></i>
                                Mis empresas
                            </a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="empleados">
                                <i class="fa fa-users" aria-hidden="true"></i>
                                Empleados
                            </a>
                        </li>
                    </ul>
                </div>
            </nav>
        </div>
    </div>
</template>

<script>
    import { defineComponent }  from 'vue';

    window.onbeforeunload = function () { window.history.forward(1) }

    export default defineComponent({
        data() {
            return {
            }
        },
        mounted() {
        },
        methods: {
        }
    })
</script>

<style scoped lang="css">
    @import 'header.css';
</style>

