<template>
  <div class="login-page-link-container">
    <a href="/login" class="login-link">已有账号？点击这里登录</a>
  </div>
</template>

<script setup>
// 在这个简单的组件中，我们不需要导入或设置Vue或Element Plus的特定功能。
// 该组件主要提供一个静态链接到登录页面。
</script>

<style scoped>
.login-page-link-container {
  text-align: center; /* 使链接居中 */
  margin-top: 20px; /* 与其他元素保持一定距离 */
}

.login-link {
  color: #7a6248; /* 链接颜色 */
  font-family: 'Times New Roman', Times, serif; /* 经典字体 */
  font-size: 16px; /* 字体大小 */
  text-decoration: underline; /* 下划线装饰 */
}

.login-link:hover {
  color: #9b856a; /* 鼠标悬停时链接颜色变化 */
  text-decoration: none; /* 移除下划线 */
}
</style>