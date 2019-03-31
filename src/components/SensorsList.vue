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
            <h4>Список датчиков</h4><br />
            <!-- <div v-for="sensor in sensors_data" class="alert alert-primary">
                <h4>Датчик {{sensor.name}}</h4>
                <p>Температура: <b>{{sensor.temp}}</b> Направление ветра в градусах: <b>{{sensor.wind_direction}}</b>
                    Скорость ветра: <b>{{sensor.wind_speed}}</b> | Влажность: <b>{{sensor.humidity}}</b>
                </p>
                <p><span>Координаты датчика {{sensor.sensor_coords_lat}} {{sensor.sensor_coords_lng}}</span></p>

                    <div class="btn btn-info ml-2" href="#">Сообщить в МЧС</div>
                    <div class="btn btn-primary ml-2" href="#">Связаться с лесничим</div>
                    <div class="btn btn-light ml-2" href="#">Запросить данные снова</div>
            </div> -->
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
    import axios from 'axios'

    export default {
        name: "SensorsList",
        components: {
            'f': F,
            'nav-bar': NavBar,
            'side-menu': SideMenu
        },
        data() {
            return {
              sensors_data: null
            };
          },
        mounted() {
          axios
            .get('http://localhost:8000/api/rest/sensor/0/')
            .then(response => (this.sensors_data = response.data))
        },
        methods: {

        }
    }

</script>

<style scoped>

</style>