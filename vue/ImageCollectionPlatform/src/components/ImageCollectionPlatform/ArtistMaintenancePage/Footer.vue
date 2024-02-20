<template>
  <footer class="site-footer">
    <div class="container">
      <div class="footer-content">
        <p>© 2024 艺术家管理系统. All rights reserved.</p>
        <el-button type="text" @click="scrollToTop">回到顶部</el-button>
      </div>
      <div class="contact-info">
        <p>联系我们: info@artistmanagement.com</p>
      </div>
    </div>
  </footer>
</template>

<script setup>
import { ElButton } from 'element-plus';
import { ref } from 'vue';

const scrollToTop = () => {
  window.scrollTo({
    top: 0,
    behavior: 'smooth',
  });
};
</script>

<style scoped>
.site-footer {
  padding: 20px 0;
  background-color: #f9f5f0;
  color: #7a6248;
  font-family: "Times New Roman", Times, serif;
  text-align: center;
}

.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
}

.footer-content {
  margin-bottom: 20px;
}

.contact-info {
  margin-top: 10px;
}

.el-button {
  color: #7a6248;
  border-color: #7a6248;
}

.el-button:hover {
  color: #5a4234;
  border-color: #5a4234;
}
</style>