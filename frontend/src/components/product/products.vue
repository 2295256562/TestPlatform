<template>
  <div>
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
        <el-col style="width: 20%;text-align: left;margin-left: 6%;">
          <el-button @click="addProductHandler" type="success">添加</el-button>
        </el-col>
      </el-row>

      <!--    表格-->
      <div>
        <el-table
          :data="tableData"
          border
          style="width: 100%;margin-top: 32px"
          :header-cell-style="{ background: '#87F0E5' }"
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
                @click="handleEdit(scope.row)">编辑
              </el-button>
              <el-button
                size="mini"
                type="danger"
                @click="handleDelete(scope.$index, scope.row)">删除
              </el-button>
            </template>
          </el-table-column>
        </el-table>
      </div>

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

    <i-modal
      :addForm="addForm"
      :sign="sign"
      :show="show"
      :title="title"
      @close="close"
    />
  </div>
</template>


<script>
    import {time} from '@/assets/js/shijianchuo'   //处理时间戳
    import Modal from '../model/add'

    export default {
        name: "products",

        components: {
            'i-modal': Modal
        },

        async created() {
            // // 实例创建完成后执行的钩子函数
            // const res = await this.$http.get(`products/?&page=${this.page}&pagesiez=${this.pagesize}`)
            // this.tableData = res.data.data.map(item => {
            //   item.creater_time = time(item.creater_time)
            //   return item
            // })

            // this.count = res.data.count
            this.getproductList()
        },

        data() {
            return {
                tableData: [],
                query: "",
                count: -1,
                page: 1,
                pagesize: 10,
                addForm: {
                    id:-1,
                    productname: '',
                    productdesc: '',
                    productuser:''
                },
                sign: 'add',
                show: false,
                title: '新增用户'
            }
        },


        methods: {
            async getproductList() {
                // query 查询参数可以为空
                // pagenum  当前页码 不能为空
                // pagesiez 每页显示条数  不能为空
                const res = await this.$http.get(
                    `products/?&page=${this.page}&pagesize=${this.pagesize}`)
                this.count = res.data.count
                this.tableData = res.data.data.map(_v => {
                    _v.creater_time = time(_v.creater_time)
                    return _v
                })
            },
            addProductHandler() {
                // 点击新建产品跳页
                // this.$router.push({path: '/home/addProduct'})
                this.show = true
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
            handleEdit(row) {
                this.sign = 'edit'
                this.title = '编辑用户'
                this.$http.get('products/' + row.id + '/').then(res => {
                    const {product_name, product_desc, product_user} = res.data.data
                    console.log(product_name, 'product_name')

                    this.addForm = {
                        id:row.id,
                        productname: product_name,
                        productdesc: product_desc,
                        productuser: product_user
                    }
                    this.show = true
                })

            },

            open() {
                console.log('111')
            },
            close() {
                this.show = false
                this.addForm = {
                    id:-1,
                    productname: '',
                    productdesc:'',
                    productuser:''
                }
                this.sign = 'add'
                this.title = '新增用户'
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

<style>
  * {
    margin: 0;
    padding: 0;
  }

  body .el-table th.gutter {
    display: table-cell !important;
  }

</style>
