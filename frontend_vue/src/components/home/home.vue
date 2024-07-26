<template>
    <app-header />
    <main class="px-1 mt-5 pt-5">
        <h2>Bienvenid@ A <b>Tu Empleado  Perfecto</b></h2>
    </main>
</template>

<script>
    import header               from '@/components/layout/header.vue'
    import { defineComponent }  from 'vue';

    window.onbeforeunload = function () { window.history.forward(1) }

    export default defineComponent({
        name : 'home',
        components: {
            "app-header" : header
        },
        data() {
            return {
            }
        },
        mounted() {
        },
        methods: {
            init(){
                
            }
        }
    })
</script>
<style scoped lang="css">
    @import 'home.css';
</style>

