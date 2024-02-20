<template>
  <div class="edit-delete-options">
    <el-table :data="artistList" style="width: 100%">
      <el-table-column prop="name" label="艺人姓名"></el-table-column>
      <el-table-column prop="category" label="艺术类别"></el-table-column>
      <el-table-column label="操作">
        <template #default="scope">
          <el-button type="text" @click="handleEdit(scope.row)">编辑</el-button>
          <el-button type="text" @click="handleDelete(scope.row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const artistList = ref([
  // 示例数据，实际应用中应从后端获取
  { name: '艺人A', category: '绘画' },
  { name: '艺人B', category: '雕塑' },
]);

const handleEdit = (row) => {
  console.log('编辑艺人信息', row);
  // 实现编辑逻辑
};

const handleDelete = (row) => {
  console.log('删除艺人信息', row);
  // 实现删除逻辑
};
</script>

<style scoped>
.edit-delete-options {
  padding: 20px;
  background-color: #f9f5f0;
  color: #7a6248;
  font-family: "Times New Roman", Times, serif;
}

.el-button {
  color: #7a6248;
  border-color: #7a6248;
}

.el-button:hover {
  color: #5a4234;
  border-color: #5a4234;
}
</style>