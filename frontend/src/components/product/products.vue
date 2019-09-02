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
      :current-page="currentPage4"
      :page-sizes="10"
      :page-size="100"
      layout="total, sizes, prev, pager, next, jumper"
      :total="400">
    </el-pagination>

  </el-card>
</template>

<script>
import {time} from '@/assets/js/shijianchuo'   //处理时间戳
export default {
  name: "products",

  async created() {
    // 实例创建完成后执行的钩子函数
    const res = await this.$http.get('products/')
    this.tableData = res.data.data.map(item => {
      item.creater_time = time(item.creater_time)
      return item
    })
  },
  data() {
    return {
      tableData: [],
      query: ""
    }
  },
  async getproductList(){
    // query 查询参数可以为空
    // pagenum  当前页码 不能为空
    // pagesiez 每页显示条数  不能为空
    const res = await this.$http.get(
      `products/?page=${this.page}&pagesiez=${this.pagesize}`)
  },

  methods: {
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
    handleSizeChange(){},
    handleCurrentChange(){},
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
