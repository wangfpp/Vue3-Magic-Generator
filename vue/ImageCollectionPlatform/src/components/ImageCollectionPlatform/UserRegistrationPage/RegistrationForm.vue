<template>
  <div class="registration-form-container">
    <el-form ref="form" :model="form" label-position="top" class="registration-form">
      <el-form-item label="邮箱" required>
        <el-input v-model="form.email" placeholder="请输入邮箱"></el-input>
      </el-form-item>
      <el-form-item label="用户名" required>
        <el-input v-model="form.username" placeholder="请输入用户名"></el-input>
      </el-form-item>
      <el-form-item label="密码" required>
        <el-input type="password" v-model="form.password" placeholder="请输入密码"></el-input>
      </el-form-item>
      <el-form-item label="确认密码" required>
        <el-input type="password" v-model="form.confirmPassword" placeholder="请再次输入密码"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm">注册</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const form = ref({
  email: '',
  username: '',
  password: '',
  confirmPassword: '',
});

const submitForm = () => {
  console.log('Submitted form:', form.value);
  // 实际应用中，这里会包含表单验证和提交到服务器的逻辑
};
</script>

<style scoped>
.registration-form-container {
  max-width: 600px;
  margin: 50px auto;
  background-color: #f9f3e4; /* 淡黄色背景 */
  padding: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
}

.registration-form {
  font-family: 'Times New Roman', Times, serif; /* 经典字体 */
}

.el-form-item {
  margin-bottom: 20px;
}

.el-input {
  background-color: #f9f3e4; /* 输入框背景 */
  border-color: #d3c1a5; /* 边框颜色 */
  color: #7a6248; /* 文字颜色 */
}

.el-button {
  background-color: #7a6248; /* 按钮背景颜色 */
  border-color: #7a6248; /* 按钮边框颜色 */
  color: #f9f3e4; /* 按钮文字颜色 */
}

.el-button:hover {
  background-color: #9b856a; /* 鼠标悬停时按钮背景颜色变化 */
  border-color: #9b856a; /* 鼠标悬停时按钮边框颜色变化 */
}
</style>