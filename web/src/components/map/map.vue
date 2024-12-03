<template>
  <div style="display: flex">
    <div style="margin-top: 10px">
      <div>
        <span>搜索地址：</span>
        <el-autocomplete
          v-model="keywords"
          style="width: 300px"
          :fetch-suggestions="querySearchAsync"
          placeholder="请输入内容"
          @select="handleSelect"
        ></el-autocomplete>
<!--        <span style="margin-left: 10px">-->
<!--          <span>经度：{{ form.lng }}</span>-->
<!--          <span style="margin-left: 10px">纬度：{{ form.lat }}</span>-->
<!--          <span>地址：{{form.address}}</span>-->
<!--        </span>-->
<!--        <el-button style="margin-left: 10px" type="danger" size="small" @click="reset">清空</el-button>-->
      </div>
      <div id="container" class="container"></div>
    </div>
  </div>
</template>

<script>
import AMapLoader from "@amap/amap-jsapi-loader";
window._AMapSecurityConfig = {
  // 安全密钥
  securityJsCode: "3a3b6117726d2b4607fe63fcae94f39f",
};
export default {
  name: "HomeView",
  data() {
    return {
      // 地图实例
      map: null,
      // 标记点
      marker: "",
      // 地址逆解析
      geoCoder: null,
      // 搜索提示
      AutoComplete: null,
      //缩放控件
      ToolBar:null,
      //地图放大镜
      HawkEye:null,
      // 搜索关键字
      keywords: "",
      // 位置信息
      form: {
        lng: "116.397755",
        lat: "39.903179",
        address:'',
      },
      // 搜索节流阀
      loading: false,
      // 搜索提示信息
      options: [],
    };
  },
  created() {
    this.initMap();
  },
  methods: {
    reset(){
      this.keywords = '';
      this.form = {
        lng: "116.397755",
        lat: "39.903179",
        address: '',
      }
      // 清除点
      this.removeMarker();
      // 标记点
      this.setMapMarker();
    },
    initMap() {
      AMapLoader.load({
        // 你申请的Key
        key: "d475863950202700a7a0aa3ceff75df3",
        version: "2.0",
        // 需要用到的插件
        plugins: ["AMap.Geocoder", "AMap.AutoComplete","AMap.ToolBar","AMap.HawkEye"],
      })
        .then((AMap) => {
          this.map = new AMap.Map("container", {
            viewMode: "3D", //是否为3D地图模式
            zoom: 23, //初始化地图级别
            center: [this.form.lng, this.form.lat], //初始化地图中心点位置
          });
          //地址逆解析插件
          this.geoCoder = new AMap.Geocoder({
            city: "010", //城市设为北京，默认：“全国”
            radius: 1000, //范围，默认：500
          });
          // 搜索提示插件
          this.AutoComplete = new AMap.AutoComplete({ city: "全国" });
          this.ToolBar =  new AMap.ToolBar({
            position: {
              bottom: '210px',
              right: '35px'
            }
          });
          this.HawkEye =  new AMap.HawkEye({
            position: {
              bottom: '110px',
              left: '35px'
            }
          });
          this.map.addControl(this.ToolBar);
          this.map.addControl(this.HawkEye);
          // 清除点
          this.removeMarker();
          // 标记点
          this.setMapMarker();
          //点击获取经纬度;
          this.map.on("click", (e) => {
            // 获取经纬度
            this.form.lng = e.lnglat.lng;
            this.form.lat = e.lnglat.lat;
            // 清除点
            this.removeMarker();
            // 标记点
            this.setMapMarker();
          });
        })
        .catch((err) => {
          // 错误
        });
    },
    // 标记点
    setMapMarker() {
      // 自动适应显示想显示的范围区域
      this.map.setFitView();
      this.marker = new AMap.Marker({
        map: this.map,
        position: [this.form.lng, this.form.lat],
      });
      // 逆解析地址
      this.toGeoCoder();
      this.map.setFitView();
      this.map.add(this.marker);
    },
    // 清除点
    removeMarker() {
      if (this.marker) {
        this.map.remove(this.marker);
      }
    },
    // 逆解析地址
    toGeoCoder() {
      let lnglat = [this.form.lng, this.form.lat];
      this.geoCoder.getAddress(lnglat, (status, result) => {
        if (status === "complete") {
          this.form.address = result.regeocode.formattedAddress;
        }else {
          this.form.address = '';
        }
        this.$emit('update-project-id', this.form);
      });
    },
    querySearchAsync(queryString, cb){
      if (queryString) {
        this.AutoComplete.search(queryString, (status, result) => {
          if(status === 'complete'){
            this.options = result.tips;
            for (let i = 0; i < this.options.length; i++) {
              this.options[i].value = this.options[i].name;
            }
          }else {
            this.options = [];
          }
          cb(this.options);
        });
      } else {
        this.options = [];
        cb(this.options);
      }
    },
    handleSelect(val){
      // 清空时不执行后面代码
      if (!val) {
        return;
      }
      this.form = {
        lng: val.location.lng,
        lat: val.location.lat,
      };
      // 清除点
      this.removeMarker();
      // 标记点
      this.setMapMarker();
    },
  },
  mounted() {
  },
};
</script>

<style>
.container {
  margin-top: 10px;
  width: 800px;
  height: 720px;
}
</style>
