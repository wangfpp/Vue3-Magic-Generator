<template>
  <div class="add-new-category-form">
    <el-form ref="form" :model="form" label-width="120px" @submit.native.prevent="onSubmit">
      <el-form-item label="类别名称">
        <el-input v-model="form.name" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item label="类别描述">
        <el-input type="textarea" v-model="form.description" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="onSubmit">提交</el-button>
        <el-button @click="onReset">重置</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const form = ref({
  name: '',
  description: '',
});

const onSubmit = () => {
  console.log('Form submitted:', form.value);
  // 实际应用中，这里会是提交表单到后端的逻辑
};

const onReset = () => {
  form.value.name = '';
  form.value.description = '';
};
</script>

<style scoped>
.add-new-category-form {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f0ebe5;
  border-radius: 8px;
  box-shadow: 0 2px 12px 0 rgba(0,0,0,0.1);
  font-family: 'Courier New', Courier, monospace;
}

.el-form-item {
  margin-bottom: 20px;
}

.el-input, .el-textarea {
  border-color: #c0b3a9;
}

.el-button {
  margin-right: 10px;
  background-color: #7a6248;
  border-color: #7a6248;
  color: #fff;
}

.el-button:hover {
  background-color: #9d8568;
  border-color: #9d8568;
}

.el-button:active {
  background-color: #7a6248;
  border-color: #7a6248;
}
</style>