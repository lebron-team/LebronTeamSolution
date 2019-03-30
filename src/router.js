import Vue from 'vue'
import Router from 'vue-router'
import VueDemo from '@/components/VueDemo'
import Messages from '@/components/Messages'
import Bootstrap from '@/components/Bootstrap'
import ControlPanel from '@/components/ControlPanel'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: VueDemo
    },
    {
      path: '/messages',
      name: 'messages',
      component: Messages
    },
    {
      path: '/bootstrap',
      name: 'bootstrap',
      component: Bootstrap
    },
    {
      path: '/panel',
      name: 'control_panel',
      component: ControlPanel
    }
  ]
})
