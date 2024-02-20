import {createApp} from 'vue'
import {install} from '@icon-park/vue-next/es/all';
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import App from './App.vue'
import '@icon-park/vue-next/styles/index.css';

const app = createApp(App)
app.use(ElementPlus).use(router)
app.provide('$axios',axios)
app.mount('#app')
install(app)
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import router from "./router/index.js";
import axios from './api.js'
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
}

