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
            <h4>Области и регионы</h4><br />
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
    export default {
        name: "Territories",
        components: {
            'side-menu': SideMenu,
            'nav-bar': NavBar,
            'f': F
        }
    }
</script>

<style scoped>

</style>