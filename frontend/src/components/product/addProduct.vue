<template>
  <div class="product_div">
    <el-form :model="ruleForm" :rules="rules" ref="ruleForm" label-width="100px" class="demo-ruleForm">
      <el-form-item label="产品名称" prop="productname" style="text-align: left">
        <el-input class="product_input" v-model="ruleForm.productname"></el-input>
      </el-form-item>
      <el-form-item label="产品描述" prop="productdesc" style="text-align: left">
        <el-input class="product_input" v-model="ruleForm.productdesc"></el-input>
      </el-form-item>
      <el-form-item label="产品负责人" prop="productuser" style="text-align: left">
        <el-input class="product_input" v-model="ruleForm.productuser"></el-input>
      </el-form-item>
      <el-form-item size="large" style="text-align: left">
        <el-button type="primary" @click="onSubmit">保存</el-button>
        <el-button @click="cancel">取消</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  name: "addProduct",
  // 创建前执行的钩子函数
  created() {
    const {id} = this.$route.query
    if (id) {
      this.getdetails();
    }

  },
  data() {
    return {
      ruleForm: {
        productname: '',
        productdesc: '',
        productuser: ''
      },
      rules: {
        productname: [
          {required: true, message: '请输入活动名称', trigger: 'blur'}
        ],
        productuser: [
          {required: true, message: '请输入活动名称', trigger: 'blur'}
        ],
      }
    }
  },
  methods: {


    // 请求接口 新增产品
    async onSubmit() {
      const {id} = this.$route.query
      const {productname, productdesc, productuser} = this.ruleForm
      if (!id) {
        const res = await this.$http.post('add_product/', {
          product_name: productname,
          product_desc: productdesc,
          product_user: productuser
        })
        const {code, product_name, msg} = res.data
        if (code === 201) {
          this.$router.push({name: 'product'})
        } else {
          this.$message.warning(product_name[0])
        }
      } else {
        const res = await this.$http.put('products/' + id + '/', {
          product_name: productname,
          product_desc: productdesc,
          product_user: productuser
        })
        const {code, product_name, msg} = res.data
        if (code === 200) {
          this.$router.push({name: 'product'})
        } else {
          this.$message.warning(product_name[0])
        }
      }


    },

    // 点击取消按钮返回列表页
    cancel() {
      this.$router.push({name: 'product'})
    },

    // 通过点击编辑按钮的id返回的数据渲染到表单中
    getdetails() {
      this.$http.get('products/' + this.$route.query.id + '/').then(res => {
        const {product_name, product_desc, product_user} = res.data.data
        console.log(product_name, 'product_name')
        this.ruleForm = {
          productname: product_name,
          productdesc: product_desc,
          productuser: product_user
        }
        console.log(res, 'res')
      })
    }
  }
}
</script>

<style scoped>
  .product_div {
    margin: 10px;
    background-color: #fff;
    border-radius: 4px;
    padding: 16px;
  }

  .product_input {
    width: 400px;
  }
</style>
