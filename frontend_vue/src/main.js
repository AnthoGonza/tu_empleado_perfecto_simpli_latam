import { createApp }        from 'vue';
import App                  from './App.vue';
import router               from './router';
import VueSweetalert2       from 'vue-sweetalert2';
import { FontAwesomeIcon }  from '@fortawesome/vue-fontawesome';
import { library }          from "@fortawesome/fontawesome-svg-core";
import { faUsers }          from "@fortawesome/free-solid-svg-icons";
library.add(faUsers)

import 'sweetalert2/dist/sweetalert2.min.css';
  
const app = createApp(App)
    .use(router)
    .use(VueSweetalert2)
    .component('font-awesome-icon', FontAwesomeIcon)


router.isReady().then(() => {
    app.mount('#app');
});

//createApp(App).mount('#app')
