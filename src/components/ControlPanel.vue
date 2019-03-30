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


        <!-- Buttons-->
        <h2>Buttons</h2>
        <div style="padding: 1rem;">
              <div v-for="type in ['', 'outline']" :key="type">
                  <span v-for="brand in ['primary', 'secondary', 'success', 'info', 'warning', 'danger']" :key="brand">
                      <button role="button" class="btn" :class="'btn-' + (type.length ? (type + '-') : '') + brand" style="margin-bottom: 1rem; margin-right: 1rem;">
                          {{brand}} {{type}}
                      </button>
                  </span>
              </div>
        </div>
        <!-- Progress-->
        <h2>Progress</h2>
        <div style="padding: 1rem;">
          <div v-for="brand in ['success', 'info', 'warning', 'danger']" :key="brand" class="progress" style='margin-bottom: 1rem;'>
              <div class="progress-bar" :class="'bg-' + brand" style="width: 25%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
          </div>
        </div>
        <!-- Notice-->
        <h2>Modal</h2>
        <div style="padding: 1rem;">
          <div class="modal-dialog" role="document">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title">Modal title</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                  <span aria-hidden="true">&times;</span>
                </button>
              </div>
              <div class="modal-body">
                <p>Modal body text goes here.</p>
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-primary">Save changes</button>
                <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
              </div>
            </div>
          </div>
        </div>
        <!-- Spacing utilities-->
        <h2>Spacing utilities</h2>
        <test></test>
        <div style="padding: 1rem;">
          <div v-for="brand in ['success', 'info', 'warning', 'danger']" :key="brand" class="progress" style='margin-bottom: 1rem;'>
              <div class="progress-bar" :class="'bg-' + brand" style="width: 25%" aria-valuenow="25" aria-valuemin="0" aria-valuemax="100"></div>
          </div>
        </div>
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
    padding: 2rem 0.5rem 0.5rem 0.5rem;
    border-radius: 0.3rem;
  }

</style>