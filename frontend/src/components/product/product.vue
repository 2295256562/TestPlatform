<template>
    <div>
      <el-button @click="addProductHandler" class="add_product" type="primary">新建产品</el-button>
    </div>
</template>

<script>
    export default {
        name: "product",
        methods: {
          addProductHandler(){
            // this.$router.push({ path: '/home/addProduct' })
            this.$router.push({path: '/home/addProduct'})
          }
        }
    }
</script>

<style scoped>
.add_product {
  float: left;
}
</style>
