<template>
  <div style="display: flex">
    <div style="margin-top: 10px">
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
  props: {
    parentLongitude: {
      type: Number,
      default: 0
    },
    parentLatitude: {
      type: Number,
      default: 0
    }
  },
  data() {
    return {
      // 地图实例
      map: null,
      // 标记点
      marker: "",
    };
  },
  created() {
    console.log(this.parentLongitude)
    console.log(this.parentLatitude)
    this.initMap();
  },
  methods: {

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
            center: [this.parentLongitude, this.parentLatitude], //初始化地图中心点位置
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
        })
        .catch((err) => {
          // 错误
        });
    },
    // 清除点
    removeMarker() {
      if (this.marker) {
        this.map.remove(this.marker);
      }
    },
    // 标记点
    setMapMarker() {
      // 自动适应显示想显示的范围区域
      this.map.setFitView();
      this.marker = new AMap.Marker({
        map: this.map,
        position: [this.parentLongitude, this.parentLatitude],
      });
      // 逆解析地址
      this.toGeoCoder();
      this.map.setFitView();
      this.map.add(this.marker);
    },

  },
  mounted() {

  },
};
</script>

<style>
.container {
  width: 900px;
  height: 250px;
}
</style>
