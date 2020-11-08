import Vue from 'vue'
import Router from 'vue-router'
import Home from "../components/Home";
import Login from "../components/Login";
import Register from "../components/Register";
import Login_msg from "../components/Login_msg";


Vue.use(Router)

export default new Router({
  routes: [

      {path: "/home", component: Home},
      {path: "/", redirect: "/home"},
      {path: "/login", component: Login},
      {path:"/register",component: Register},
      {path:"/msg_login",component: Login_msg},

  ]
})
