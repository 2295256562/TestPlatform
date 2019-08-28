<template>
    <div class="login-wrap">

      <el-form class="login-form" label-position="left" label-width="80px" :model="fromdata">
        <h1>用户登录</h1>
        <el-form-item label="用户名:">
          <el-input v-model="fromdata.username"></el-input>
        </el-form-item>
        <el-form-item label="密码:">
          <el-input v-model="fromdata.password"></el-input>
        </el-form-item>
        <el-button class="login-btn" type="primary">登录</el-button>
      </el-form>

    </div>
</template>

<script>
export default {
    data() {
       return {
         fromdata: {
           username:'',
           password: '',
         }
       }
    }
}
</script>

<style scoped>
.login-wrap {
  height: 100%;
  background-color: #2c3e50;
  /*弹性盒布局*/
  display: flex;
  justify-content: center;
  align-items: center;
}
.login-wrap .login-form {
  width: 400px;
  background-color: azure;
  border-radius: 5px;
  padding: 30px;
}
.login-wrap .login-btn {
   width: 100%;
}
</style>
