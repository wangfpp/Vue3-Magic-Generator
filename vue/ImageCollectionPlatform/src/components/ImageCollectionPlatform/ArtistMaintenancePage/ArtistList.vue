<template>
  <div class="artist-list">
    <el-input v-model="search" placeholder="搜索艺人..." clearable @clear="fetchArtists"
              @input="fetchArtists"></el-input>
    <el-row :gutter="20">
      <el-col :span="6" v-for="artist in filteredArtists" :key="artist.id">
        <el-card :body-style="{ padding: '20px' }">
          <div class="image-container">
            <img :src="artist.artists_url" class="artist-image" alt="艺人照片">
          </div>
          <div style="margin-top: 20px;">
            <h3>{{ artist.name }}</h3>
            <div class="artist-info">{{ artist.bio }}</div>
          </div>
        </el-card>
      </el-col>
    </el-row>
  </div>
</template>

<script setup>
import {computed, inject, ref} from 'vue';

const search = ref('');
const artists = ref([]);
const axios = inject('$axios')

axios.post(`/common/artist/query`, {}).then(res => {
  artists.value = res.data
})

const filteredArtists = computed(() => {
  if (!search.value) {
    return artists.value;
  }
  return artists.value.filter((artist) => artist.name.includes(search.value) || artist.category.includes(search.value));
});

const fetchArtists = () => {
  // 这里可以实现获取艺人列表的逻辑，目前使用静态数据
};
</script>

<style scoped>
.artist-list {
  padding: 20px;
}

.image-container {
  height: 180px;
  overflow: hidden;
  display: flex;
  justify-content: center;
  align-items: center;
}

.artist-image {
  width: 100%;
  height: auto;
  transition: transform .3s ease;
}

.el-card:hover .artist-image {
  transform: scale(1.1);
}

.artist-info {
  color: #7a6248;
  font-size: 14px;
}

.el-input {
  margin-bottom: 20px;
}
</style>