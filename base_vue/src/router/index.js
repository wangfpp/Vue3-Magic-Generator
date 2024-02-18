import {createRouter, createWebHistory} from "vue-router";


const routes = [
    ${router}
]

const router = createRouter({
    history: createWebHistory(),
    routes,
    scrollBehavior: () => ({top: 0, left: 0}),
    linkActiveClass: 'active',
    linkExactActiveClass: 'exact-active',
    parseQuery: null,
    stringifyQuery: null,
    fallback: true
})

export default router