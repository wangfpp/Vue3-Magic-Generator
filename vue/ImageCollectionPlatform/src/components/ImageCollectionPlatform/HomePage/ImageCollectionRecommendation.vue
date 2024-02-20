<template>
  <section class="image-collection-recommendation">
    <div class="title">
      <h2>图片集推荐</h2>
    </div>
    <div class="image-collection-container">
      <div class="image-collection-item" v-for="(image, index) in images" :key="index" @click="linkTo(image)">
        <el-image :src="image.images?image.images[0].url:''" fit="cover" class="image-collection-img"></el-image>
        <div class="image-collection-info">
          <h3>{{ image.title }}</h3>
          <p>{{ image.description }}</p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import {inject, ref} from 'vue';
import {useRouter} from "vue-router";
const router = useRouter()
const axios = inject('$axios')
const linkTo = function (e) {
  router.push({path: "/ImageCollectionPlatform/CollectionDetailsPage", query:{id: e.id}})
}
const images = ref([

]);

axios.post(`/common/image_collection/page`, {page: 1, is_top: 1, orderby: [{"column": "is_top", "sort": 'desc'}]}).then(res => {
    images.value = res.data.items
  })


</script>

<style scoped>
.image-collection-recommendation {
  background-color: #f0ebe3;
  padding: 20px;
  font-family: 'Times New Roman', Times, serif;
}

.title h2 {
  color: #5c3a21;
  text-align: center;
}

.image-collection-container {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
  margin-top: 20px;
}

.image-collection-item {
  cursor: pointer;
  width: 30%;
  margin-bottom: 20px;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  transition: 0.3s;
}

.image-collection-item:hover {
  box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
}

.image-collection-img {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.image-collection-info {
  padding: 10px;
  text-align: center;
}

.image-collection-info h3 {
  color: #5c3a21;
  margin: 10px 0;
}

.image-collection-info p {
  color: #5c3a21;
  font-size: 14px;
}
</style>