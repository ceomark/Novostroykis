<template>
  <div>
    <h1>Добавить отзыв</h1>
    <form @submit.prevent="submitReview">
      <div>
        <label for="rating">Рейтинг</label>
        <input type="number" v-model="rating" min="1" max="5" required />
      </div>
      <div>
        <label for="comment">Комментарий</label>
        <textarea v-model="comment" required></textarea>
      </div>
      <button type="submit">Отправить</button>
    </form>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  props: ['id'],
  data() {
    return {
      rating: 5,
      comment: ''
    };
  },
  methods: {
    submitReview() {
      axios.post(`/api/reviews/${this.id}/`, { rating: this.rating, comment: this.comment })
        .then(() => {
          alert("Отзыв успешно добавлен");
          this.$router.push(`/properties/${this.id}`);
        })
        .catch(error => {
          console.error("Error adding review:", error);
        });
    }
  }
};
</script>
