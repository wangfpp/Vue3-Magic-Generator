<template>
  <div class="search-bar">
    <el-input
        v-model="searchQuery"
        placeholder="请输入搜索内容"
        prefix-icon="el-icon-search"
        clearable
        @clear="onClear"
        @keyup.enter="onSearch"
    >
      <template #append>
        <el-button icon="el-icon-search" @click="onSearch">搜索</el-button>
      </template>
    </el-input>
  </div>
</template>

<script setup>
import {ref, defineProps, defineEmits, watch} from 'vue';

const emit = defineEmits(["search"])
const props = defineProps({
  title: String,
})

watch(() => props.title, (newVal) => {
  searchQuery.value = newVal
})
const searchQuery = ref(props.title);
const onSearch = () => {
  emit("search", {title: searchQuery.value})
};

const onClear = () => {
  console.log('清空搜索框');
  // 清空搜索框后的逻辑处理
};
</script>

<style scoped>
.search-bar {
  padding: 20px;
  background-color: #f0ead6;
  display: flex;
  justify-content: center;
  align-items: center;
}

.el-input {
  max-width: 600px;
  border: 1px solid #c8b7a1;
  background-color: #fdf6e3;
  color: #5c3a21;
}

.el-input__inner {
  border-color: #c8b7a1;
  background-color: #fdf6e3;
  color: #5c3a21;
}

.el-input__icon {
  color: #5c3a21;
}

.el-button {
  background-color: #dcd0c0;
  color: #5c3a21;
  border: none;
}

.el-button:focus, .el-button:hover {
  background-color: #c8b7a1;
  color: #5c3a21;
}
</style>