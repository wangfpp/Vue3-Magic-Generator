<template>
  <div class="category-display-section">
    <el-card class="box-card" v-for="category in categories" :key="category.id" :body-style="{ padding: '20px' }">
      <div class="category-content">
        <h4>{{ category.name }}</h4>
        <el-button type="text" @click="editCategory(category.id)">编辑</el-button>
        <el-button type="text" @click="deleteCategory(category.id)">删除</el-button>
      </div>
    </el-card>
    <el-input v-model="searchText" placeholder="搜索类别..." clearable @clear="fetchCategories" @input="searchCategory"></el-input>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { ElCard, ElButton, ElInput } from 'element-plus';

const categories = ref([
  // 示例数据，实际应用中应从后端获取
  { id: 1, name: '类别1' },
  { id: 2, name: '类别2' },
  { id: 3, name: '类别3' },
]);

const searchText = ref('');

const fetchCategories = () => {
  // 实现获取类别的逻辑
  console.log('Fetching categories...');
};

const searchCategory = () => {
  // 实现搜索类别的逻辑，这里只是一个示例
  console.log('Searching for:', searchText.value);
};

const editCategory = (id) => {
  // 实现编辑类别的逻辑
  console.log('Editing category with id:', id);
};

const deleteCategory = (id) => {
  // 实现删除类别的逻辑
  console.log('Deleting category with id:', id);
};
</script>

<style scoped>
.category-display-section {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  margin: 20px 0;
}

.box-card {
  width: calc(33.333% - 20px);
  background-color: #f0ebe5;
  color: #333;
  border-color: #f0ebe5;
}

.category-content {
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-family: 'Courier New', Courier, monospace;
}

.el-input {
  margin: 20px 0;
  width: 100%;
  max-width: 300px;
}

.el-button {
  color: #7a6248;
}

.el-button:focus, .el-button:hover {
  background-color: transparent !important;
}
</style>