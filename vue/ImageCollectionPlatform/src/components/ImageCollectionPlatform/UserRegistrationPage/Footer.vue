<template>
  <footer class="footer-container">
    <div class="footer-content">
      <p>© 2024 YourWebsiteName. All rights reserved.</p>
      <nav class="footer-nav">
        <ul>
          <li><a href="/privacy-policy">隐私政策</a></li>
          <li><a href="/terms">服务条款</a></li>
          <li><a href="/contact">联系我们</a></li>
        </ul>
      </nav>
    </div>
  </footer>
</template>

<script setup>
// 由于页脚组件主要包含静态内容和链接，这里不需要导入Vue或Element Plus的特定功能。
</script>

<style scoped>
.footer-container {
  background-color: #f4f1ea; /* 复古色调背景 */
  color: #7a6248; /* 文字颜色 */
  font-family: 'Times New Roman', Times, serif; /* 经典字体 */
  padding: 20px 0; /* 上下填充 */
  text-align: center; /* 文本居中 */
}

.footer-content p {
  margin: 0; /* 移除默认的段落间距 */
}

.footer-nav ul {
  list-style: none; /* 移除列表项目的默认样式 */
  padding: 0; /* 移除默认的内边距 */
  margin: 10px 0 0; /* 调整间距 */
}

.footer-nav li {
  display: inline; /* 列表项内联显示 */
  margin: 0 10px; /* 调整列表项之间的间距 */
}

.footer-nav a {
  color: #7a6248; /* 链接颜色 */
  text-decoration: none; /* 移除下划线 */
}

.footer-nav a:hover {
  color: #9b856a; /* 鼠标悬停时链接颜色变化 */
}
</style>