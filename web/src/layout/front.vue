<template>
  <div>
    <!--    头部-->
    <div style="width: 100%; height: 60px; line-height: 60px; background-color: #049d04">
      <el-row>
        <el-col :span="4">
          <div style="font-size: 20px; font-weight: bold; text-align: center"><a style="color: #FFFFFFFF;" href="/front/home">智慧充电桩系统</a></div>
        </el-col>
        <el-col :span="10">
          <el-menu class="side-menu"
                   background-color="#049d04"
                   text-color="#fff"
                   active-text-color="#ffd04b"
                   :default-active="$route.path" @select="handleMenuSelect" mode="horizontal">
            <el-menu-item index="/front/home">
              首页
            </el-menu-item>
            <el-menu-item index="/front/order">
              我的订单
            </el-menu-item>
            <el-menu-item index="/front/person">
              个人中心
            </el-menu-item>
            <el-menu-item index="/front/feedback">
              反馈中心
            </el-menu-item>
          </el-menu>
        </el-col>
        <el-col :span="6">
          <div v-if="!$route.path.includes('/search')">
            <el-input style="width: 80%" placeholder="请输入充电站名称" v-model="searchText"></el-input>
            <el-button style="margin-left: 5px" @click="search">搜索</el-button>
          </div>
          <div v-else>
            <div style="width: 100px;height: 20px"></div>
          </div>
        </el-col>
        <el-col :span="4">
          <div style="text-align: right; padding-right: 10px" v-if="user.id">
            <el-dropdown style="float: right;" @command="handleCommand">
              <span class="el-dropdown-link" style="cursor: pointer;color: rgb(255, 255, 255);">
                欢迎你！{{ user.username }}<i class="el-icon-arrow-down el-icon--right"></i>
              </span>
              <el-dropdown-menu slot="dropdown">
                <el-dropdown-item command="person">个人信息</el-dropdown-item>
                <el-dropdown-item command="loginOut">退出登录</el-dropdown-item>
              </el-dropdown-menu>
            </el-dropdown>
          </div>
          <div style="text-align: right; padding-right: 10px" v-else>
            <el-button @click="$router.replace('/login')">登录</el-button>
            <el-button @click="$router.replace('/register')">注册</el-button>
          </div>

        </el-col>
      </el-row>
    </div>

    <!-- 主体 -->
    <el-row>
      <el-col :span="16" :offset="4" style="margin-bottom: 80px">
        <router-view />
      </el-col>
    </el-row>

<!--    底部-->
    <div style="height: 60px; width: 100%; background-color: white; padding: 10px 0; position: fixed; bottom: 0">
      <div style="text-align: center">
        Copyright ©智慧充电桩系统
      </div>

    </div>

  </div>
</template>

<script>

export default {
  name: "Front",
  data() {
    return {
      searchText: '',
      user: {}
    }
  },
  created() {
    this.user = sessionStorage.getItem("user") ? JSON.parse(sessionStorage.getItem("user")) : {}
  },
  methods: {
    search() {
      this.$router.replace({path: '/front/search', query: {searchText: this.searchText}})
    },
    handleCommand(command) {
      if (command === 'person') {
        this.$router.push('/front/person');
      }
      if (command === 'loginOut') {
        sessionStorage.removeItem("user")
        this.$router.replace('/login');

      }
    },
    handleMenuSelect(index) {
      console.log(index)
      this.$router.push(index);
    },
  }
}
</script>

<style scoped>

</style>
