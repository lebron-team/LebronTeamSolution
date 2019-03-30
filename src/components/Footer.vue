<template>
    <div class="footer-style">
        <div class="container">
          <p class="footer-block">Place sticky footer content here.</p>
        </div>
    </div>
</template>

<script>
    export default {
        name: "Footer"
    }
</script>

<style scoped>
  .footer-style {
    bottom: 0;
    width: 100%;
    position: absolute;
    height: 5rem;
    background-color: #f5f5f5;
    margin: 20px 0;
  }


</style>