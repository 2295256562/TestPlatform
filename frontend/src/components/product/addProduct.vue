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


  created() {

    this.getdetails();
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
    async onSubmit() {

      const {productname, productdesc, productuser} = this.ruleForm
      const res = await this.$http.post('add_product/', {
        product_name: productname,
        product_desc: productdesc,
        product_user: productuser
      })
      console.log(res)
      const {code, product_name, msg} = res.data
      if (code === 201) {
        this.$router.push({name: 'product'})
      } else {
        this.$message.warning(product_name[0])
      }
      console.log(res)
    },
    cancel() {
      this.$router.push({name: 'product'})
    },
    getdetails() {
      console.log(111)
      this.$http.get('products/' + this.$route.query.id + '/').then(res => {
        console.log(res)
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
