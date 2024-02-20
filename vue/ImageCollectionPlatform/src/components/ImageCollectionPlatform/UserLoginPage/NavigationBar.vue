<template>
  <nav class="navigation-bar">
    <div class="container">
      <img src="https://img.freepik.com/free-vector/traditional-red-chinese-new-year-banner-with-golden-elements_1017-35911.jpg?t=st=1708270917~exp=1708271517~hmac=892f63ee1ce452ed94fd6b1343c13add263848c751f8bb0038ed86c3f782daee" alt="Website Logo" class="logo">
      <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" @select="handleSelect">
        <el-menu-item index="1">主页</el-menu-item>
        <el-menu-item index="2">帮助中心</el-menu-item>
        <el-menu-item index="3">联系我们</el-menu-item>
        <el-submenu index="4">
          <template #title>账户</template>
          <el-menu-item index="4-1">登录</el-menu-item>
          <el-menu-item index="4-2">注册</el-menu-item>
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
  padding: 10px 0;
  background-color: #f9f5f0;
  color: #7a6248;
  font-family: "Times New Roman", Times, serif;
}

.container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 50px;
}

.logo {
  width: 120px;
  height: auto;
}

.el-menu-demo {
  background-color: transparent;
}

.el-menu {
  border-color: transparent;
}

.el-menu-item:focus, .el-menu-item:hover {
  background-color: #f0e6d2;
}

.el-menu-item.is-active {
  border-bottom: 2px solid #7a6248;
}

.el-submenu .el-menu-item {
  color: #7a6248;
}

.el-submenu:focus, .el-submenu:hover {
  background-color: #f0e6d2;
}

.el-submenu .el-menu {
  background-color: #f9f5f0;
}

.el-submenu .el-menu-item.is-active {
  background-color: #f0e6d2;
}
</style>