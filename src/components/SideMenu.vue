<template>
<div class="container-fluid side-element box-shadow-line">
  <ul>
    <li class="#"><router-link :to="{ name: 'home' }">Главная</router-link></li>
    <li><router-link :to="{ name: 'control_panel' }">Панель управления</router-link></li>
    <li><router-link :to="{ name: 'messages' }">Территории</router-link></li>
    <li><router-link :to="{ name: 'bootstrap' }">Список датчиков</router-link></li>
  </ul>
</div>
</template>

<script>
    export default {
        name: "SideMenu"
    }
</script>

<style scoped>
  .side-element {
    margin: 1rem 0 1rem 0;
    border-radius: 0.3rem;
    padding: 0.5rem;
    background: white;
  }
</style>