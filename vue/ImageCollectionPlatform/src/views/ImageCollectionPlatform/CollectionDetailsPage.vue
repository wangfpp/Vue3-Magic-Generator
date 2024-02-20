<template>
  <NavigationBar/>
  <ImageDisplay/>
  <DownloadButton/>
  <RelatedRecommendations/>
  <Footer/>
</template>

<script lang="ts" setup>
import NavigationBar from "@/components/ImageCollectionPlatform/HomePage/NavigationBar.vue";
import CollectionTitleAndDescription
  from "@/components/ImageCollectionPlatform/CollectionDetailsPage/CollectionTitleAndDescription.vue";
import ImageDisplay from "@/components/ImageCollectionPlatform/CollectionDetailsPage/ImageDisplay.vue";
import ArtistInformation from "@/components/ImageCollectionPlatform/CollectionDetailsPage/ArtistInformation.vue";
import DownloadButton from "@/components/ImageCollectionPlatform/CollectionDetailsPage/DownloadButton.vue";
import RelatedRecommendations
  from "@/components/ImageCollectionPlatform/CollectionDetailsPage/RelatedRecommendations.vue";
import Footer from "@/components/ImageCollectionPlatform/CollectionDetailsPage/Footer.vue";
</script>
<style>
@import url("@/style.css");
</style>
    