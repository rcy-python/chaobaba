import Vue from 'vue'
import Router from 'vue-router'
import Home from "../components/Home";
import User from "../components/User";
import User_detail from "../components/User_detail";

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/home',
      name: 'Home',
      component: Home
    },
    {
      path: '/user',
      name: 'user',
      component: User
    },
    {
      path: '/',
      redirect:"/home"
    },
    {
      path: '/user_detail/:id',
      component: User_detail
    },
  ]
})
