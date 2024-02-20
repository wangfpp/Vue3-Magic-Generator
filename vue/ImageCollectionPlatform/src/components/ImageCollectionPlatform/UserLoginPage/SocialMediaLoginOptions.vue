<template>
  <div class="social-media-login-container">
    <div class="social-media-login-title">社交媒体登录</div>
    <div class="social-media-buttons">
      <el-button class="social-button facebook" @click="loginWithSocialMedia('Facebook')">Facebook</el-button>
      <el-button class="social-button twitter" @click="loginWithSocialMedia('Twitter')">Twitter</el-button>
      <el-button class="social-button google" @click="loginWithSocialMedia('Google')">Google</el-button>
    </div>
  </div>
</template>

<script setup>
import { ElMessage } from 'element-plus';

const loginWithSocialMedia = (platform) => {
  console.log(`Logging in with ${platform}`);
  // 实际项目中这里应该是调用社交媒体登录接口的逻辑
  ElMessage({
    message: `通过${platform}登录成功`,
    type: 'success',
  });
};
</script>

<style scoped>
.social-media-login-container {
  text-align: center;
  padding: 20px;
  background-color: #f9f5f0;
  border: 1px solid #d3c1ae;
  box-shadow: 0 2px 12px rgba(0,0,0,.1);
  border-radius: 5px;
  margin-top: 20px;
}

.social-media-login-title {
  font-size: 20px;
  color: #7a6248;
  margin-bottom: 20px;
}

.social-media-buttons .social-button {
  margin: 10px;
  background-color: #7a6248;
  border-color: #7a6248;
  color: #fff;
}

.social-media-buttons .social-button:focus, .social-media-buttons .social-button:hover {
  background-color: #9b856a;
  border-color: #9b856a;
}
</style>