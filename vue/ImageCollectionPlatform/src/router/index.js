import {createRouter, createWebHistory} from "vue-router";


const routes = [
    {
        path: '/',
        name: "index",
        component: () => import('@/views/ImageCollectionPlatform/HomePage.vue')
    },
    {
        path: '/ImageCollectionPlatform/HomePage',
        name: "ImageCollectionPlatformHomePage",
        component: () => import('@/views/ImageCollectionPlatform/HomePage.vue')
    }, {
        path: '/ImageCollectionPlatform/SearchResultsPage',
        name: "ImageCollectionPlatformSearchResultsPage",
        component: () => import('@/views/ImageCollectionPlatform/SearchResultsPage.vue')
    }, {
        path: '/ImageCollectionPlatform/CollectionDetailsPage',
        name: "ImageCollectionPlatformCollectionDetailsPage",
        component: () => import('@/views/ImageCollectionPlatform/CollectionDetailsPage.vue')
    }, {
        path: '/ImageCollectionPlatform/UploadPage',
        name: "ImageCollectionPlatformUploadPage",
        component: () => import('@/views/ImageCollectionPlatform/UploadPage.vue')
    }, {
        path: '/ImageCollectionPlatform/CategoryMaintenancePage',
        name: "ImageCollectionPlatformCategoryMaintenancePage",
        component: () => import('@/views/ImageCollectionPlatform/CategoryMaintenancePage.vue')
    }, {
        path: '/ImageCollectionPlatform/ArtistMaintenancePage',
        name: "ImageCollectionPlatformArtistMaintenancePage",
        component: () => import('@/views/ImageCollectionPlatform/ArtistMaintenancePage.vue')
    }, {
        path: '/ImageCollectionPlatform/UserLoginPage',
        name: "ImageCollectionPlatformUserLoginPage",
        component: () => import('@/views/ImageCollectionPlatform/UserLoginPage.vue')
    }, {
        path: '/ImageCollectionPlatform/UserRegistrationPage',
        name: "ImageCollectionPlatformUserRegistrationPage",
        component: () => import('@/views/ImageCollectionPlatform/UserRegistrationPage.vue')
    }
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