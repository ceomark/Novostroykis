<template>
  <div>
    <h1>Регистрация пользователя</h1>
    <form @submit.prevent="register">
      <div>
        <label for="username">Имя пользователя</label>
        <input type="text" id="username" v-model="username" required />
      </div>
      <div>
        <label for="email">Email</label>
        <input type="email" id="email" v-model="email" required />
      </div>
      <div>
        <label for="password">Пароль</label>
        <input type="password" id="password" v-model="password" required />
      </div>
      <button type="submit">Зарегистрироваться</button>
    </form>
    <p v-if="errorMessage" style="color: red;">{{ errorMessage }}</p>
  </div>
</template>

<script>
// Импортируем axios для отправки HTTP-запросов
import axios from 'axios';

export default {
  name: 'UserRegister',
  data() {
    return {
      username: '',  // Поле для имени пользователя
      email: '',     // Поле для email
      password: '',  // Поле для пароля
      errorMessage: ''  // Сообщение об ошибке при регистрации
    };
  },
  methods: {
    // Метод для регистрации пользователя
    register() {
      const userData = {
        username: this.username,
        email: this.email,
        password: this.password
      };

      // Используем переменную окружения из .env файла
      axios
        .post(`${process.env.VUE_APP_API_BASE_URL}/auth/register/`, userData)
        .then(() => {
          alert('Регистрация успешна!');
          this.$router.push('/login'); // Перенаправляем на страницу логина после успешной регистрации
        })
        .catch((error) => {
          this.errorMessage = 'Ошибка регистрации: ' + (error.response.data.detail || error.message);
        });
    }
  }
};
</script>
