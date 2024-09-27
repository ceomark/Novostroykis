<template>
  <div>
    <h1>Модератор Панель</h1>
    <p>{{ message }}</p>
  </div>
</template>

<script>
import axios from '@/axios';

export default {
  name: 'ModeratorDashboard',
  data() {
    return {
      message: ''
    };
  },
  mounted() {
    axios.get('/auth/moderator-dashboard/')
      .then(response => {
        this.message = response.data.msg;
      })
      .catch(error => {
        console.error(error);
      });
  }
};
</script>
