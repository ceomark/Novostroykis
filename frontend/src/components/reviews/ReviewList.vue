<template>
  <div>
    <h1>Отзывы</h1>
    <div v-for="review in reviews" :key="review.id">
      <p>{{ review.user.username }}: {{ review.comment }} ({{ review.rating }} звёзд)</p>
    </div>
    <router-link :to="`/properties/${$route.params.id}/reviews/add`">Добавить отзыв</router-link>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      reviews: []
    };
  },
  created() {
    this.fetchReviews();
  },
  methods: {
    fetchReviews() {
      axios.get(`/api/reviews/${this.$route.params.id}/`)
        .then(response => {
          this.reviews = response.data;
        })
        .catch(error => {
          console.error("Error fetching reviews:", error);
        });
    }
  }
};
</script>
