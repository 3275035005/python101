<template>
  <div class="app-container">
    <header style="background-color: #049d04">
      充电桩管理系统
      <el-dropdown style="float: right;" @command="handleCommand">
        <span class="el-dropdown-link" style="cursor: pointer;color: rgb(255, 255, 255);">
          欢迎你！{{ user.username }}<i class="el-icon-arrow-down el-icon--right"></i>
        </span>
        <el-dropdown-menu slot="dropdown">
          <el-dropdown-item command="person">个人信息</el-dropdown-item>
          <el-dropdown-item command="loginOut">退出登录</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
    </header>
    <div class="main-content">
      <el-menu class="side-menu" :default-active="$route.path" @select="handleMenuSelect">
        <el-menu-item :index="item.path" v-for="item in user.permission" :key="item.path">
          <template slot="title">
            <i :class="['el-icon-' + item.icon]"></i>
            <span>{{ item.name }}</span>
          </template>
        </el-menu-item>
      </el-menu>

      <router-view class="main-container" :key="Math.random()" @call="getMenu"/>
    </div>
  </div>
</template>

<script>


export default {
  name: 'Manage',
  components: {},
  data() {
    return {
      user: {},
      permissions: []
    };
  },
  created() {
    this.getMenu()
  },
  methods: {
    getMenu() {
      this.user = sessionStorage.getItem("user") ? JSON.parse(sessionStorage.getItem("user")) : {}
      this.user.permission = [
        {"id":1,"name":"首页","path":"/manage/home","description":"首页","icon":"s-home"},
        {"id":2,"name":"充电站管理","path":"/manage/chargingStation","description":"充电站管理","icon":"s-goods"},
        {"id":3,"name":"充电桩管理","path":"/manage/chargingChargingPile","description":"充电桩管理","icon":"s-data"},
        {"id":4,"name":"订单管理","path":"/manage/order","description":"订单管理","icon":"s-data"},
        {"id":5,"name":"公告管理","path":"/manage/notice","description":"公告管理","icon":"data-board"},
        {"id":6,"name":"轮播图管理","path":"/manage/banner","description":"轮播图管理","icon":"picture"},
        {"id":7,"name":"用户反馈管理","path":"/manage/feedback","description":"用户反馈管理","icon":"s-data"},
        {"id":8,"name":"用户管理","path":"/manage/user","description":"用户管理","icon":"user-solid"}


        ]
    },
    handleCommand(command) {
      if (command === 'person') {
        this.$router.push('/manage/person');
      }
      if (command === 'loginOut') {
        sessionStorage.removeItem("user")
        this.$router.replace('/login');
      }
    },
    handleMenuSelect(index) {
      this.$router.push(index);
    },
  },
  computed: {},
}
</script>

<style scoped>
.app-container {
  display: flex;
  flex-direction: column;
  height: 100%;
}

header {
  margin-bottom: 3px;
  line-height: 50px;
  padding: 0 16px;
  font-size: 18px;
  font-weight: bold;
  background-color: #fff;
  box-shadow: 0 0 4px 4px #e6e6e6;
}

.main-content {
  flex: 1;
  display: flex;
  flex-direction: row;
}

.main-container {
  margin-left: 3px;
  padding: 10px;
  flex: 1;
  overflow-y: auto;
  background-color: #fff;
}

.side-menu {
  width: 200px;
  height: 100%;

}

.el-menu-item a {
  text-decoration: none;
}

.el-menu-item.is-active a {
  color: #409EFF;
}
</style>
