<template>
<div>这是userdetail
用户详情页接受传递的id --->:{{$route.params.id}}
</div>
</template>

<script>
export default {
name: "User_detail",
  data(){
  return{
    id:''
  }
  },
  beforeMount() {
  }
}




</script>

<style scoped>

</style>
