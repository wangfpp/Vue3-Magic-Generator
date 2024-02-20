<template>
  <div class="footer">
    <div class="footer-content">
      <p>© 2024 Your Company. All rights reserved.</p>
      <p>
        <a href="#privacy-policy">Privacy Policy</a> | 
        <a href="#terms-of-use">Terms of Use</a> | 
        <a href="#contact-us">Contact Us</a>
      </p>
      <el-button type="text" @click="scrollToTop">返回顶部</el-button>
    </div>
  </div>
</template>

<script setup>
import { ElButton } from 'element-plus';

const scrollToTop = () => {
  window.scrollTo({
    top: 0,
    behavior: 'smooth',
  });
};
</script>

<style scoped>
.footer {
  background-color: #f0ebe5;
  color: #7a6248;
  text-align: center;
  padding: 20px;
  font-family: 'Courier New', Courier, monospace;
}

.footer-content p {
  margin: 10px 0;
}

.footer-content a {
  color: #7a6248;
  text-decoration: none;
}

.footer-content a:hover {
  text-decoration: underline;
}

.el-button {
  color: #7a6248;
  font-size: 14px;
}
</style>