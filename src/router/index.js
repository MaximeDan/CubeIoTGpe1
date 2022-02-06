import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import tables from "@/views/Tables";

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/table',
    name: 'table',
    props: true,
    component: tables
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
