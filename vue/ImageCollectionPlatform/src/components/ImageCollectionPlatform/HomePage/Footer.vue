<template>
  <footer class="site-footer">
    <div class="footer-content">
      <p>© 2024 VintageArt. All rights reserved.</p>
      <div class="footer-links">
        <a href="#" class="footer-link">Privacy Policy</a>
        <a href="#" class="footer-link">Terms of Service</a>
        <a href="#" class="footer-link">Contact Us</a>
      </div>
      <div class="social-media-icons">
        <el-link class="social-icon">

        </el-link>
        <el-link class="social-icon">

        </el-link>
        <el-link class="social-icon">

        </el-link>
      </div>
    </div>
  </footer>
</template>

<script setup>
// No need to manually import Element Plus components as per the instruction.
</script>

<style scoped>
.site-footer {
  padding: 20px;
  background-color: #f0ead6;
  text-align: center;
  color: #5c3a21;
}

.footer-content {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.footer-links {
  margin-top: 10px;
}

.footer-link {
  margin: 0 10px;
  color: #5c3a21;
  font-size: 16px;
  text-decoration: none;
}

.social-media-icons {
  margin-top: 20px;
}

.social-icon {
  font-size: 24px;
  color: #5c3a21;
  margin: 0 5px;
}
</style>