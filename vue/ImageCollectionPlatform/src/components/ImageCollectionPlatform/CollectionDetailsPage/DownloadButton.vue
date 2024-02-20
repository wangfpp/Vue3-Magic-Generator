<template>
  <div class="download-button-wrapper">
    <el-button type="primary" icon="el-icon-download" class="download-btn">下载图片集</el-button>
  </div>
</template>

<script setup>
import { ElButton } from 'element-plus';
</script>

<style scoped>
.download-button-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
  background-color: #f0ead6;
}

.download-btn {
  font-family: 'Courier New', Courier, monospace;
  font-size: 16px;
  color: #333;
  background-color: #a78e6f;
  border-color: #a78e6f;
}

.download-btn:hover {
  background-color: #8c7a5f;
  border-color: #8c7a5f;
}
</style>