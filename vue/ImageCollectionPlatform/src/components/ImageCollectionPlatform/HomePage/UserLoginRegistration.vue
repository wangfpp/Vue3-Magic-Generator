<template>
  <section class="user-login-registration">
    <div class="login-registration-container">
      <el-button @click="showLoginDialog = true" type="text">登录</el-button>
      <el-dialog title="登录" v-model="showLoginDialog" @close="clearLoginForm">
        <el-form :model="loginForm">
          <el-form-item label="用户名" prop="username">
            <el-input v-model="loginForm.username" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="密码" prop="password">
            <el-input type="password" v-model="loginForm.password" autocomplete="off"></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="showLoginDialog = false">取消</el-button>
          <el-button type="primary" @click="login">登录</el-button>
        </div>
      </el-dialog>

      <el-button @click="showRegistrationDialog = true" type="text">注册</el-button>
      <el-dialog title="注册" v-model="showRegistrationDialog" @close="clearRegistrationForm">
        <el-form :model="registrationForm">
          <el-form-item label="用户名" prop="username">
            <el-input v-model="registrationForm.username" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="邮箱" prop="email">
            <el-input v-model="registrationForm.email" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="密码" prop="password">
            <el-input type="password" v-model="registrationForm.password" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="确认密码" prop="confirmPassword">
            <el-input type="password" v-model="registrationForm.confirmPassword" autocomplete="off"></el-input>
          </el-form-item>
        </el-form>
        <div slot="footer" class="dialog-footer">
          <el-button @click="showRegistrationDialog = false">取消</el-button>
          <el-button type="primary" @click="register">注册</el-button>
        </div>
      </el-dialog>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue';

const showLoginDialog = ref(false);
const showRegistrationDialog = ref(false);
const loginForm = ref({ username: '', password: '' });
const registrationForm = ref({ username: '', email: '', password: '', confirmPassword: '' });

const clearLoginForm = () => {
  loginForm.value.username = '';
  loginForm.value.password = '';
};

const clearRegistrationForm = () => {
  registrationForm.value.username = '';
  registrationForm.value.email = '';
  registrationForm.value.password = '';
  registrationForm.value.confirmPassword = '';
};

const login = () => {
  // 实现登录逻辑
  console.log('登录信息', loginForm.value);
  showLoginDialog.value = false;
  clearLoginForm();
};

const register = () => {
  // 实现注册逻辑
  console.log('注册信息', registrationForm.value);
  showRegistrationDialog.value = false;
  clearRegistrationForm();
};
</script>

<style scoped>
.user-login-registration {
  text-align: center;
  margin-top: 20px;
}

.login-registration-container {
  display: inline-block;
}

.el-button {
  margin: 0 10px;
  color: #5c3a21;
  border-color: #5c3a21;
}

.dialog-footer {
  text-align: right;
}
</style>