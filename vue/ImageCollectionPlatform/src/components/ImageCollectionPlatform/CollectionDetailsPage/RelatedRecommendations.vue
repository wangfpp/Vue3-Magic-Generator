<template>
  <div class="related-recommendations-wrapper">
    <el-carousel :interval="5000" arrow="always">
      <el-carousel-item v-for="(item, index) in recommendations" :key="index">
        <div class="recommendation-content">
          <img :src="item.imgUrl" class="recommendation-img" alt="推荐内容图片">
          <div class="recommendation-info">
            <h3>{{ item.title }}</h3>
            <p>{{ item.description }}</p>
          </div>
        </div>
      </el-carousel-item>
    </el-carousel>
  </div>
</template>

<script setup>
import { ElCarousel, ElCarouselItem } from 'element-plus';
import { ref } from 'vue';

const recommendations = ref([
  {
    title: '精选图片集',
    description: '探索精选的高质量图片集，丰富你的视觉体验。',
    imgUrl: 'https://img.freepik.com/free-photo/painting-mountain-lake-with-mountain-background_188544-9126.jpg?t=st=1708270260~exp=1708270860~hmac=ef879dc8996977386db54ceb08f8a56481bf2111e980821cd4416cfee4451b59',
  },
  {
    title: '艺术家专访',
    description: '深入了解艺术家的创作灵感与背后故事。',
    imgUrl: 'https://img.freepik.com/free-vector/vector-realistic-light-flares-laser-beams_134830-1802.jpg?t=st=1708270260~exp=1708270860~hmac=dba3917ef4ccdb8359884696bd7af243bc5fafa106bbdda3f4fb2c2814515db8',
  },
  {
    title: '新作发布',
    description: '最新发布的图片集，带给你前所未有的视觉享受。',
    imgUrl: 'https://img.freepik.com/free-photo/majestic-mountain-peak-tranquil-winter-landscape-generated-by-ai_188544-15662.jpg?t=st=1708270260~exp=1708270860~hmac=3c79c1de73875a4f20cdff9d2cd2e6a1243da56a945cad0830826fe8daa4cf79',
  }
]);
</script>

<style scoped>
.related-recommendations-wrapper {
  padding: 20px;
  background-color: #f0ead6;
}

.recommendation-content {
  display: flex;
  align-items: center;
  justify-content: center;
}

.recommendation-img {
  width: 100px;
  height: 100px;
  object-fit: cover;
  margin-right: 20px;
  border-radius: 10px;
}

.recommendation-info h3 {
  font-family: 'Courier New', Courier, monospace;
  font-size: 18px;
  color: #333;
}

.recommendation-info p {
  font-family: 'Courier New', Courier, monospace;
  font-size: 14px;
  color: #555;
}
</style>