<template>
  <div>这是User组件
  <h3>用户列表页</h3>
  <table border="2px">
    <tr>
      <td>ID</td>
      <td>姓名</td>
      <td>年龄</td>
      <td>个人信息</td>
      <td>操作</td>
    </tr>
    <tr v-for=" (user,index) in users" :Key="index">
      <td>{{user.id}}</td>
      <td>{{user.username}}</td>
      <td>{{user.bir}}</td>
      <td>{{user.content}}</td>
      <td><a href="javascript:0;" @click="delete_one(index)" >删除</a>丨<router-link :to="`/user_detail/${user.id}`">查看用户详情</router-link></td>
    </tr>
  </table><h2>添加用户信息</h2>
  用户名:<input type="text" v-model="new_username"><br>
  附加内容:<input type="text" v-model="new_content"><br>
  生日:<input type="text" v-model="new_bir"><br>
    <button value="添加" @click="add_one">添加</button>
  </div>
</template>

<script>
export default {
  name: "User",
  data(){
  return{
    users: localStorage.stu ? JSON.parse(localStorage.stu) : [],
    new_username:'',
    new_content:'',
    new_bir:'',
    id:1
  }
  },
  methods:{
    delete_one(index){
      this.users.splice(index,1)
      localStorage.stu = JSON.stringify(this.users);
    },
    add_one(){
      let msg = this.new_username;
      if(msg){
        this.users.push({id:this.id,username:this.new_username,bir:this.new_bir,content:this.new_content})
        localStorage.stu = JSON.stringify(this.users);
        this.id+=1
      }
      this.new_content=""
      this.new_bir=""
      this.new_username=''
    }
    }


}
</script>

<style scoped>

</style>
