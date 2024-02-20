<template>
  <NavigationBar/>
  <CategoryDisplaySection/>
  <AddNewCategoryForm/>
  <Footer/>
</template>

<script lang="ts" setup>
import NavigationBar from "@/components/ImageCollectionPlatform/HomePage/NavigationBar.vue";
import CategoryDisplaySection
  from "@/components/ImageCollectionPlatform/CategoryMaintenancePage/CategoryDisplaySection.vue";
import AddNewCategoryForm from "@/components/ImageCollectionPlatform/CategoryMaintenancePage/AddNewCategoryForm.vue";
import Footer from "@/components/ImageCollectionPlatform/CategoryMaintenancePage/Footer.vue";
</script>
<style>
@import url("@/style.css");
</style>
    