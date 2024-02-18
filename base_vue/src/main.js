import {createApp} from 'vue'
import ElementPlus from 'element-plus'
import 'element-plus/dist/index.css'
import App from './App.vue'

const app = createApp(App)
app.use(ElementPlus).use(router)
app.mount('#app')
import * as ElementPlusIconsVue from '@element-plus/icons-vue'
import router from "./router/index.js";

for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
}

