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
        <h4>Перечень лесничих, ответственных за леные хозяйства</h4><br />

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
  <f></f>
</div>
</template>

<script>
  import SideMenu from "@/components/SideMenu"
  import NavBar from '@/components/NavBar'
  import F from '@/components/F'
    export default {
        name: "Forester",
        components: {
            'nav-bar': NavBar,
            'side-menu': SideMenu,
            'f': F

        }
    }
</script>

<style scoped>

</style>