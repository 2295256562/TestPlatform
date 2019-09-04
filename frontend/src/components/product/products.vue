<template>
  <el-card class="box-card">
    <!--      面包屑-->
    <el-breadcrumb separator="/">
      <el-breadcrumb-item :to="{ path: '/' }">首页</el-breadcrumb-item>
      <el-breadcrumb-item><a href="/">活动管理</a></el-breadcrumb-item>
      <el-breadcrumb-item>活动列表</el-breadcrumb-item>
      <el-breadcrumb-item>活动详情</el-breadcrumb-item>
    </el-breadcrumb>
    <!--    搜索-->

    <el-row class="seacrchRow">
      <el-col style="width: 30%">
        <el-input placeholder="请输入内容" v-model="query" class="inputSeach">
          <el-button slot="append" icon="el-icon-search"></el-button>
        </el-input>
      </el-col>
      <el-col style="width: 20%;text-align: left;margin-left: 23px;">
        <el-button @click="addProductHandler" type="success">添加</el-button>
      </el-col>
    </el-row>

    <!--    表格-->
    <el-table
      :data="tableData"
      class="productTable"
      border
      style="width: 100%;margin-top: 32px"
      :header-cell-style="tableHeaderColor"
    >
      <el-table-column
        prop="index"
        label="序号"
        width="180"
        type="index"
      >
      </el-table-column>
      <el-table-column
        prop="product_name"
        label="产品名称"
        width="180">
      </el-table-column>
      <el-table-column
        prop="product_desc"
        label="产品描述">
      </el-table-column>
      <el-table-column
        prop="product_user"
        label="产品负责人">
      </el-table-column>
      <el-table-column
        prop="creater_time"
        label="添加日期">
      </el-table-column>
      <el-table-column label="操作">
        <template slot-scope="scope">
          <el-button
            size="mini"
            @click="handleEdit(scope.$index, scope.row)">编辑
          </el-button>
          <el-button
            size="mini"
            type="danger"
            @click="handleDelete(scope.$index, scope.row)">删除
          </el-button>
        </template>
      </el-table-column>
    </el-table>

    <!--    分页-->
    <el-pagination
      @size-change="handleSizeChange"
      @current-change="handleCurrentChange"
      :current-page="page"
      :page-sizes="[10,20]"
      :page-size="10"
      layout="total, sizes, prev, pager, next, jumper"
      :total="count">
    </el-pagination>
  </el-card>

  <!-- 添加用户的对话框 -->
    <el-dialog
      title="添加用户"
      :visible.sync="addDialogVisible"
      width="50%"
      @close="addDialogClosed">
      <!-- 添加用户的表单 -->
      <el-form :model="addForm" :rules="addFormRules" ref="addFormRef" label-width="70px">
        <el-form-item label="产品名称" prop="username">
          <el-input v-model="addForm.username"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input v-model="addForm.password"></el-input>
        </el-form-item>
        <el-form-item label="邮箱" prop="email">
          <el-input v-model="addForm.email"></el-input>
        </el-form-item>
        <el-form-item label="手机" prop="mobile">
          <el-input v-model="addForm.mobile"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="addDialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="addUser">确 定</el-button>
      </span>
    </el-dialog>
</template>

<script>
import {time} from '@/assets/js/shijianchuo'   //处理时间戳
export default {
  name: "products",

  async created() {
    // 实例创建完成后执行的钩子函数
    const res = await this.$http.get(`products/?&page=${this.page}&pagesiez=${this.pagesize}`)
    this.tableData = res.data.data.map(item => {
      item.creater_time = time(item.creater_time)
      return item
    })

    // this.count = res.data.count
    this.getproductList()
  },

  data() {
    return {
      tableData: [],
      query: "",
      count: -1,
      page: 1,
      pagesize: 10
    }
  },


  methods: {
    async getproductList() {
      // query 查询参数可以为空
      // pagenum  当前页码 不能为空
      // pagesiez 每页显示条数  不能为空
      const res = await this.$http.get(
        `products/?&page=${this.page}&pagesiez=${this.pagesize}`)
      this.count = res.data.count
      this.tableData = res.data.data
    },
    addProductHandler() {
      // 点击新建产品跳页
      this.$router.push({path: '/home/addProduct'})
    },
    // 表格头部颜色
    tableHeaderColor({row, column, rowIndex, columnIndex}) {
      if (rowIndex === 0) {
        return 'background-color: #409EFF;color: #fff;font-weight: 500;'
      }
    },
    // 分页相关方法
    handleSizeChange(val) {
      console.log(`每页${val}条`)
      this.pagesize = val
      this.getproductList()
    },
    handleCurrentChange(val) {
      console.log(`当前页${val}条`)
      this.page = val
      this.getproductList()
    },

    handleEdit(){
      this.dialog
    }
  },
}
</script>

<style scoped>
  .box-card {
    height: 100%;
  }

  .inputSeach {
    width: 400px;
  }

  .seacrchRow {
    margin-top: 30px;
  }

</style>
