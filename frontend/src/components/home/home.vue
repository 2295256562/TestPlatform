<template>
  <el-container class="container">
    <el-header class="header">
      <el-row>
        <el-col :span="4">
          <div class="grid-content bg-purple">
            <img src="" alt="无法显示图片">
          </div>
        </el-col>
        <el-col :span="18">
          <h3 class="middle">测试平台</h3>
        </el-col>
        <el-col :span="2">
          <div class="grid-content bg-purple">
            <a class="logout" href="#">退出</a>
          </div>
        </el-col>
      </el-row>
    </el-header>
    <el-container>
      <el-aside class="aside" width="200px">

        <el-menu
          background-color="#545c64"
          default-active="/home/index"
          text-color="#fff"
          active-text-color="red"
          style="text-align: left"
          @select="select"
        >
          <el-menu-item index="/home/index">
            <i class="el-icon-menu"></i>
            <span slot="title">首页</span>
          </el-menu-item>

          <el-menu-item index="/home/product">
            <i class="el-icon-menu"></i>
            <span slot="title">项目管理</span>
          </el-menu-item>

          <el-submenu index="3">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span>导航一</span>
            </template>
            <el-menu-item index="3-1">
              <i class="el-icon-location"></i>
              <span>选修</span>
            </el-menu-item>
          </el-submenu>
        </el-menu>
      </el-aside>
      <el-main class="main">
        <router-view />
      </el-main>
    </el-container>
  </el-container>

</template>

<script>
  export default {
    name: "home",
    // data() {
    //   return {
    //     index: '/home/index'
    //   }
    // },
    methods: {
      select(key, keypath) {
        console.log(key, keypath)
        this.$router.push({ path: key })
        // if (v == 2) {
        //   this.$router.push({path: '/home/product'})
        // } else if (v == 1) {
        //   this.$router.push({path: '/home/index'})
        // }

      }
    },
    // created() {
    //   this.index = '/home/index'
    // }
  }
</script>

<style>
  .container {
    height: 100%;
  }

  .header {
    background-color: #f68e54;
  }

  .aside {
    background-color: black;
  }

  .main {
    background-color: #eee;
  }

  .middle {
    text-align: center;
  }

  .logout {
    line-height: 50px;
    text-decoration: none;
  }
</style>
