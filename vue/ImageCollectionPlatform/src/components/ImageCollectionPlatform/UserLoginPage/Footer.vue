<template>
  <footer class="footer-container">
    <div class="footer-content">
      <p>© 2024 YourWebsiteName. All rights reserved.</p>
      <el-link class="footer-link" href="/privacy-policy">隐私政策</el-link>
      <el-link class="footer-link" href="/terms">条款和条件</el-link>
      <el-link class="footer-link" href="/about-us">关于我们</el-link>
    </div>
    <div class="social-media-icons">
      <el-link icon="el-icon-facebook" class="social-icon"></el-link>
      <el-link icon="el-icon-twitter" class="social-icon"></el-link>
      <el-link icon="el-icon-google" class="social-icon"></el-link>
    </div>
  </footer>
</template>

<script setup>
// Element Plus components are auto-imported
</script>

<style scoped>
.footer-container {
  background-color: #f9f3e4; /* 淡黄色背景 */
  color: #7a6248; /* 复古色调文字 */
  text-align: center;
  padding: 20px;
  font-family: 'Times New Roman', Times, serif; /* 经典字体 */
}

.footer-content p {
  margin: 0;
  padding: 5px;
}

.footer-link {
  color: #7a6248; /* 复古色调 */
  margin: 0 10px;
}

.footer-link:hover {
  color: #9b856a; /* 鼠标悬停时的颜色变化 */
}

.social-media-icons {
  margin-top: 20px;
}

.social-icon {
  font-size: 24px; /* 社交媒体图标大小 */
  color: #7a6248; /* 复古色调 */
  margin: 0 5px;
}

.social-icon:hover {
  color: #9b856a; /* 鼠标悬停时的颜色变化 */
}
</style>