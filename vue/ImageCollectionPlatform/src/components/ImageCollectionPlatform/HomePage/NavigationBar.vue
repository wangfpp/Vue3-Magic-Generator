<template>
  <nav class="navigation-bar">
    <div class="logo">
      <img src="@/assets/logo.png" alt="Logo" class="logo-image">
    </div>
    <ul class="nav-links">
      <li><a href="/ImageCollectionPlatform/HomePage">首页</a></li>
      <li><a href="/ImageCollectionPlatform/SearchResultsPage">图片集推荐</a></li>
      <li><a href="/ImageCollectionPlatform/ArtistMaintenancePage">艺人介绍</a></li>
      <li><a href="/ImageCollectionPlatform/UploadPage">发布图片集</a></li>
    </ul>
    <div class="user-actions">
      <el-button type="text" @click="handleLogin">登录</el-button>
      <el-button type="text" @click="handleRegister">注册</el-button>
    </div>
  </nav>
</template>

<script setup>
import { ElButton } from 'element-plus';
import {useRouter} from "vue-router";
const router = useRouter()
const handleLogin = () => {
  router.push({path: "/ImageCollectionPlatform/UserLoginPage"})
  console.log('Login modal should appear');
};

const handleRegister = () => {
  router.push({path: "/ImageCollectionPlatform/UserRegistrationPage"})
  console.log('Register modal should appear');
};
</script>

<style scoped>
.navigation-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #f0ebe3;
  padding: 10px 50px;
  font-family: 'Times New Roman', Times, serif;
}

.logo {
  flex: 1;
}

.logo-image {
  height: 50px;
}

.nav-links {
  flex: 2;
  list-style: none;
  display: flex;
  justify-content: center;
}

.nav-links li {
  margin: 0 15px;
}

.nav-links a {
  text-decoration: none;
  color: #5c3a21;
  font-size: 16px;
}

.user-actions {
  flex: 1;
  display: flex;
  justify-content: flex-end;
}

.el-button {
  color: #5c3a21;
  border-color: #5c3a21;
}

.el-button:hover {
  color: #3e2714;
  border-color: #3e2714;
}
</style>