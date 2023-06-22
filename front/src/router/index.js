import { createRouter, createWebHistory } from 'vue-router'
import TableView from '../views/TableView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Tableview
    },
  ]
})

export default router
