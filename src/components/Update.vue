<template>
    <div id="app">
    <nav-bar></nav-bar>

    <div class="container-fluid">
      <div class="row">

        <div class="col-2">
          <side-menu></side-menu>
        </div>
        <div class="col-10 main-window-element box-shadow-line">
              <h4>Ожидающие обновления системы</h4>
            <p class="alert alert-primary">На данный момент нет обновлений</p>
        </div>

      </div>
    </div>

  </div>
</template>

<script>
  import SideMenu from "@/components/SideMenu"
  import NavBar from '@/components/NavBar'

    export default {
        name: "Update",
        components: {
            'nav-bar': NavBar,
            'side-menu': SideMenu
        }
    }
</script>

<style scoped>

</style>