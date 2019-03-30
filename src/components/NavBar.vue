<template>
<nav class="navbar navbar-expand-lg blue-gradient">
  <a class="navbar-brand text-light" href="#">Мой Лес</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarColor01" aria-controls="navbarColor01" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarColor01">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <a class="nav-link text-light" href="#">Система уравления <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link text-light" href="#">Лесничие</a>
      </li>
      <li class="nav-item">
        <a class="nav-link text-light" href="#">Экстренная связь</a>
      </li>
      <li class="nav-item">
        <a class="nav-link text-light" href="#">Обновление</a>
      </li>
    </ul>
    <form class="form-inline text-span">
      <button class="btn btn-secondary my-sm-0" type="submit">Выход</button>
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