<template>
    <div class="login-wrap">

      <el-form class="login-form" label-position="left" label-width="80px" :model="fromdata" :rules="rules">
        <h1>用户登录</h1>
        <el-form-item label="用户名:" prop="username">
          <el-input v-model.trim="fromdata.username"></el-input>
        </el-form-item>
        <el-form-item label="密码:" prop="password">
          <el-input type="password" v-model.trim="fromdata.password"></el-input>
        </el-form-item>
        <el-button @click.prevent="handleLogin()" class="login-btn" type="primary">登录</el-button>
      </el-form>

    </div>
</template>

<script>
export default {
    data() {
       return {
         fromdata: {
           username:'',
           password: ''
         },
         // 表单输入规则校验
         rules: {
           username:[{required:true, message: '请输入用户名', trigger: 'blur'}],
           password:[{required:true, message: '请输入密码', trigger: 'blur'}],
         }
       }
    },
    methods: {
       handleLogin() {
         this.$http.post('login', this.fromdata).then(res => {
           console.log(res)
           const {
             data, msg, status
           } = res.data
           if (status === 200) {
              // 登录成功
              // 保存token值 目的：如果用户没登录不让进入页面，登录成功后保存token
             localStorage.setItem('token', data[0].token)
              // 跳转home
             this.$router.push({name:'index'})
             // 提示成功
             this.$message.success("登陆成功")
           } else {
             // 不成功
             // 提示信息
             this.$message.error(msg)
           }
         })
           // .catch(e => this.$message.error('xxxxx'))
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
