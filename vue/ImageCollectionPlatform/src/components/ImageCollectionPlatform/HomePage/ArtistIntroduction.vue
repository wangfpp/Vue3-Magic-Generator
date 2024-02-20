<template>
  <section class="artist-introduction">
    <div class="title">
      <h2>艺人介绍</h2>
    </div>
    <div class="artist-container">
      <div class="artist-item" v-for="(artist, index) in artists" :key="index" @click="linkTo">
        <el-image :src="artist.artists_url" fit="cover" class="artist-photo"></el-image>
        <div class="artist-info">
          <h3>{{ artist.name }}</h3>
          <p>{{ artist.bio }}</p>
          <el-button type="text">查看更多</el-button>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import {inject, ref} from 'vue';
import {useRouter} from "vue-router";
const router = useRouter()
const linkTo = function () {
  router.push({path: "/ImageCollectionPlatform/ArtistMaintenancePage"})
}

const artists = ref([
]);


const axios = inject('$axios')

axios.post(`/common/artist/page`, {orderby: [{"column": "id", "sort": 'desc'}]}).then(res => {
  artists.value = res.data.items
})
</script>

<style scoped>
.artist-introduction {
  background-color: #f0ebe3;
  padding: 20px;
  font-family: 'Times New Roman', Times, serif;
}

.title h2 {
  color: #5c3a21;
  text-align: center;
}

.artist-container {
  display: flex;
  justify-content: space-around;
  flex-wrap: wrap;
  margin-top: 20px;
}

.artist-item {
  cursor: pointer;
  width: 30%;
  margin-bottom: 20px;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  transition: 0.3s;
}

.artist-item:hover {
  box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
}

.artist-photo {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.artist-info {
  padding: 10px;
  text-align: center;
}

.artist-info h3 {
  color: #5c3a21;
  margin: 10px 0;
}

.artist-info p {
  color: #5c3a21;
  font-size: 14px;
}

.el-button {
  color: #5c3a21;
  border-color: #5c3a21;
}
</style>