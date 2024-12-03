<template>
  <div>
    <div style="width: 100%; height: 100vh; overflow: hidden" class="bgImg">
      <div style="width: 500px; height: 420px; background-color:rgba(9, 50, 113 ,0.2); border-radius: 10px;
        margin: 150px auto;">

        <div style="width: 260px; margin: 0 auto; padding-top: 30px">
          <div class="item" style="font-size: 20px; color: white">注册</div>
          <div class="item">
            <input type="text" v-model="user.name" style="width: 100%; padding: 10px; border-radius: 5px;" placeholder="请输入姓名">
          </div>
          <div class="item">
            <input type="text" v-model="user.username" style="width: 100%; padding: 10px; border-radius: 5px;" placeholder="请输入用户名">
          </div>
          <div class="item">
            <input v-model="user.phone"  style="width: 100%; padding: 10px; border-radius: 5px; box-sizing:border-box;"  placeholder="请输入手机号">
          </div>
          <div class="item">
            <input type="password" v-model="user.password"  style="width: 100%; padding: 10px; border-radius: 5px; box-sizing:border-box;"  placeholder="请输入密码">
          </div>
          <div class="item">
            <button style="background: #049d04; border-radius: 5px; color: white; width: 100%; padding: 10px; cursor: pointer" @click="register">注册</button>
          </div>
          <div style="padding: 10px 0; text-align: right">
            <span style="cursor: pointer; color: #049d04" @click="$router.push('/login')">去登录</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import API from "@/utils/request";

export default {
  name: "Register",
  data() {
    return {
      user: {}
    }
  },
  methods: {
    register() {
      if (!this.user.name) {
        this.$message({
          type: "error",
          message: "请输入姓名"
        })
        return
      }
      if (!this.user.username) {
        this.$message({
          type: "error",
          message: "请输入用户名"
        })
        return
      }
      if (!this.user.phone) {
        this.$message({
          type: "error",
          message: "请输入手机号"
        })
        return
      }
      if (!this.user.password) {
        this.$message({
          type: "error",
          message: "请输入密码"
        })
        return
      }

      API.post("/manage/user/create", this.user).then(res => {
        if (res.code === 0) {
          this.$message({
            type: "success",
            message: "注册成功"
          })
          this.$router.replace("/login")
        } else {
          this.$message({
            type: "error",
            message: res.msg
          })
        }
      })
    }
  }
}
</script>

<style scoped>
  .bgImg {
    background: url("../assets/bg.jpg") no-repeat;
    background-size: 100% 100vh;
  }
  .item {
    text-align: center;
    padding: 10px 0
  }
</style>
