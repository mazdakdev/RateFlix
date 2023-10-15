import { createRouter, createWebHistory } from '@ionic/vue-router';
import { RouteRecordRaw } from 'vue-router';

const routes: Array<RouteRecordRaw> = [
  {
    path: '',
    redirect: '/start'
  },

  {
    path: '/about',
    component: () => import("@/views/AboutPage.vue")
  },
  {
    path: '/start',
    component: () => import ('@/views/StartPage.vue')
  },
  {
    path: '/results',
    component: () => import ('@/views/ResultPage.vue')
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
