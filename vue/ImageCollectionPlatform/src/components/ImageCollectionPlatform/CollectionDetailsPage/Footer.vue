<template>
  <div class="footer-wrapper">
    <div class="footer-content">
      <p>© 2024 YourWebsiteName. All rights reserved.</p>
      <div class="footer-links">
        <a href="#" class="footer-link">Privacy Policy</a>
        <a href="#" class="footer-link">Terms of Use</a>
        <a href="#" class="footer-link">Contact Us</a>
      </div>
    </div>
  </div>
</template>

<script setup>
// No need to manually import components from Element Plus in this setup script.
</script>

<style scoped>
.footer-wrapper {
  padding: 20px;
  background-color: #f0ead6;
  text-align: center;
}

.footer-content p {
  font-family: 'Courier New', Courier, monospace;
  font-size: 14px;
  color: #333;
}

.footer-links {
  margin-top: 10px;
}

.footer-link {
  font-family: 'Courier New', Courier, monospace;
  font-size: 14px;
  color: #555;
  text-decoration: none;
  margin: 0 10px;
}

.footer-link:hover {
  text-decoration: underline;
}
</style>