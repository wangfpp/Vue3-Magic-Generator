<template>
  <NavigationBar/>
  <ImageCollectionRecommendation/>
  <LatestImageCollectionDisplay/>
  <ArtistIntroduction/>
  <Footer/>
</template>

<script lang="ts" setup>
import NavigationBar from "@/components/ImageCollectionPlatform/HomePage/NavigationBar.vue";
import ImageCollectionRecommendation
  from "@/components/ImageCollectionPlatform/HomePage/ImageCollectionRecommendation.vue";
import LatestImageCollectionDisplay
  from "@/components/ImageCollectionPlatform/HomePage/LatestImageCollectionDisplay.vue";
import ArtistIntroduction from "@/components/ImageCollectionPlatform/HomePage/ArtistIntroduction.vue";
import UserLoginRegistration from "@/components/ImageCollectionPlatform/HomePage/UserLoginRegistration.vue";
import SearchBar from "@/components/ImageCollectionPlatform/HomePage/SearchBar.vue";
import Footer from "@/components/ImageCollectionPlatform/HomePage/Footer.vue";
</script>
<style>
@import url("@/style.css");
</style>
    