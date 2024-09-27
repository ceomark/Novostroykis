<template>
  <div>
    <h1>Список недвижимости</h1>
    <ul>
      <li v-for="property in properties" :key="property.id">
        {{ property.title }} - {{ property.price }}
      </li>
    </ul>
  </div>
</template>

<script>
import apiClient from '../axios';

export default {
  data() {
    return {
      properties: []  // Хранение данных о недвижимости
    };
  },
  async created() {
    try {
      // Запрос на получение списка недвижимости с API
      const response = await apiClient.get('properties/');
      this.properties = response.data;  // Сохранение полученных данных в state
    } catch (error) {
      console.error("Ошибка при загрузке списка недвижимости:", error);
    }
  }
};
</script>
<script>
export default {
  name: "PropertyList",  // Измени на соответствующее имя компонента
  mounted() {
    console.log("Компонент Home загружен");
  }
};
</script>