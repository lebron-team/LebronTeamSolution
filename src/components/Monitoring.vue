<template>
  <div id="app">
    <nav-bar></nav-bar>

  <div class="container-fluid">
    <div class="row">

      <div class="col-2 ml-3">
        <side-menu></side-menu>
      </div>

      <div class="col-9 main-window-element box-shadow-line"><br />
        <h4>Mониторинг ситуации на территории</h4><br />
        <div id="paper"></div>
      </div>

    </div>
  </div>
  <f></f>
</div>
</template>

<script>
  import SideMenu from "@/components/SideMenu"
  import NavBar from '@/components/NavBar'
  import F from '@/components/F'

  export default {
    name: "ControlPanel",
    components: {
      'side-menu': SideMenu,
      'nav-bar': NavBar,
      'f': F
    }
  }
</script>

<style scoped>

</style>