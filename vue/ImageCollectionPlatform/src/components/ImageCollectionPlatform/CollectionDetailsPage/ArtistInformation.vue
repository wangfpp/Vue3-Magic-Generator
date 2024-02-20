<template>
  <div class="artist-information-wrapper">
    <el-card class="box-card" shadow="hover">
      <div slot="header" class="clearfix">
        <span>艺人信息</span>
      </div>
      <div class="artist-details">
        <el-row :gutter="20">
          <el-col :span="8">
            <el-image
              src="https://img.freepik.com/free-photo/painting-mountain-lake-with-mountain-background_188544-9126.jpg?t=st=1708270215~exp=1708270815~hmac=2a7f8612030cfed42d687cd669880a67812c6e4bca7ae61f70125c6af2e71a17"
              fit="cover"
              class="artist-image"
            ></el-image>
          </el-col>
          <el-col :span="16">
            <p class="artist-name">艺人姓名: 张艺谋</p>
            <p class="artist-intro">简介: 张艺谋，中国著名电影导演，其作品多次获得国际奖项。</p>
            <p class="artist-works">代表作品:《红高粱》《活着》《英雄》等。</p>
          </el-col>
        </el-row>
      </div>
    </el-card>
  </div>
</template>

<script setup>
import { ElCard, ElRow, ElCol, ElImage } from 'element-plus';
</script>

<style scoped>
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