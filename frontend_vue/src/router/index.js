import { createRouter, createWebHistory }   from 'vue-router';
import homePage                             from '@/components/home/home.vue'
import empresaPage                          from '@/components/empresa/empresa.vue'
import empleadoPage                         from '@/components/empleado/empleado.vue'

const routes = [
    {
        path      : '/',
        redirect  : '/home'
    },
    {
        path      : '/home',
        name      : 'home',
        component : homePage
       
    },
    {
        path      : '/mis-empresas',
        name      : 'mis-empresas',
        component : empresaPage
       
    },
    {
        path      : '/empleados',
        name      : 'empleados',
        component : empleadoPage
       
    },
]

const router = createRouter({
    history: createWebHistory(process.env.BASE_URL),
    routes
  })
  
  export default router
  