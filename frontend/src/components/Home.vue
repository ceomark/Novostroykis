<template>
  <div>
    <h1>Добро пожаловать на Novostroykis!</h1>
    <p>Используйте навигацию для перехода на страницы регистрации и входа.</p>
    <router-link to="/register">Регистрация</router-link> |
    <router-link to="/login">Вход</router-link>
  </div>
</template>

<script>
export default {
  name: "Home"
};
</script>
