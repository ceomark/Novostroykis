import Vue from 'vue';
import Router from 'vue-router';
import HomePage from '@/pages/HomePage';
import UserRegister from '@/pages/UserRegister';
import UserLogin from '@/pages/UserLogin';
import UserProfile from '@/pages/UserProfile';
import PropertyList from '@/pages/PropertyList';

Vue.use(Router);

function requireAuth(to, from, next) {
  if (!localStorage.getItem('token')) {
    next('/login');
  } else {
    next();
  }
}

export default new Router({
  mode: 'history',
  routes: [
    { path: '/', component: HomePage },
    { path: '/register', component: UserRegister },
    { path: '/login', component: UserLogin },
    { path: '/profile', component: UserProfile },
    { path: '/properties', component: PropertyList },
    { path: '/admin-dashboard', component: AdminDashboard },
    { path: '/moderator-dashboard', component: ModeratorDashboard },
    { path: '*', redirect: '/' }
  ]
});