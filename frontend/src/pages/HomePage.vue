<template>
  <div class="home">
    <h1>Привет, это интеграция Vue.js и Django! </h1>
  </div>
</template>

<script>
export default {
  name: 'HomePage'
}
</script>

<style scoped>
.home {
  padding: 20px;
  text-align: center;
}
</style>
<script>
export default {
  name: "HomePage",  // Измени на соответствующее имя компонента
  mounted() {
    console.log("Компонент Home загружен");
  }
};
</script>