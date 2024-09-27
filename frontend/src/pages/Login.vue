<template>
  <div>
    <h1>Вход</h1>
    <form @submit.prevent="login">
      <div>
        <label for="email">Email</label>
        <input type="email" v-model="email" id="email" />
      </div>
      <div>
        <label for="password">Пароль</label>
        <input type="password" v-model="password" id="password" />
      </div>
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
    async login() {
      try {
        const response = await axios.post('http://127.0.0.1:8000/auth/login/', {
          email: this.email,
          password: this.password
        });
        console.log("Успешный вход:", response.data);
      } catch (error) {
        console.error("Ошибка входа:", error);
      }
    }
  }
};
</script>
