<template>
  <nav class="navigation-bar">
    <div class="nav-content">
      <img src="https://img.freepik.com/free-vector/retro-camera-set_460-28.jpg?t=st=1708269735~exp=1708270335~hmac=0acd62ab412a45a84dddf250ca01da344978fff6af938f63b2715a267afed4fc" alt="VintageArt Logo" class="logo">
      <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
        <el-menu-item index="1">主页</el-menu-item>
        <el-menu-item index="2">搜索页面</el-menu-item>
        <el-submenu index="3">
          <template #title>账户管理</template>
          <el-menu-item index="3-1">登录</el-menu-item>
          <el-menu-item index="3-2">注册</el-menu-item>
        </el-submenu>
      </el-menu>
    </div>
  </nav>
</template>

<script setup>
import { ref } from 'vue';

const activeIndex = ref('1');

const handleSelect = (index, indexPath) => {
  console.log('selected index:', index, 'index path:', indexPath);
};
</script>

<style scoped>
.navigation-bar {
  background-color: #f0ead6;
  padding: 10px 20px;
  color: #5c3a21;
}

.nav-content {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  align-items: center;
}

.logo {
  width: 100px;
  margin-right: 20px;
}

.el-menu-demo {
  background-color: transparent;
}

.el-menu-item, .el-submenu__title {
  color: #5c3a21 !important;
  font-family: 'Times New Roman', Times, serif;
}

.el-menu-item:hover, .el-submenu__title:hover {
  background-color: #dcd0c0 !important;
}
</style>