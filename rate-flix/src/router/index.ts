import { createRouter, createWebHistory } from '@ionic/vue-router';
import { RouteRecordRaw } from 'vue-router';
import Navigation from '../components/BottomNavigation.vue';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    redirect: '/home',
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
  },
  {
    path: '/team',
    component: () => import ('@/views/TeamPage.vue')
  },
  {
    path: '/',
    component: Navigation,
    children: [
      {
        path: '',
        redirect: '/home',
      },
      {
        path: 'home',
        component: () => import('../views/HomePage.vue'),
      },
      {
        path: 'profile',
        component: () => import('../views/ProfilePage.vue'),
      },
      {
        path: 'library',
        component: () => import('../views/LibraryPage.vue'),
      },
      {
        path: 'search',
        component: () => import('../views/SearchPage.vue'),
      },
      {
        path: 'setting',
        component: () => import('../views/SettingPage.vue'),
      },
    ],
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
