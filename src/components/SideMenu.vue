<template>
<div class="container-fluid side-element box-shadow-line">
  <ul>
    <li><router-link :to="{ name: 'monitoring' }">Мониторинг</router-link></li>
    <li><router-link :to="{ name: 'territories' }">Области и регионы</router-link></li>
    <li><router-link :to="{ name: 'sensors-list' }">Список датчиков</router-link></li>
    <li><router-link :to="{ name: 'forester' }">Лесничие</router-link></li>
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
    margin: 1rem auto;
    border-radius: 0.3rem;
    padding: 0.5rem;
    background: white;
  }
</style>