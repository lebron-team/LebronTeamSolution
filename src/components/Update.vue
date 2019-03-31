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
              <h4>Ожидающие обновления системы</h4>
            <p class="alert alert-primary">На данный момент нет обновлений</p>
        </div><br />

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
        name: "Update",
        components: {
            'nav-bar': NavBar,
            'side-menu': SideMenu,
            'f': F
        }
    }
</script>

<style scoped>

</style>