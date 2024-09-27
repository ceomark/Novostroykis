<template>
  <div>
    <h1>Вход</h1>
    <form @submit.prevent="login">
      <div>
        <label for="email">Email</label>
        <input type="email" id="email" v-model="email" required />
      </div>
      <div>
        <label for="password">Пароль</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <button type="submit">Войти</button>
    </form>
    <p v-if="errorMessage" style="color: red;">{{ errorMessage }}</p>
  </div>
</template>

<script>
import axios from '@/axios';

export default {
  name: 'UserLogin',
  data() {
    return {
      email: '',
      password: '',
      errorMessage: ''
    };
  },
  methods: {
    // Метод для входа пользователя
    login() {
      const userData = {
        email: this.email,
        password: this.password
      };
      axios
        .post(`${process.env.VUE_APP_API_BASE_URL}/auth/login/`, userData)
        .then(response => {
          // Сохраняем токен в localStorage
          localStorage.setItem('access_token', response.data.access);
          localStorage.setItem('refresh_token', response.data.refresh);
          this.$router.push('/profile');  // Перенаправляем на страницу профиля
        })
        .catch((error) => {
          this.errorMessage = 'Ошибка входа: ' + (error.response.data.detail || error.message);
        });
    }
  }
};
</script>
