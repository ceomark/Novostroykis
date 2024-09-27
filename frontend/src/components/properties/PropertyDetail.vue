<template>
  <div v-if="property">
    <h1>{{ property.name }}</h1>
    <p>Адрес: {{ property.address }}</p>
    <p>Этажность: {{ property.number_of_floors }}</p>
    <p>Цена от: {{ property.price_from }} ₽</p>
    <router-link :to="`/properties/${property.id}/reviews`">Отзывы</router-link>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  props: ['id'],
  data() {
    return {
      property: null
    };
  },
  created() {
    this.fetchProperty();
  },
  methods: {
    fetchProperty() {
      axios.get(`/api/properties/${this.id}/`)
        .then(response => {
          this.property = response.data;
        })
        .catch(error => {
          console.error("Error fetching property:", error);
        });
    }
  }
};
</script>
