<template>
  <div>
    <h1>Список объектов недвижимости</h1>
    <div v-for="property in properties" :key="property.id">
      <router-link :to="`/properties/${property.id}`">{{ property.name }}</router-link>
      <p>{{ property.address }}</p>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      properties: []
    };
  },
  created() {
    this.fetchProperties();
  },
  methods: {
    fetchProperties() {
      axios.get('/api/properties/')
        .then(response => {
          this.properties = response.data;
        })
        .catch(error => {
          console.error("Error fetching properties:", error);
        });
    }
  }
};
</script>
