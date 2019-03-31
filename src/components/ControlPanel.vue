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

              <div id="layer1">
                <russian-map></russian-map>
              </div>
              <div id="layer2">
                <svg height="150%" width="100%" class="blinking">
                  <circle cx="63%" cy="44%" r="5" fill="red"></circle>
                  <circle cx="30%" cy="40%" r="5" fill="red"></circle>
                  <circle cx="23%" cy="15%" r="5" fill="red"></circle>
                  <circle cx="24%" cy="17%" r="5" fill="red"></circle>
                  <circle cx="52%" cy="79%" r="5" fill="red"></circle>
                  <circle cx="19%" cy="90%" r="5" fill="red"></circle>
                  <circle cx="60%" cy="47%" r="5" fill="red"></circle>
                  <circle cx="49%" cy="49%" r="5" fill="red"></circle>
                </svg>
              </div>

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
    components: {
      'test': Test,
      'side-menu': SideMenu,
      'russian-map': RussianMap,
      'nav-bar': NavBar,
      'f': F
    },
    data() {
            return {
              sensors_data: null
            };
          },
    mounted() {
      axios
        .get('http://localhost:8000/api/rest/region/0/')
        .then(response => (this.sensors_data = response.data))
    },
    methods: {

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
  top: -30%;
 }

 #layer1 { z-index: 1; }
 #layer2 { z-index: 2; }

  .blinking {
    -webkit-animation: 1.5s blink ease infinite;
    -moz-animation: 1.5s blink ease infinite;
    -ms-animation: 1.5s blink ease infinite;
    -o-animation: 1.5s blink ease infinite;
    animation: 1.5s blink ease infinite;
  }

  @keyframes "blink" {
    from, to {
      opacity: 0;
    }
      50% {
        opacity: 1;
      }
    }
    @-moz-keyframes blink {
      from, to {
        opacity: 0;
      }
      50% {
        opacity: 1;
      }
    }
    @-webkit-keyframes "blink" {
      from, to {
        opacity: 0;
      }
      50% {
        opacity: 1;
      }
    }
    @-ms-keyframes "blink" {
      from, to {
        opacity: 0;
      }
      50% {
        opacity: 1;
      }
    }
    @-o-keyframes "blink" {
      from, to {
        opacity: 0;
      }
      50% {
        opacity: 1;
      }
    }



</style>