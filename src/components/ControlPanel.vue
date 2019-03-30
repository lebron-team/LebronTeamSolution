<template class="bg-light-gray">
<div id="app">

  <nav-bar></nav-bar>

  <div class="container-fluid">
    <div class="row">

      <div class="col-2">
        <side-menu></side-menu>
      </div>

      <div class="col-10 main-window-element box-shadow-line">
        <h4>Система мониторинга лесного массива Российской Федерации</h4>
          <div class="row-8">
            <span class="text-muted">Доступны обновления с датчиков: 24 </span>
            <span class="text-muted">Последний запуск мониторинга: 1 час назад</span>
          </div>

        <russian-map></russian-map>

      </div>
    </div>
  </div>

</div>
</template>

<script>
  import Test from '@/components/Test'
  import SideMenu from "@/components/SideMenu"
  import RussianMap from '@/components/RussianMap'
  import NavBar from '@/components/NavBar'

  export default {
    name: "ControlPanel",
    components: {
      'test': Test,
      'side-menu': SideMenu,
      'russian-map': RussianMap,
      'nav-bar': NavBar
    }
  }
</script>

<style>
  body {
  }
  ul {
    list-style: none;
  }
  li {
    padding: 0.75rem 0.5rem 0.75rem 0 ;
    text-align: left;
  }
  .bg-light-gray {
    background: #f8f9fa;
  }
  .blue-gradient {
    background: #007bff;
    background: linear-gradient(to right, #0062E6, #33AEFF);
  }
  .box-shadow-line {
    box-shadow: 0 0.5rem 1rem 0 rgba(0, 0, 0, 0.1);
    border: 1px solid #dee2e6;
  }

  .main-window-element {
    margin: 1rem 0 1rem 0;
    padding: 1rem 0.5rem 0.5rem 0.5rem;
    border-radius: 0.3rem;
  }

</style>