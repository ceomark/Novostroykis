<template>
  <div v-if="developer">
    <h1>{{ developer.name }}</h1>
    <p>Год основания: {{ developer.founded_year }}</p>
    <p>Рейтинг: {{ developer.rating }}</p>
    <p>Описание: {{ developer.description }}</p>
    <router-link :to="`/developers/${developer.id}/reviews`">Отзывы</router-link>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  props: ['id'],
  data() {
    return {
      developer: null
    };
  },
  created() {
    this.fetchDeveloper();
  },
  methods: {
    fetchDeveloper() {
      axios.get(`/api/developers/${this.id}/`)
        .then(response => {
          this.developer = response.data;
        })
        .catch(error => {
          console.error("Error fetching developer:", error);
        });
    }
  }
};
</script>
