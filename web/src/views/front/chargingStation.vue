<template>
  <div>

    <div style="margin-top: 10px">
      <!--      充电桩-->
      <el-row :gutter="10">
        <!--    图片-->
        <el-col :span="8">
          <el-card>
            <div >
              <el-image :src="chargingStation.image" style="width: 400px; height: 400px"></el-image>
            </div>
          </el-card>
        </el-col>

        <!--    充电站描述-->
        <el-col :span="16">
          <el-card>

            <div style="padding: 10px 0; font-size: 20px; font-weight: bold">{{ chargingStation.name }}</div>
            <div style="padding: 10px 0; color: #666; font-size: 14px">{{ chargingStation.description }}</div>
            <div style="padding: 10px 0; color: #999;">
              <span>营业时间</span>
              <span style="margin-left: 20px; color: #666">{{ chargingStation.start_time}}-{{chargingStation.end_time}}</span>
            </div>

            <div style="padding: 10px 0">
              <span style="color: #999">地址</span>
              <span style="margin-left: 20px; color: #666;"> {{ chargingStation.address }}</span>
            </div>

            <div style="padding: 10px 0">
              <FrontMap :parent-longitude="chargingStation.longitude" :parent-latitude="chargingStation.latitude"/>
            </div>
          </el-card>
        </el-col>

      </el-row>
      <!--      充电桩-->
      <el-row>
        <el-col :span="24">
          <div style="margin-top: 10px; margin-bottom: 80px">
            <el-card>
              <div style="padding-bottom: 10px; margin-bottom: 20px; border-bottom: 2px solid orangered; font-size: 20px">充电桩列表</div>
              <div style="margin-left: 20px;text-align: center">
                <ul style="  position: relative;list-style: none; margin: 0;padding: 0;">
                  <li
                      v-for="item in chargingStation.station_id"
                      :key="item.id">
                    <div v-if="item.state === '2'" style=" position: relative; float: left;font-size: 20px;margin: 10px 0;padding: 10px;height: 70px;width: 100%;border: 1px solid #DDD;" @click="buyNow">
                      <div style="position: absolute;top: 0;left: 0; background-color: #049d04">{{item.type === '1'?'快充':'慢充'}}</div>
                      <div> {{ item.number }}</div>
                      <div> 正常 </div>
                    </div>
                    <div  v-else style="background-color: red;float: left;font-size: 20px;margin: 10px 0;padding: 10px;height: 70px;width: 100%;border: 1px solid #DDD;">
                    <div> {{ item.number }}</div>
                      <div> 占用 </div>
                    </div>
                  </li>
                </ul>
              </div>
            </el-card>
          </div>
        </el-col>
      </el-row>

    </div>
  </div>
</template>

<script>
import API from "@/utils/request";
import FrontMap from '@/components/map/frontMap.vue'
export default {
  components: {
    FrontMap
  },
  name: "chargingStation",
  data() {
    return {
      dialogFormVisible: false,
      entity: {},
      id: 1,
      user: {},
      chargingStation: {

      },
      praiseFlag: false
    };
  },
  created() {
    this.id = this.$route.query.id
    this.load()
  },
  methods: {

    buyNow() {
      this.$router.replace("/front/preOrder/" + this.chargingStation.id)
    },
    cancel() {
      this.dialogFormVisible = false;
      this.entity = {};
    },
    load() {
      API.get("front/chargingStation/get_detail?id=" + this.id).then(res => {
        this.chargingStation = res.data
      })
    },
  },
};
</script>

<style scoped>
.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}

.clearfix:after {
  clear: both
}
</style>
