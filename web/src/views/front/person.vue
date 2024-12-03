<template>
  <div style="margin-top: 10px">
    <el-row>
      <el-col :span="24">
        <el-card>
          <div style="padding: 10px 0; border-bottom: 1px solid #ccc; display: flex">
            <div style="flex: 1;font-size: 18px">个人信息</div>
            <div style="flex: 1; text-align: right">
              <el-button @click="recharge">充值</el-button>
              <el-button @click="edit">修改</el-button>
            </div>
          </div>
          <el-row>
            <el-col :span="12" :offset="10">


              <div style="padding: 10px 0; margin-top: 20px">
                <div style="padding-left: 40px">
                  <el-upload
                      ref="upload"
                      :multiple="false"
                      :before-upload="beforeUpload"
                      action="#"
                      class="avatar-uploader"
                  >
                    <img v-if="imageUrl" :src="imageUrl" class="avatar">
                    <i v-else class="el-icon-plus avatar-uploader-icon" />
                  </el-upload>
                </div>

                <el-form label-width="100px">
                  <el-form-item label="用户名：" >
                    <div>{{ userInfo.username }}</div>
                  </el-form-item>
                  <el-form-item label="姓名：">
                    <div>{{ userInfo.name }}</div>
                  </el-form-item>
                  <el-form-item label="电话：">
                    <div>{{ userInfo.phone }}</div>
                  </el-form-item>
                  <el-form-item label="账户余额：">
                    <div>￥ {{ userInfo.account }}</div>
                  </el-form-item>
                </el-form>
              </div>

            </el-col>
          </el-row>

        </el-card>
      </el-col>
    </el-row>


    <el-dialog title="个人信息" :visible.sync="dialogFormVisible" width="30%"
               :close-on-click-modal="false" :close-on-press-escape="false" :show-close="false">
      <el-form :model="entity">
        <el-form-item label="姓名" label-width="100px">
          <el-input v-model="entity.name" autocomplete="off" style="width: 80%"></el-input>
        </el-form-item>
        <el-form-item label="电话" label-width="100px">
          <el-input v-model="entity.phone" autocomplete="off" style="width: 80%"></el-input>
        </el-form-item>
        <el-form-item label="用户名" label-width="100px">
          <el-input v-model="entity.username" autocomplete="off" style="width: 80%"></el-input>
        </el-form-item>
        <el-form-item label="密码" label-width="100px">
          <el-input show-password v-model="entity.password" autocomplete="off" style="width: 80%"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="save">确 定</el-button>
      </div>
    </el-dialog>

    <el-dialog title="充值" :visible.sync="vis" width="30%"
               :close-on-click-modal="false" :close-on-press-escape="false" :show-close="false">
      <el-form>
        <el-form-item label="金额" label-width="100px">
          <el-input v-model="money" autocomplete="off" style="width: 80%"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="vis = false">取 消</el-button>
        <el-button type="primary" @click="doRecharge">确 定</el-button>
      </div>
    </el-dialog>

  </div>
</template>

<script>
import API from '../../utils/request'

export default {
  name: "User",
  data() {
    return {
      user: {},
      userInfo: {},
      entity: {},
      dialogFormVisible: false,
      vis: false,
      imageUrl:'',
      money: 0
    };
  },
  created() {
    this.user = sessionStorage.getItem("user") ? JSON.parse(sessionStorage.getItem("user")) : {}
    this.load()
  },
  methods: {
    doRecharge() {
      API.post("front/user/rechargeAccount",{
        id: this.user.id,
        account: this.money
      }).then(res => {
        if (res.code === 0) {
          this.$message({
            type: "success",
            message: "充值成功"
          })
          this.load()
        } else {
          this.$message({
            type: "error",
            message: res.msg
          })
        }
        this.vis = false;
      })
    },
    recharge() {
      this.vis = true
      this.money = 0
    },
    load() {
      API.get('front/user/info?id='+ this.user.id).then(res => {
        this.userInfo = res.data || {}
        this.imageUrl =  res.data.avatar
      })
    },
    save() {
      API.post('front/user/update', this.entity).then(res => {
        if (res.code === 0) {
          this.$message({
            type: "success",
            message: "修改成功"
          })
          this.dialogFormVisible = false;
          this.load()
        }
      })
    },
    beforeUpload(file) {
      // 改封面文件名
      const fileName = new Date().getTime().toString() + '.' + file.type.substring(6)
      const formData = new FormData();
      formData.append("image", new File([file], fileName))
      API.post(`manage/file/upload`, formData)
          .then(response => { // 请求成功
            this.imageUrl = response.data

            this.entity.avatar = response.data
            this.entity.id = this.user.id
            this.save()
            this.$refs.upload.clearFiles() // 去掉文件列表
          })
    },
    edit() {
      this.entity = this.userInfo
      this.dialogFormVisible = true;
    },

  },
};
</script>

<style scoped>
.avatar-uploader .el-upload {
  border: 1px dashed #d9d9d9;
  border-radius: 6px;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}

.avatar-uploader .el-upload:hover {
  border-color: #409EFF;
}

.avatar-uploader-icon {
  font-size: 28px;
  color: #8c939d;
  width: 100px;
  height: 100px;
  line-height: 100px;
  text-align: center;
}

.avatar {
  width: 100px;
  height: 100px;
  display: block;
}

.el-form-item {
  margin-bottom: 10px;
}
</style>
