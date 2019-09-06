<template>
  <div>
    <el-dialog
      :title="title"
      :visible.sync="showModal"
      width="50%"
      @close="addDialogClosed">
      <!-- 添加用户的表单 -->
      <el-form :model="addForm" ref="addFormRef" label-width="70px">
        <el-form-item label="产品名称" prop="username">
          <el-input v-model="addForm.productname"></el-input>
        </el-form-item>
        <el-form-item label="密码" prop="password">
          <el-input v-model="addForm.productdesc"></el-input>
        </el-form-item>
        <el-form-item label="邮箱" prop="email">
          <el-input v-model="addForm.productuser"></el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="addDialogClosed">取 消</el-button>
        <el-button type="primary" @click="addUser">确 定</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
    export default {
        props: {
            title: {
                type: String,
                default: '添加用户'
            },
            show: {
                type: Boolean,
                default: false
            },
            addForm: {
                type: Object,
                default: () => {
                }
            },
            sign: {
                type: String,
                default: 'add'
            }
        },
        computed: {
            showModal: {
                get() {
                    return this.show
                },
                set(val) {
                }
            }
        },
        methods: {
            async addUser() {
                const { id, productname, productdesc,productuser} = this.addForm
                if (this.sign === 'add') {
                    const res = await this.$http.post('add_product/', {
                        product_name: productname,
                        product_desc: productdesc,
                        product_user: productuser,
                    })
                    console.log(res, 'aaaaa')
                    const {code, product_name, msg} = res.data
                    if (code === 201) {
                        this.$message.success('添加成功')
                        this.addDialogClosed()
                    }else {
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
                        this.$message.success('编辑成功')
                        this.addDialogClosed()
                    } else {
                        this.$message.warning(product_name[0])
                    }
                }
            }
            ,
            addDialogClosed() {
                this.$emit('close')
            },
        }
    }
</script>
