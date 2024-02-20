<template>
  <nav class="navigation-wrapper">
    <div class="logo">
      <el-image src="https://img.freepik.com/free-vector/circle-hearts-set_78370-2859.jpg" style="width: 40px; height: 40px;"></el-image>
    </div>
    <el-menu
      class="navigation-menu"
      background-color="#f0ead6"
      text-color="#5c3a21"
      active-text-color="#ffd04b"
      mode="horizontal"
      default-active="1"
    >
      <el-menu-item index="1">首页</el-menu-item>
      <el-menu-item index="2">图片集</el-menu-item>
      <el-menu-item index="3">艺人信息</el-menu-item>
      <el-menu-item index="4">联系我们</el-menu-item>
    </el-menu>
  </nav>
</template>

<script setup>
import { ElMenu, ElMenuItem, ElImage } from 'element-plus';
</script>

<style scoped>
.navigation-wrapper {
  display: flex;
  align-items: center;
  background-color: #f0ead6;
  padding: 10px 20px;
  box-shadow: 0 2px 4px 0 rgba(0,0,0,0.1);
}

.logo {
  margin-right: 20px;
}

.navigation-menu {
  border: none;
}
</style>