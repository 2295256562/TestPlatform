<template>
  <div>
    <el-button @click="addProductHandler" class="add_product" type="primary">新建产品</el-button>

    <el-table
      :data="tableData"
      class="productTable"
      border
      style="width: 100%"
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
          @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
        <el-button
          size="mini"
          type="danger"
          @click="handleDelete(scope.$index, scope.row)">删除</el-button>
      </template>
    </el-table-column>
    </el-table>
  </div>
</template>

<script>
  import { time } from '@/assets/js/shijianchuo'
  export default {
    name: "product",
    methods: {
      addProductHandler() {
        // this.$router.push({ path: '/home/addProduct' })
        this.$router.push({path: '/home/addProduct'})
      },
      tableHeaderColor({row, column, rowIndex, columnIndex}) {
        if (rowIndex === 0) {
          return 'background-color: gray;color: #fff;font-weight: 500;'
        }
      }
    },
    async created() {
        const res = await this.$http.get('products/')
        this.tableData = res.data.data.map(item => {
          item.creater_time = time(item.creater_time)
          return item
        })
    },
    data() {
      return {
        tableData: []
      }
    }
  }
</script>

<style scoped>
  .add_product {
    float: left;
    margin-bottom: 40px;
  }

</style>
