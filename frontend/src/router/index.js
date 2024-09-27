import Vue from 'vue';
import Router from 'vue-router';
import HomePage from '@/pages/HomePage';
import UserRegister from '@/pages/UserRegister';
import UserLogin from '@/pages/UserLogin';
import UserProfile from '@/pages/UserProfile';
import PropertyList from '@/pages/PropertyList';
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
    { path: '/', component: HomePage },
    { path: '/register', component: UserRegister },
    { path: '/login', component: UserLogin },
    { path: '/profile', component: UserProfile, beforeEnter: requireAuth },  // Проверка авторизации перед входом в профиль
    { path: '/properties', component: PropertyList },
    { path: '/admin-dashboard', component: AdminDashboard, beforeEnter: requireAuth }, // Проверка авторизации
    { path: '/moderator-dashboard', component: ModeratorDashboard, beforeEnter: requireAuth }, // Проверка авторизации
    { path: '*', redirect: '/' }
    { path: '/properties', component: PropertyList }, // Список объектов недвижимости
    { path: '/properties/:id', component: PropertyDetail, props: true }, // Детальная страница объекта
    { path: '/developers', component: DeveloperList }, // Список застройщиков
    { path: '/developers/:id', component: DeveloperDetail, props: true }, // Детальная страница застройщика
    { path: '/properties/:id/reviews', component: ReviewList, props: true }, // Список отзывов к объекту
    { path: '/developers/:id/reviews', component: ReviewList, props: true }, // Список отзывов к застройщику
    { path: '/properties/:id/reviews/add', component: ReviewForm, props: true }, // Добавление отзыва к объекту
    { path: '/developers/:id/reviews/add', component: ReviewForm, props: true }, // Добавление отзыва к застройщику
  ]
});
