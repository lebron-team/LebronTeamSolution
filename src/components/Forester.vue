<template>
  <div id="app">
    <nav-bar></nav-bar>

  <div class="container-fluid">
    <div class="row">

      <div class="col-2">
        <side-menu></side-menu>
      </div>

      <div class="col-10 main-window-element box-shadow-line">

        <div class="alert alert-primary">
          Лесничий <strong>Алексеев Иван Васильевич</strong> ––
          Рязанская область, лесхозяйство №153
          <span>Тел. +733391020</span>
        </div>
        <div class="alert alert-primary">
          Лесничий <strong>Алексеев Иван Васильевич</strong> ––
          Рязанская область, лесхозяйство №153
          <span>Тел. +733391020</span>
        </div>
        <div class="alert alert-primary">
          Лесничий <strong>Алексеев Иван Васильевич</strong> ––
          Рязанская область, лесхозяйство №153
          <span>Тел. +733391020</span>
        </div>
        <div class="alert alert-primary">
          Лесничий <strong>Алексеев Иван Васильевич</strong> ––
          Рязанская область, лесхозяйство №153
          <span>Тел. +733391020</span>
        </div>
        <div class="alert alert-primary">
          Лесничий <strong>Алексеев Иван Васильевич</strong> ––
          Рязанская область, лесхозяйство №153
          <span>Тел. +733391020</span>
        </div>

      </div>

    </div>
  </div>
</div>
</template>

<script>
  import SideMenu from "@/components/SideMenu"
  import NavBar from '@/components/NavBar'
    export default {
        name: "Forester",
        components: {
            'nav-bar': NavBar,
            'side-menu': SideMenu

        }
    }
</script>

<style scoped>

</style>