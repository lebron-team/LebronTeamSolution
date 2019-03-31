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
import SensorsList from '@/components/SensorsList.vue'
import Territories from '@/components/Territories'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: ControlPanel
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
    },
    {
      path: '/sensors-list',
      name: 'sensors-list',
      component: SensorsList
    },
    {
      path: '/territories',
      name: 'territories',
      component: Territories
    }
  ]
})
