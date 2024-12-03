<template>
  <div style="margin-top: 10px">
    <el-button type="primary" icon="el-icon-search" @click="edit" style="margin: 10px 0 10px 0">提交反馈</el-button>
    <el-table :data="tableData" stripe style="width: 100%" border :header-cell-style="{'text-align':'center'}"  :cell-style="{ textAlign: 'center' }">
      <el-table-column label="反馈内容" prop="content"></el-table-column>
      <el-table-column label="反馈时间" prop="create_time"></el-table-column>
      <el-table-column label="处理状态" prop="state">
        <template slot-scope="scope">
          <el-tag type="warning" v-if="scope.row.state === '0'">未处理</el-tag>
          <el-tag type="primary" v-if="scope.row.state === '1'">已处理</el-tag>
        </template>
      </el-table-column>
      <el-table-column label="处理结果" prop="handle_content"></el-table-column>
      <el-table-column label="处理时间" prop="handle_time"></el-table-column>
    </el-table>

    <el-dialog title="提交反馈" :visible.sync="dialogFormVisible" width="30%"
               :close-on-click-modal="false" :close-on-press-escape="false" :show-close="false">
      <el-form>
        <el-form-item label="反馈内容" label-width="100px">
          <el-input type="textarea" :rows="4" v-model="content" autocomplete="off" style="width: 80%"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="save">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import API from "@/utils/request";

export default {
  name: "cart",
  data() {
    return {
      tableData: [],
      state: '0',
      dialogFormVisible: false,
      content: '',
      user: {}
    }
  },
  created() {

    this.user = sessionStorage.getItem("user") ? JSON.parse(sessionStorage.getItem("user")) : {}
    this.load()
  },
  methods: {

    edit() {
      this.content = "";
      this.dialogFormVisible = true;
    },


    save() {
      API.post('front/feedback/create', {
        state:'0',
        content: this.content,
        user: this.user.id
      }).then(res => {
        this.dialogFormVisible = false;
        if (res.code === 0) {
          this.$message({
            type: "success",
            message: "反馈成功"
          })

          this.load()
        }else{
          this.$message({
            type: "error",
            message: res.msg
          })
        }
      })
    },


    load() {
      API.get(`front/feedback/list_api?userId=`+this.user.id).then(res => {
        this.tableData = res.data
      })
    },

  }
}
</script>

<style scoped>
  .demo-table-expand {
    font-size: 0;
  }

  .demo-table-expand label {
    width: 90px;
    color: #99a9bf;
  }

  .demo-table-expand .el-form-item {
    margin-right: 0;
    margin-bottom: 0;
    width: 50%;
  }
</style>
