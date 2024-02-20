<template>
  <section class="search-bar">
    <div class="search-container">
      <el-input
        v-model="searchQuery"
        placeholder="搜索图片集或艺人..."
        prefix-icon="el-icon-search"
        class="search-input"
        @keyup.enter="performSearch"
      ></el-input>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue';

const searchQuery = ref('');

const performSearch = () => {
  // 实现搜索逻辑
  console.log('搜索内容', searchQuery.value);
  // 根据searchQuery.value进行搜索
};
</script>

<style scoped>
.search-bar {
  padding: 20px;
  background-color: #f0ead6;
  text-align: center;
}

.search-container {
  display: inline-block;
  width: 100%;
  max-width: 600px;
}

.search-input {
  width: 100%;
  border: 1px solid #5c3a21;
  color: #5c3a21;
}

.el-input__inner {
  border-color: #5c3a21;
  color: #5c3a21;
}

.el-input__icon {
  color: #5c3a21;
}
</style>