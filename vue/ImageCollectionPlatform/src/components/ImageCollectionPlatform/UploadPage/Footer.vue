<template>
  <div class="footer-container">
    <div class="footer-content">
      <p>© 2024 Your Company Name. All rights reserved.</p>
      <div class="footer-links">
        <a href="#" class="footer-link">隐私政策</a>
        <a href="#" class="footer-link">联系我们</a>
      </div>
    </div>
  </div>
</template>

<script setup>
// No additional JavaScript needed for this component as it's mostly static content
</script>

<style scoped>
.footer-container {
  display: flex;
  justify-content: center;
  padding: 20px;
  background-color: #f0ebe5;
  color: #333;
  font-family: 'Courier New', Courier, monospace;
}

.footer-content {
  text-align: center;
}

.footer-links {
  margin-top: 10px;
}

.footer-link {
  margin: 0 10px;
  color: #333;
  text-decoration: none;
  transition: color 0.3s ease;
}

.footer-link:hover {
  color: #7a6248;
}
</style>