<template>
  <div class="pagination-wrapper">
    <el-pagination
      @current-change="handleCurrentChange"
      :current-page="currentPage"
      :page-size="pageSize"
      layout="prev, pager, next"
      :total="total">
    </el-pagination>
  </div>
</template>

<script setup>
import { ref, computed, watch, toRefs , defineEmits} from 'vue';

const emit = defineEmits(["current-change"])
// 从父组件接收的props
const props = defineProps({
  currentPage: Number,
  pageSize: Number,
  total: Number,
});

const currentPage = ref(props.currentPage || 1);

// 计算总页数
const totalPages = computed(() => {
  return Math.ceil(props.total / props.pageSize);
});

// 监听props.currentPage的变化，以保持内外状态一致
watch(
  () => props.currentPage,
  (newVal) => {
    currentPage.value = newVal;
  },
);


// 提供给template使用的ref需要再次解构
const { pageSize, total } = toRefs(props);

const handleCurrentChange = val => {
  currentPage.value = val;
  // 这里可以添加加载新页面的逻辑
  console.log(`当前页: ${val}`);
  emit('current-change', currentPage.value);
};
</script>

<style scoped>
.pagination-wrapper {
  text-align: center;
  padding: 20px;
  background-color: #f0ead6;
}

.el-pagination .el-pager li:not(.active) {
  color: #5c3a21;
}

.el-pagination .el-pager li.active {
  background-color: #c8b7a1;
  color: #5c3a21;
}

.el-pagination button {
  background-color: #fdf6e3;
  border-color: #c8b7a1;
  color: #5c3a21;
}

.el-pagination button:hover {
  background-color: #c8b7a1;
  border-color: #c8b7a1;
  color: #5c3a21;
}
</style>