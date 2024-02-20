<template>
  <NavigationBar/>
  <SearchResultsDisplay/>
  <Footer/>
</template>

<script lang="ts" setup>
import NavigationBar from "@/components/ImageCollectionPlatform/HomePage/NavigationBar.vue";
import SearchBar from "@/components/ImageCollectionPlatform/SearchResultsPage/SearchBar.vue";
import SearchResultsDisplay from "@/components/ImageCollectionPlatform/SearchResultsPage/SearchResultsDisplay.vue";
import FilterOptions from "@/components/ImageCollectionPlatform/SearchResultsPage/FilterOptions.vue";
import Pagination from "@/components/ImageCollectionPlatform/SearchResultsPage/Pagination.vue";
import Footer from "@/components/ImageCollectionPlatform/SearchResultsPage/Footer.vue";
</script>
<style>
@import url("@/style.css");
</style>
    