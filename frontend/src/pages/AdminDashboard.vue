<template>
  <div>
    <h1>Админ Панель</h1>
    <p>{{ message }}</p>
  </div>
</template>

<script>
import axios from '@/axios';

export default {
  name: 'AdminDashboard',
  data() {
    return {
      message: ''
    };
  },
  mounted() {
    axios.get('/auth/admin-dashboard/')
      .then(response => {
        this.message = response.data.msg;
      })
      .catch(error => {
        console.error(error);
      });
  }
};
</script>
