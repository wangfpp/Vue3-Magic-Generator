<template>
  <div class="navigation-bar">
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect" background-color="#f0ebe5" text-color="#7a6248" active-text-color="#ffd04b">
      <el-menu-item index="1">艺人列表</el-menu-item>
      <el-menu-item index="2">添加新艺人</el-menu-item>
      <el-menu-item index="3">后台管理主页</el-menu-item>
      <el-sub-menu index="4">
        <template #title>
          <span>更多功能</span>
        </template>
        <el-menu-item index="4-1">功能一</el-menu-item>
        <el-menu-item index="4-2">功能二</el-menu-item>
        <el-menu-item index="4-3">功能三</el-menu-item>
      </el-sub-menu>
    </el-menu>
  </div>
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
  font-family: 'Courier New', Courier, monospace;
  border-bottom: 1px solid #ebebeb;
}

.el-menu-demo {
  background-color: #f0ebe5;
  color: #7a6248;
}

.el-menu {
  background-color: #f0ebe5;
  color: #7a6248;
}

.el-menu-item:focus, .el-menu-item:hover {
  background-color: #ffd04b;
}

.el-submenu__title:focus, .el-submenu__title:hover {
  background-color: #ffd04b;
}

.el-menu-item, .el-submenu__title {
  color: #7a6248 !important;
}

.el-menu-item.is-active, .el-submenu__title.is-active {
  color: #ffd04b !important;
}
</style>