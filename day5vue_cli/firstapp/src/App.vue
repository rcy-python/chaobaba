<template>
  <div id="app">
    <h3>这是主页</h3>
    <router-link to="/home">访问home</router-link>
    <router-link to="/user">访问User</router-link>
    <router-view></router-view>
  </div>
</template>

<script>


export default {
  name: 'App',
  comments:{
  }
}
</script>

<style>

</style>
