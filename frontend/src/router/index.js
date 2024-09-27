import Vue from 'vue';
import Router from 'vue-router';
import HomePage from '@/pages/HomePage';
import UserRegister from '@/pages/UserRegister';
import UserLogin from '@/pages/UserLogin';
import UserProfile from '@/pages/UserProfile';
import AdminDashboard from '@/pages/AdminDashboard';
import ModeratorDashboard from '@/pages/ModeratorDashboard';
import PropertyList from '@/components/properties/PropertyList';
import PropertyDetail from '@/components/properties/PropertyDetail';
import DeveloperList from '@/components/developers/DeveloperList';
import DeveloperDetail from '@/components/developers/DeveloperDetail';
import ReviewList from '@/components/reviews/ReviewList';
import ReviewForm from '@/components/reviews/ReviewForm';

Vue.use(Router);

// Функция для проверки авторизации
const requireAuth = (to, from, next) => {
  const isAuthenticated = localStorage.getItem('access_token'); // Проверка наличия токена
  if (!isAuthenticated) {
    next('/login');
  } else {
    next();
  }
};

export default new Router({
  mode: 'history',
  routes: [
    { path: '/', component: HomePage }, // Главная страница
    { path: '/register', component: UserRegister }, // Страница регистрации
    { path: '/login', component: UserLogin }, // Страница логина
    { path: '/profile', component: UserProfile, beforeEnter: requireAuth },  // Профиль пользователя с проверкой авторизации
    { path: '/admin-dashboard', component: AdminDashboard, beforeEnter: requireAuth }, // Проверка авторизации
    { path: '/moderator-dashboard', component: ModeratorDashboard, beforeEnter: requireAuth }, // Проверка авторизации
    { path: '*', redirect: '/' }, // Перенаправление всех неизвестных маршрутов на главную страницу
    { path: '/novostroyki', component: PropertyList }, // Список объектов недвижимости
    { path: '/novostroyki/:id', component: PropertyDetail, props: true }, // Детальная страница объекта
    { path: '/zastroyshiki', component: DeveloperList }, // Список застройщиков
    { path: '/zastroyshiki/:id', component: DeveloperDetail, props: true }, // Детальная страница застройщика
    { path: '/novostroyki/:id/reviews', component: ReviewList, props: true }, // Список отзывов к объекту
    { path: '/zastroyshiki/:id/reviews', component: ReviewList, props: true }, // Список отзывов к застройщику
    { path: '/novostroyki/:id/reviews/add', component: ReviewForm, props: true }, // Добавление отзыва к объекту
    { path: '/zastroyshiki/:id/reviews/add', component: ReviewForm, props: true }, // Добавление отзыва к застройщику
  ]
});
