<template>
  <div style="margin-top: 10px">
    <!--    全部-->
    <el-tabs v-model="activeName" @tab-click="handleClick">
      <el-tab-pane label="全部订单" name="all">
        <el-table :data="tableData" stripe style="width: 100%"  border :header-cell-style="{'text-align':'center'}"  :cell-style="{ textAlign: 'center' }">
          <el-table-column label="订单号" prop="order_number"  width="200"></el-table-column>
          <el-table-column label="充电桩编号" width="300" prop="number"></el-table-column>
          <el-table-column label="充电时间" prop="hour">
            <template slot-scope="scope">
              {{scope.row.hour}}小时
            </template>
          </el-table-column>
          <el-table-column label="充电时间段" prop="count" width="400">
            <template slot-scope="scope">
              {{scope.row.start_charging_time}}-{{scope.row.end_charging_time}}
            </template>
          </el-table-column>
          <el-table-column label="价格">
            <template slot-scope="scope">
              <span style="color: red">￥ {{ scope.row.money }}</span>
            </template>
          </el-table-column>
          <el-table-column label="状态" prop="state">
            <template slot-scope="scope">
              <span v-if="scope.row.state ==='0'">充电中</span>
              <span v-if="scope.row.state ==='1'">充电完成</span>
            </template>
          </el-table-column>
          <el-table-column
              fixed="right"
              label="操作"
          >
            <template slot-scope="scope">
              <el-button type="danger" @click="cancel(scope.row.id)" v-if="scope.row.state === '0'">取消</el-button>
            </template>
          </el-table-column>
        </el-table>
        <div style="margin-top: 10px">
          <el-pagination
              @size-change="handleSizeChange"
              @current-change="handleCurrentChange"
              :current-page="pageNum"
              :page-size="pageSize"
              :page-sizes="[2, 5, 10]"
              layout="prev, pager, next"
              :total="total"
          >
          </el-pagination>
        </div>
      </el-tab-pane>
      <el-tab-pane label="充电中"  name="0">
        <el-table :data="tableData" stripe style="width: 100%">
          <el-table-column label="订单号" prop="order_number"  width="200"></el-table-column>
          <el-table-column label="充电桩编号" width="300" prop="number"></el-table-column>
          <el-table-column label="充电时间" prop="hour">
            <template slot-scope="scope">
              {{scope.row.hour}}小时
            </template>
          </el-table-column>
          <el-table-column label="充电时间段" prop="count" width="400">
            <template slot-scope="scope">
              {{scope.row.start_charging_time}}-{{scope.row.end_charging_time}}
            </template>
          </el-table-column>
          <el-table-column label="价格">
            <template slot-scope="scope">
              <span style="color: red">￥ {{ scope.row.money }}</span>
            </template>
          </el-table-column>
          <el-table-column
              fixed="right"
              label="操作"
          >
            <template slot-scope="scope">
              <el-button type="danger" @click="cancel(scope.row.id)" v-if="scope.row.state === '0'">取消</el-button>
            </template>
          </el-table-column>
        </el-table>
        <div style="margin-top: 10px">
          <el-pagination
              @size-change="handleSizeChange"
              @current-change="handleCurrentChange"
              :current-page="pageNum"
              :page-size="pageSize"
              :page-sizes="[2, 5, 10]"
              layout="prev, pager, next"
              :total="total"
          >
          </el-pagination>
        </div>
      </el-tab-pane>
      <el-tab-pane label="充电完成" name="1">
        <el-table :data="tableData" stripe style="width: 100%">
          <el-table-column label="订单号" prop="order_number"  width="200"></el-table-column>
          <el-table-column label="充电桩编号" width="300" prop="number"></el-table-column>
          <el-table-column label="充电时间" prop="hour">
            <template slot-scope="scope">
              {{scope.row.hour}}小时
            </template>
          </el-table-column>
          <el-table-column label="充电时间段" prop="count" width="400">
            <template slot-scope="scope">
              {{scope.row.start_charging_time}}-{{scope.row.end_charging_time}}
            </template>
          </el-table-column>
          <el-table-column label="价格">
            <template slot-scope="scope">
              <span style="color: red">￥ {{ scope.row.money }}</span>
            </template>
          </el-table-column>
        </el-table>
        <div style="margin-top: 10px">
          <el-pagination
              @size-change="handleSizeChange"
              @current-change="handleCurrentChange"
              :current-page="pageNum"
              :page-size="pageSize"
              :page-sizes="[2, 5, 10]"
              layout="prev, pager, next"
              :total="total"
          >
          </el-pagination>
        </div>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
import API from "@/utils/request";

export default {
  name: "cart",
  data() {
    return {
      user: {},
      pageNum: 1,
      pageSize: 10,
      total: 0,
      activeName: 'all',
      tableData: [],
    }
  },
  created() {
    this.user = sessionStorage.getItem("user") ? JSON.parse(sessionStorage.getItem("user")) : {}
    if (!this.user.id) {
      this.$message({
        type: 'warning',
        message: '请登录！'
      })
      return
    }
    this.load()
  },
  methods: {
    handleClick(tab, event) {
      this.state = tab.name
      this.load()
    },
    handleSizeChange(pageSize) {
      this.pageSize = pageSize
      this.load()
    },
    handleCurrentChange(pageNum) {
      this.pageNum = pageNum
      this.load()
    },
    load() {
      if(this.state === 'all') {this.state = ''}
      API.get("front/order/list_api", {params: {
        page:this.pageNum,
        state: this.state,
        userId: this.user.id
      }}).then(res => {
        this.tableData = res.data.list
        this.total = res.data.total
      })
    },
    // 取消订单
    cancel(id) {
      API.post("front/order/update", {id: id, state: '1'}).then(res => {
        if (res.code === 0) {
          this.$message({
            type: 'success',
            message: res.msg
          })
        }else{
          this.$message({
            type: 'error',
            message: res.msg
          })

        }
        this.load()
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
