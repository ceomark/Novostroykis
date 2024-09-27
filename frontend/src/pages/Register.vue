<template>
  <div>
    <h1>Регистрация</h1>
    <form @submit.prevent="register">
      <div>
        <label for="username">Имя пользователя</label>
        <input type="text" v-model="username" id="username" />
      </div>
      <div>
        <label for="email">Email</label>
        <input type="email" v-model="email" id="email" />
      </div>
      <div>
        <label for="password">Пароль</label>
        <input type="password" v-model="password" id="password" />
      </div>
      <button type="submit">Зарегистрироваться</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      email: '',
      password: ''
    };
  },
  methods: {
    async register() {
      try {
        await axios.post('http://127.0.0.1:8000/auth/register/', {
          username: this.username,
          email: this.email,
          password: this.password
        });
        this.$router.push('/login');
      } catch (error) {
        console.error("Ошибка регистрации:", error);
      }
    }
  }
};
</script>
