<template class="bg-light-gray">
<div id="app">

  <nav-bar></nav-bar>

  <div class="container-fluid">
    <div class="page-container">
    <div class="row">

      <div class="col-2 ml-3">
        <side-menu></side-menu>
      </div>

        <div class="col-9 main-window-element box-shadow-line">
          <div class="container-fluid"><br />
            <h4>Система мониторинга лесного массива Российской Федерации</h4>
              <div class="row-8">
                <span class="text-muted">Доступны обновления с датчиков: 24 </span>
                <span class="text-muted">Последний запуск мониторинга: 1 час назад</span>
              </div><br />
          </div>

          <russian-map></russian-map>


        </div>
      </div>
    </div>
    <div class="row">
      <f></f>
    </div>
  </div>

</div>
</template>

<script>
  import Test from '@/components/Test'
  import SideMenu from "@/components/SideMenu"
  import RussianMap from '@/components/RussianMap'
  import NavBar from '@/components/NavBar'
  import F from '@/components/F'

  export default {
    name: "ControlPanel",
      props: ['sensor_id'],
      data () {
        return {
          sensor_id: {},
        }
      },
    components: {
      'test': Test,
      'side-menu': SideMenu,
      'russian-map': RussianMap,
      'nav-bar': NavBar,
      'f': F
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
  .page-container {
    position: relative;
    min-height: 100%;
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
    margin: 1rem 0 1rem 1rem;
    padding: 1rem;
    border-radius: 0.3rem;
  }
  #layer1, #layer2 {
    position: relative;
   }

  #layer2 {
    top: 50%;
   }
   #layer1 { z-index: 2; }
   #layer2 { z-index: 1; }



</style>