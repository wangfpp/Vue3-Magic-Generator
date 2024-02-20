<template>
  <div class="publish-button-container">
    <el-button type="primary" @click="onPublish" class="publish-button">发布</el-button>
  </div>
</template>

<script setup>
import { ref } from 'vue';

// Assuming you have a method to handle the publishing logic
const onPublish = () => {
  console.log('Publishing content...');
  // Here you would implement the actual publish logic
};
</script>

<style scoped>
.publish-button-container {
  display: flex;
  justify-content: center;
  margin-top: 20px;
}

.publish-button {
  font-family: 'Courier New', Courier, monospace;
  background-color: #dcd0c0;
  border-color: #dcd0c0;
  color: #333;
  font-size: 16px;
  padding: 10px 20px;
}

.publish-button:hover {
  background-color: #c4b395;
  border-color: #c4b395;
}
</style>