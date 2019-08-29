import Vue from 'vue'
import Router from 'vue-router'
import Login from '@/components/login/login.vue'
import Index from '@/components/index/index'
import Home from '@/components/home/home.vue'
import Product from '@/components/product/product.vue'

Vue.use(Router);

export default new Router({
  routes: [
    {
      name: 'login',
      path: '/login',
      component: Login
    },
    {
      path: 'home',
      component: Home,
      children: [
        {
          name: 'index',
          path: '/home/index',
          component: Index
        },
        {
          name: 'product',
          path: '/home/product',
          component: Product
        }
      ]
    }
  ]
})
