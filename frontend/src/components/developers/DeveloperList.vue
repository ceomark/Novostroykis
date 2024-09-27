<template>
  <div>
    <h1>Список застройщиков</h1>
    <div v-for="developer in developers" :key="developer.id">
      <router-link :to="`/developers/${developer.id}`">{{ developer.name }}</router-link>
      <p>Рейтинг: {{ developer.rating }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      developers: []
    };
  },
  created() {
    this.fetchDevelopers();
  },
  methods: {
    fetchDevelopers() {
      axios.get('/api/developers/')
        .then(response => {
          this.developers = response.data;
        })
        .catch(error => {
          console.error("Error fetching developers:", error);
        });
    }
  }
};
</script>
