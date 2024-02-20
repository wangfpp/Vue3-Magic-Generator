<template>
  <div class="navigation-bar">
    <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect" background-color="#f0ebe5" text-color="#333" active-text-color="#7a6248">
      <el-menu-item index="1">首页</el-menu-item>
      <el-menu-item index="2">类别维护</el-menu-item>
      <el-menu-item index="3">其他管理</el-menu-item>
    </el-menu>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { ElMenu, ElMenuItem } from 'element-plus';

const activeIndex = ref('1');

const handleSelect = (index, indexPath) => {
  console.log('selected index:', index);
  // 根据选中的index进行路由跳转或其他操作
  // 例如: router.push({ path: `/your-path/${index}` });
};
</script>

<style scoped>
.navigation-bar {
  font-family: 'Courier New', Courier, monospace;
  background-color: #f0ebe5;
  padding: 10px 0;
}

.el-menu-demo {
  border: none;
}

/* 覆盖element-plus的样式以匹配设计要求 */
.el-menu {
  background-color: #f0ebe5 !important;
}

.el-menu-item:focus, .el-menu-item:hover {
  background-color: transparent !important;
}

.el-menu-item.is-active {
  color: #7a6248 !important;
  border-bottom: 2px solid #7a6248 !important;
}
</style>