<template>
  <div class="register-page">
    <h1>Регистрация</h1>
    <form @submit.prevent="registerUser">
      <input v-model="email" type="email" placeholder="Email" required />
      <input v-model="username" type="text" placeholder="Имя пользователя" required />
      <input v-model="password" type="password" placeholder="Пароль" required />
      <button type="submit">Зарегистрироваться</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      email: '',
      username: '',
      password: ''
    };
  },
  methods: {
    registerUser() {
      axios.post('http://127.0.0.1:8000/auth/register/', {
        email: this.email,
        username: this.username,
        password: this.password
      })
      .then(() => {
        this.$router.push('/login');
      })
      .catch(error => {
        console.log(error);
      });
    }
  }
}
</script>

<style scoped>
.register-page {
  padding: 20px;
  text-align: center;
}
</style>
