<template>
  <header class="navigation-bar">
    <div class="logo">
      <img src="https://img.freepik.com/free-vector/circle-hearts-set_78370-2859.jpg" alt="Logo" class="logo-image">
    </div>
    <el-menu class="nav-menu" mode="horizontal" background-color="#f9f3e4" text-color="#7a6248" active-text-color="#9b856a">
      <el-menu-item index="1">主页</el-menu-item>
      <el-menu-item index="2">用户注册</el-menu-item>
      <el-menu-item index="3">登录</el-menu-item>
      <el-menu-item index="4">其他页面</el-menu-item>
    </el-menu>
  </header>
</template>

<script setup>
// Element Plus components are auto-imported
</script>

<style scoped>
.navigation-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  background-color: #f9f3e4; /* 淡黄色背景 */
  color: #7a6248; /* 复古色调文字 */
  padding: 10px 50px;
  font-family: 'Times New Roman', Times, serif; /* 经典字体 */
}

.logo-image {
  height: 50px;
  width: auto;
}

.nav-menu {
  background-color: #f9f3e4; /* 保持背景一致性 */
}

.el-menu-item:focus, .el-menu-item:hover {
  background-color: #e8dfc9; /* 鼠标悬停时的背景变化 */
}

.el-menu-item:not(.is-disabled):active {
  color: #9b856a; /* 鼠标点击时的文字颜色变化 */
}
</style>