<template>
  <div>
    <h1>Список новостроек</h1>
    <ul v-if="properties.length">
      <!-- Добавляем ссылку на детальный вид -->
      <li v-for="property in properties" :key="property.id">
        <router-link :to="`/properties/${property.id}`">{{ property.name }}</router-link>
      </li>
    </ul>
    <p v-else>Нет данных для отображения.</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'PropertyList',
  data() {
    return {
      properties: [],
    };
  },
  mounted() {
    // Отправляем запрос на сервер, чтобы получить список объектов недвижимости
    axios.get('http://localhost:8000/api/properties/')
      .then(response => {
        this.properties = response.data;
      })
      .catch(error => {
        console.error('Ошибка при получении данных:', error);
      });
  },
};
</script>
