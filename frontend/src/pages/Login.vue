<template>
  <div class="login-page">
    <h1>Вход</h1>
    <form @submit.prevent="loginUser">
      <input v-model="email" type="email" placeholder="Email" required />
      <input v-model="password" type="password" placeholder="Пароль" required />
      <button type="submit">Войти</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      email: '',
      password: ''
    };
  },
  methods: {
    loginUser() {
      axios.post('http://127.0.0.1:8000/auth/login/', {
        email: this.email,
        password: this.password
      })
      .then(response => {
        localStorage.setItem('access_token', response.data.access);
        this.$router.push('/profile');
      })
      .catch(error => {
        console.log(error);
      });
    }
  }
}
</script>

<style scoped>
.login-page {
  padding: 20px;
  text-align: center;
}
</style>
