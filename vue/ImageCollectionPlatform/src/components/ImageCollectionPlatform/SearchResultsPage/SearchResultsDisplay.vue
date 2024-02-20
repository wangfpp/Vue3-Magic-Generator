<template>
  <FilterOptions @search="search" :artist_id="query.artist_id" :category_id="query.category_id"/>
  <SearchBar @search="search" :title="query.title"/>
  <div class="search-results">
    <el-row :gutter="20">
      <el-col :span="6" v-for="(item, index) in searchResults" :key="index">
        <el-card :body-style="{ padding: '0px', cursor: 'pointer'}" @click="toDetail(item)">
          <img :src="item.images?item.images[0].url:''" class="image" alt="搜索结果图片">
          <div style="padding: 14px;">
            <span class="title">{{ item.title }}</span>
            <div class="info">
              <el-tag size="small">{{ item.artists?.name }}</el-tag>
            </div>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
  <Pagination
      @current-change="handleCurrentChange"
      :current-page="currentPage"
      :page-size="pageSize"
      layout="prev, pager, next"
      :total="pageTotal"/>
</template>

<script setup>
import {inject, ref} from 'vue';
import Pagination from "@/components/ImageCollectionPlatform/SearchResultsPage/Pagination.vue";
import {useRoute, useRouter} from "vue-router";
import SearchBar from "@/components/ImageCollectionPlatform/SearchResultsPage/SearchBar.vue";
import FilterOptions from "@/components/ImageCollectionPlatform/SearchResultsPage/FilterOptions.vue";

const route = useRoute()
const router = useRouter()
const axios = inject('$axios')
const currentPage = ref(1)
const pageTotal = ref(0)
const pageSize = ref(20)
const query = ref({
  category_id: route.query['category_id'],
  artist_id: route.query['artist_id'],
  title: route.query['title']
})

// 假设的搜索结果数据，实际应用中应从后端获取
const searchResults = ref([]);

const handleCurrentChange = (e) => {
  axios.post(`/common/image_collection/page`, {page: e, ...query.value}).then(res => {
    searchResults.value = res.data.items
    currentPage.value = res.data.page
    pageTotal.value = res.data.total
  })
}

handleCurrentChange(1)

const search = (e)=>{
  query.value = {...query.value, ...e}
  handleCurrentChange(1)
}

const toDetail = (e)=>{
  router.push({path: "/ImageCollectionPlatform/CollectionDetailsPage", query: {id: e.id}})
}

</script>

<style scoped>
.search-results {
  padding: 20px;
  background-color: #f0ead6;
}

.image {
  width: 100%;
  border-bottom: 1px solid #c8b7a1;
}

.title {
  color: #5c3a21;
  font-weight: bold;
}

.info {
  margin-top: 10px;
}

.el-card {
  border: 1px solid #c8b7a1;
  background-color: #fdf6e3;
}

.el-tag {
  border-color: #c8b7a1;
  background-color: #dcd0c0;
  color: #5c3a21;
}

.el-row {
  margin-bottom: 20px;
}

.el-col {
  display: flex;
  justify-content: center;
}
</style>