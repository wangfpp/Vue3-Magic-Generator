<script setup>
import {inject, ref, defineEmits, watch} from "vue";

const emit = defineEmits(['change'])

const props = defineProps({
  table: String,
  placeholder: String,
  value: Object,
});

const value = ref()
const list = ref([])
const axios = inject('$axios')
axios.post(`/common/${props.table}/query`, {}).then(res => {
  list.value = res.data
})
const change = (e)=>{
  emit("change", e)
}

watch(
    () => props.value,
    (newVal) => {
      value.value = newVal;
    },
);

</script>

<template>
  <el-select v-model="value" :placeholder="placeholder" @change="change">
    <el-option :label="v.name" :value="v.id" v-for="(v, i) in list" :key="i"></el-option>
  </el-select>
</template>

<style scoped>

</style>