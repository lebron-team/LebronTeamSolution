import Vue from 'vue'
import Router from 'vue-router'
import VueDemo from '@/components/VueDemo'
import Messages from '@/components/Messages'
import Bootstrap from '@/components/Bootstrap'
import ControlPanel from '@/components/ControlPanel'
import Forester from '@/components/Forester'
import Emergency from '@/components/Emergency.vue'
import Update from '@/components/Update.vue'
import Monitoring from '@/components/Monitoring.vue'

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
    },
    {
      path: '/forester',
      name: 'forester',
      component: Forester
    },
    {
      path: '/emergency',
      name: 'emergency',
      component: Emergency
    },
    {
      path: '/update',
      name: 'update',
      component: Update
    },
    {
      path: '/monitoring',
      name: 'monitoring',
      component: Monitoring
    }
  ]
})
