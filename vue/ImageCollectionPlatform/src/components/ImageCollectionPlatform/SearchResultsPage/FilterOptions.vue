<template>
  <div class="filter-options">
    <el-row :gutter="20">
      <el-col :span="24">
        <div class="filter-header">筛选条件</div>
        <l-select table="artist" placeholder="艺术家" class="filter-select" v-model="artist_id"/>
        <l-select table="category" placeholder="风格" class="filter-select" v-model="category_id"/>
        <el-button type="primary" @click="applyFilters">应用筛选</el-button>
      </el-col>
    </el-row>
  </div>
</template>

<script setup>
import LSelect from "@/components/common/form/LSelect.vue";
import {ref, defineProps, defineEmits, watch} from 'vue';

const emit = defineEmits(["search"])
const props = defineProps({
  category_id: Object,
  artist_id: Object,
})
const category_id = ref(props.category_id);
const artist_id = ref(props.artist_id);

watch(() => props.artist_id, (val) => {
  artist_id.value = val
})
watch(() => props.category_id, (val) => {
  category_id.value = val
})
const applyFilters = () => {
  emit("search", {category_id, artist_id})
};
</script>

<style scoped>
.filter-options {
  padding: 20px;
  background-color: #f0ead6;
}

.filter-header {
  font-size: 20px;
  color: #5c3a21;
  margin-bottom: 10px;
}

.filter-select {
  margin-right: 10px;
  margin-bottom: 20px;
}

.el-select .el-input {
  background-color: #fdf6e3;
  border-color: #c8b7a1;
}

.el-button--primary {
  background-color: #c8b7a1;
  border-color: #c8b7a1;
  color: #5c3a21;
}
</style>