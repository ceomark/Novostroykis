<template>
  <div>
    <h1>User Profile</h1>
    <div v-if="user">
      <form @submit.prevent="updateProfile">
        <div>
          <label for="username">Username</label>
          <input v-model="username" type="text" id="username" required />
        </div>
        <div>
          <label for="email">Email</label>
          <input v-model="email" type="email" id="email" required />
        </div>
        <button type="submit">Update Profile</button>
      </form>
      <button @click="deleteProfile">Delete Profile</button>
    </div>
  </div>
</template>

<script>
import axios from '@/axios';

export default {
  name: 'UserProfile',
  data() {
    return {
      user: null,
      username: '',
      email: ''
    };
  },
  methods: {
    fetchUserProfile() {
      axios.get('/auth/profile/')
        .then((res) => { // Изменил на `res` и убрал вывод ненужного `response`
          this.user = res.data;
          this.username = this.user.username;
          this.email = this.user.email;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    updateProfile() {
      axios.put('/auth/profile/', {
        username: this.username,
        email: this.email
      })
      .then(() => {
        console.log("Profile updated successfully!");
      })
      .catch((error) => {
        console.error(error);
      });
    },
    deleteProfile() {
      if (confirm('Are you sure you want to delete your profile?')) {
        axios.delete('/auth/profile/delete/')
          .then(() => {
            alert('Profile deleted successfully!');
            this.$router.push('/login');
          })
          .catch((error) => {
            console.error(error);
          });
      }
    }
  },
  mounted() {
    this.fetchUserProfile();
  }
};
</script>
