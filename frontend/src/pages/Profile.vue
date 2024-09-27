<template>
  <div class="profile-page">
    <h1>Профиль пользователя</h1>
    <div v-if="user">
      <p><strong>Email:</strong> {{ user.email }}</p>
      <p><strong>Имя пользователя:</strong> {{ user.username }}</p>
      <button @click="logout">Выйти</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      user: null
    };
  },
  methods: {
    fetchUserProfile() {
      axios.get('http://127.0.0.1:8000/auth/profile/', {
        headers: {
          'Authorization': `Bearer ${localStorage.getItem('access_token')}`
        }
      })
      .then(response => {
        this.user = response.data;
      })
      .catch(error => {
        console.log(error);
      });
    },
    logout() {
      localStorage.removeItem('access_token');
      this.$router.push('/login');
    }
  },
  created() {
    this.fetchUserProfile();
  }
}
</script>

<style scoped>
.profile-page {
  padding: 20px;
}
</style>
