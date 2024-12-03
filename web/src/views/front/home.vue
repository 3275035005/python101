<template>
  <div>
    <div style="margin-top: 10px">
      <el-carousel height="400px">
        <el-carousel-item v-for="item in banner" :key="item.id">
          <a target="_blank" :href="item.image"><img style="width: 100%" :src='item.image' alt=""></a>
        </el-carousel-item>
      </el-carousel>
    </div>

    <!--    其他-->
    <div style="margin-top: 10px">
      <el-card>
        <el-row :gutter="10">
          <!--          分类-->
<!--          <el-col :span="4">-->
<!--            <div style="border: 1px dashed #ccc; text-align: center; border-bottom: none">-->
<!--              <div class="category-item" @click="getGoodsByCategory(item.id)" v-for="item in categories" :key="item.id"-->
<!--                   :class="{ active: (activeIndex === item.id)}">{{item.name }}-->
<!--              </div>-->
<!--            </div>-->
<!--          </el-col>-->

          <el-col :span="20">
            <div style="min-height: 150px">
              <el-row :gutter="10">
                <el-col :span="6" v-for="item in tableData" :key="item.id">
                  <div style="margin-bottom: 10px; cursor: pointer"  @click="goodsDetail(item.id)">
                    <div style="padding: 5px"><el-image :src="item.image" style="width: 100%; height: 100px" fit="contain"></el-image></div>
                    <div style="padding: 5px; height: 20px; text-align: center; font-size: 12px; overflow: hidden">
                      <el-tooltip :content="item.name" placement="bottom" effect="light">
                        <span class="item-title">{{ item.name }}</span>
                      </el-tooltip>
                    </div>
                  </div>
                </el-col>
              </el-row>
            </div>

            <!--      分页-->
            <div style="margin-top: 20px">
              <el-pagination
                  small
                  @size-change="handleSizeChange"
                  @current-change="handleCurrentChange"
                  :current-page="pageNum"
                  :page-size="pageSize"
                  :page-sizes="[4, 8, 12]"
                  layout=" prev, pager, next"
                  :total="total"
              >
              </el-pagination>
            </div>

          </el-col>
        </el-row>
      </el-card>

    </div>



  </div>
</template>

<script>
import API from "@/utils/request";

const url = "/api/video/"

export default {
  name: "Home",
  data() {
    return {
      tableData: [],
      activeIndex: 1,
      user: {},
      categories: [],
      pageNum: 1,
      pageSize: 8,
      total: 0,
      banner:[]
    };
  },
  created() {
    this.user = sessionStorage.getItem("user") ? JSON.parse(sessionStorage.getItem("user")) : {}
    this.load();
    this.loadTable()
  },
  methods: {
    goodsDetail(id) {
      this.$router.replace({path: '/front/chargingStation', query: {id: id}})
    },

    load() {
      API.get("front/banner/get_list").then(res => {
        this.banner = res.data
      })
    },
    loadTable() {
      API.get("front/chargingStation/list_api", {params: {page: this.pageNum}}).then(res => {
        this.tableData = res.data.list
        this.total = res.data.total
      })
    },

    handleSizeChange(pageSize) {
      this.pageSize = pageSize;
      this.loadTable()
    },
    handleCurrentChange(pageNum) {
      this.pageNum = pageNum;
      this.loadTable()
    }
  },
};
</script>

<style scoped>
.active {
  color: red !important;
}

.category-item {
  padding: 5px 0;
  border-bottom: 1px dashed #ccc;
  color: #666;
  cursor: pointer;
}

.line1 {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.item-title {
  cursor: pointer;
}
.item-title:hover {
  color: orangered;
}
</style>
