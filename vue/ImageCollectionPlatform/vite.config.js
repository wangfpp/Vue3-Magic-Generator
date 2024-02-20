import {defineConfig} from 'vite'
import vue from '@vitejs/plugin-vue'
import {resolve} from 'path'


export default defineConfig({
    devServer: {
        proxy: {
            '/api': {
                target: 'http://localhost:5000', // 后端服务的地址
                ws: true, // 是否启用websockets
                changeOrigin: true, // 将主机头的来源更改为目标URL
                pathRewrite: {'^/api': ''}, // 重写请求路径
            },
        },
    },
    resolve: {
        alias: {
            '@': resolve(__dirname, 'src')
        }
    },
    plugins: [
        vue(),
         [
            "import",
            {
                "libraryName": "@icon-park/vue-next",
                "libraryDirectory": "es/icons",
                "camel2DashComponentName": false
            }
        ]
    ],
    "compilerOptions": {
        "types": ["element-plus/global"]
    }
})
