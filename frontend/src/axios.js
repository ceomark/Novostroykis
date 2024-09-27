import axios from 'axios';

// Базовая конфигурация axios
const apiClient = axios.create({
  baseURL: 'http://127.0.0.1:8000/api/',
  headers: {
    'Content-Type': 'application/json',
  },
  withCredentials: true,
});

// Добавление токена в заголовки при каждом запросе
apiClient.interceptors.request.use(config => {
  const token = localStorage.getItem('token');  // Предполагается, что токен хранится в localStorage
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

export default apiClient;
