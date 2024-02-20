<template>
  <div class="collection-title-description-wrapper">
    <h1 class="collection-title">{{form.title}}</h1>
    <p class="collection-description">
      {{form.description}}
    </p>
  </div>
  <div class="image-display-wrapper">
    <el-row :gutter="20">
      <el-col :span="6" v-for="(image, index) in images" :key="index">
        <el-image
          :src="image.url"
          fit="cover"
          class="image-item"
          @click="handleImageClick(image)"
        ></el-image>
      </el-col>
    </el-row>
    <el-dialog :visible.sync="dialogVisible" :before-close="handleClose">
      <img :src="currentImage" class="full-image" alt="查看图片" />
    </el-dialog>
  </div>

   <div class="artist-information-wrapper">
    <el-card class="box-card" shadow="hover">
      <div slot="header" class="clearfix">
        <span>艺人信息</span>
      </div>
      <div class="artist-details">
        <el-row :gutter="20">
          <el-col :span="8">
            <el-image
              :src="artists.artists_url"
              fit="cover"
              class="artist-image"
            ></el-image>
          </el-col>
          <el-col :span="16">
            <p class="artist-name">艺人姓名: {{artists.name}}</p>
            <p class="artist-intro" v-html="artists.bio"></p>
<!--            <p class="artist-works">代表作品:《红高粱》《活着》《英雄》等。</p>-->
          </el-col>
        </el-row>
      </div>
    </el-card>
  </div>
</template>

<script setup>
import {useRoute} from "vue-router";
import {inject, ref} from "vue";
import {ElCard, ElCol, ElImage, ElRow} from "element-plus";

const form = ref({})
const artists = ref({})
const route = useRoute()
const axios = inject('$axios')
axios.post(`/common/image_collection/query`, {id: route.query['id']}).then(res => {
    form.value = res.data[0]
    images.value = form.value.images
    artists.value = form.value.artists
})


const images = ref([]);

const dialogVisible = ref(false);
const currentImage = ref('');

const handleImageClick = (image) => {
  currentImage.value = image;
  dialogVisible.value = true;
};

const handleClose = () => {
  dialogVisible.value = false;
};
</script>

<style scoped>
.collection-title-description-wrapper {
  padding: 20px;
  background-color: #f0ead6;
  color: #5c3a21;
  text-align: center;
}

.collection-title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 10px;
  color: #5c3a21;
}

.collection-description {
  font-size: 16px;
  color: #5c3a21;
}


.image-display-wrapper {
  padding: 20px;
  background-color: #f0ead6;
}

.image-item {
  width: 100%;
  border-radius: 5px;
  cursor: pointer;
  transition: transform 0.3s ease;
}

.image-item:hover {
  transform: scale(1.05);
}

.full-image {
  width: 100%;
}

.artist-information-wrapper {
  padding: 20px;
  background-color: #f0ead6;
}

.box-card {
  border-radius: 5px;
}

.artist-details {
  font-family: 'Courier New', Courier, monospace;
  color: #333;
}

.artist-image {
  width: 100%;
  border-radius: 5px;
}

.artist-name,
.artist-intro,
.artist-works {
  margin-bottom: 10px;
}

.artist-name {
  font-size: 20px;
  font-weight: bold;
}

.artist-intro,
.artist-works {
  text-indent: 2em;
}
</style>