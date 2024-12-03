<template>
  <div style="margin-top: 10px">
    <div style="background-color: white; padding: 10px">
      <div style="padding: 10px; margin-bottom: 20px; border-bottom: 1px solid #eee">
        <div style="font-size: 20px; border-bottom: 2px solid dodgerblue; padding-bottom: 10px; margin-bottom: 20px">
          选择充电时长
        </div>
        <div style="padding: 10px 0; color: #555">
          <el-radio-group v-model="radio">
            <el-radio :label="item.id" v-for="item in priceList" style="border: 1px solid #DDD;padding: 10px;"  @change="handleRadioChange(item.price)">
              <span class="radio-title">
                  <p>{{item.hour}}小时</p>
                  <p>{{item.price}}元</p>
                </span>
            </el-radio>
          </el-radio-group>
        </div>
      </div>
      <div style="margin-top: 10px">
        <div style="background-color: white; padding: 10px">
          <div style="color: red; text-align: right">
            <div>
              <span>总价：</span>
              <span>￥ {{ totalPrice }}</span>
            </div>
            <div style="padding: 10px 0">
              <el-button style="background-color: red; color: white; width: 100px" @click="submitOrder">立即充电</el-button>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import API from "@/utils/request";

export default {
  name: "cart",
  data() {
    return {
      radio:'',
      user: {},
      priceList:[],
      pileId:'',
      totalPrice:''
    }
  },
  created() {
    this.user = sessionStorage.getItem("user") ? JSON.parse(sessionStorage.getItem("user")) : {}
    if (!this.user) {
      this.$message({
        type: "warning",
        message: '请登录！'
      })
      return
    }
    this.pileId = this.$route.params.id
    this.load()
  },
  methods: {
    // 选中的值
    handleRadioChange(price){
      this.totalPrice = price
    },
    submitOrder() {
      if(this.radio == null || this.radio==='' ){
        this.$message({
          type: 'error',
          message: '请输入充电时间'
        })
        return false;
      }
      // 提交订单
      API.post("front/order/charge", {
        pile: this.pileId,
        price_id: this.radio,
        user: this.user.id
      }).then(res => {
        if (res.code === 0) {
          this.$message({
            type: 'success',
            message: '提交成功！'
          })
          this.$router.replace("/front/order")
        } else {
          this.$message({
            type: 'error',
            message: res.msg
          })
        }
      })
    },

    load() {
      API.get("front/chargingPilePrice/list_api?id="+this.pileId).then(res => {
        this.priceList = res.data
      })
    },
  }
}
</script>

<style scoped>
.radio-title {
  display: block; /* 使文本标签占满整行 */
  white-space: normal; /* 允许文本换行 */
  line-height: 1.2; /* 调整行高 */
  max-width: 100px; /* 限制最大宽度，根据需要调整 */
}
</style>
