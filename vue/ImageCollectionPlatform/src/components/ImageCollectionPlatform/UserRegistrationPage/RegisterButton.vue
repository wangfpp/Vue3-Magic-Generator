<template>
  <div class="register-button-container">
    <el-button type="primary" @click="submitRegistration">注册</el-button>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { ElMessage } from 'element-plus';

const submitRegistration = () => {
  // 假设这里是提交注册信息的逻辑
  console.log('注册信息已提交');
  ElMessage({
    message: '注册成功，请检查您的邮箱以完成验证。',
    type: 'success',
  });
};
</script>

<style scoped>
.register-button-container {
  text-align: center; /* 使按钮居中 */
  padding: 20px;
}

.el-button {
  background-color: #7a6248; /* 按钮背景颜色 */
  border-color: #7a6248; /* 按钮边框颜色 */
  color: #f9f3e4; /* 按钮文字颜色 */
  font-family: 'Times New Roman', Times, serif; /* 经典字体 */
  font-size: 16px; /* 字体大小 */
}

.el-button:hover {
  background-color: #9b856a; /* 鼠标悬停时按钮背景颜色变化 */
  border-color: #9b856a; /* 鼠标悬停时按钮边框颜色变化 */
}
</style>