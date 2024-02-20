<template>
  <div class="signup-link-container">
    <span>没有账号？</span>
    <el-link class="signup-link" @click="navigateToSignUp">立即注册</el-link>
  </div>
</template>

<script setup>
import { useRouter } from 'vue-router';

const router = useRouter();

const navigateToSignUp = () => {
  router.push('/signup'); // 假设注册页面的路由是 '/signup'
};
</script>

<style scoped>
.signup-link-container {
  text-align: center;
  margin-top: 20px;
}

.signup-link {
  font-size: 16px;
  color: #7a6248; /* 复古色调 */
  margin-left: 5px;
}

.signup-link:hover {
  color: #9b856a; /* 鼠标悬停时的颜色变化 */
}
</style>