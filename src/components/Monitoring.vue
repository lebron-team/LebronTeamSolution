<template>
  <div id="app">
    <nav-bar></nav-bar>

  <div class="container-fluid">
    <div class="page-container">
    <div class="row">

      <div class="col-2 ml-3">
        <side-menu></side-menu>
      </div>

      <div class="col-9 main-window-element box-shadow-line"><br />
        <h4>Mониторинг ситуации на территории</h4><br />
        <div class="map-container">
          <div id="paper"></div>
        </div>
      </div>

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
  import createMap from '@/raphael/index.js'

  export default {
    name: "ControlPanel",
    components: {
      'side-menu': SideMenu,
      'nav-bar': NavBar,
      'f': F
    },
    mounted: createMap
  }
</script>

<style scoped>
  .map-container {
    display: flex;
    justify-content: center;
    align-items: center;
  }
  #paper {
    width: 90%;
    height: 50vh;
    background: url('./../assets/back.png') no-repeat center;
  }
</style>