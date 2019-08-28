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
        <el-menu>
          <el-submenu index="1">
            <template slot="title">
              <i class="el-icon-location"></i>
              <span>导航一</span>
            </template>
            <el-menu-item index="1-1">
              <i class="el-icon-location"></i>
              <span>选修</span>
            </el-menu-item>
          </el-submenu>

        </el-menu>
      </el-aside>
      <el-main class="main">Main</el-main>
    </el-container>
  </el-container>

</template>

<script>
export default {
  name: "home"
}
</script>

<style>
  .container {
    height: 100%;
  }

  .header {
    background-color: honeydew;
  }

  .aside {
    background-color: #42b983;
  }

  .main {
    background-color: #b3c0d1;
  }

  .middle {
    text-align: center;
  }

  .logout {
    line-height: 50px;
    text-decoration: none;
  }
</style>
