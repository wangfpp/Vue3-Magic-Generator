<template>
  <div class="collection-title-description-wrapper">
    <h1 class="collection-title">{{form.title}}</h1>
    <p class="collection-description">
      {{form.description}}
    </p>
  </div>
</template>

<script setup>
import {inject, ref} from "vue";
const form = ref({})
</script>

<style scoped>
.collection-title-description-wrapper {
  padding: 20px;
  background-color: #f0ead6;
  color: #5c3a21;
  text-align: center;
}

.collection-title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 10px;
  color: #5c3a21;
}

.collection-description {
  font-size: 16px;
  color: #5c3a21;
}
</style>