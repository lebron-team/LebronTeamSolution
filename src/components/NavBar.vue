<template>
<nav class="navbar navbar-expand-lg blue-gradient">
  <a href="/">
    <img class="mr-3" src="../assets/tree.png" href="/" height="40" alt="На главную"/>
  </a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarColor01" aria-controls="navbarColor01" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarColor01">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <router-link class="nav-link text-light" :to="{ name: 'home' }">Панель управления</router-link>
      </li>
      <li class="nav-item">
        <router-link class="nav-link text-light" :to="{ name: 'emergency' }">Экстренная связь</router-link>
      </li>
      <li class="nav-item">
        <router-link class="nav-link text-light" :to="{ name: 'update' }">Обновления</router-link>
      </li>
    </ul>
    <form class="form-inline text-span">
      <button class="btn btn-primary my-sm-0" type="submit">Выход</button>
    </form>
  </div>
</nav>
</template>

<script>
    export default {
        name: "NavBar"
    }
</script>

<style scoped>

</style>