<template>
  <div class="login-form-container">
    <el-form ref="loginForm" :model="loginForm" class="login-form" @submit.native.prevent="onLogin">
      <el-form-item>
        <el-input v-model="loginForm.username" placeholder="邮箱/用户名"></el-input>
      </el-form-item>
      <el-form-item>
        <el-input type="password" v-model="loginForm.password" placeholder="密码"></el-input>
      </el-form-item>
      <el-form-item>
        <el-checkbox v-model="loginForm.rememberMe">记住我</el-checkbox>
        <a href="#" class="forgot-password">忘记密码?</a>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onLogin">登录</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const loginForm = ref({
  username: '',
  password: '',
  rememberMe: false,
});

const onLogin = () => {
  console.log('Login form data:', loginForm.value);
  // 实际项目中这里应该是调用登录接口的逻辑
};
</script>

<style scoped>
.login-form-container {
  max-width: 400px;
  margin: 50px auto;
  padding: 25px;
  background-color: #f9f5f0;
  border: 1px solid #d3c1ae;
  box-shadow: 0 2px 12px rgba(0,0,0,.1);
  border-radius: 5px;
}

.login-form {
  display: flex;
  flex-direction: column;
}

.el-form-item {
  margin-bottom: 20px;
}

.forgot-password {
  float: right;
  font-size: 14px;
  color: #7a6248;
  text-decoration: underline;
}

.el-button {
  width: 100%;
  background-color: #7a6248;
  border-color: #7a6248;
}

.el-button:focus, .el-button:hover {
  background-color: #9b856a;
  border-color: #9b856a;
}

.el-input__inner {
  border-color: #d3c1ae;
}

.el-checkbox__input.is-checked + .el-checkbox__label {
  color: #7a6248;
}
</style>