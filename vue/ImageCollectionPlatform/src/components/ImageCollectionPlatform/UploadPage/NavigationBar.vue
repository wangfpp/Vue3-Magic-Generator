<template>
  <div class="navigation-bar">
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
      <el-menu-item index="1">首页</el-menu-item>
      <el-menu-item index="2">图片集浏览</el-menu-item>
      <el-menu-item index="3">上传页面</el-menu-item>
    </el-menu>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { ElMenu, ElMenuItem } from 'element-plus';

const activeIndex = ref('1');

const handleSelect = (index, indexPath) => {
  console.log('selected index:', index, 'index path:', indexPath);
  // Here you can implement the logic for navigating to the respective page
};
</script>

<style scoped>
.navigation-bar {
  font-family: 'Courier New', Courier, monospace;
  background-color: #f0ead6;
  padding: 10px 0;
}

.el-menu-demo {
  background-color: transparent;
  border-bottom: none;
}

.el-menu-item {
  color: #333 !important;
  font-size: 16px;
}

.el-menu-item:focus, .el-menu-item:hover {
  background-color: #dcd0c0 !important;
}

.el-menu-item.is-active {
  color: #555 !important;
  background-color: #dcd0c0 !important;
}
</style>