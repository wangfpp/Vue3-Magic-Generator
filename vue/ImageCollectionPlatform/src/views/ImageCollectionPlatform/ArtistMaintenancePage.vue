<template>
  <NavigationBar/>
  <ArtistList/>
  <AddNewArtistForm/>
  <Footer/>
</template>

<script lang="ts" setup>
import NavigationBar from "@/components/ImageCollectionPlatform/HomePage/NavigationBar.vue";
import ArtistList from "@/components/ImageCollectionPlatform/ArtistMaintenancePage/ArtistList.vue";
import AddNewArtistForm from "@/components/ImageCollectionPlatform/ArtistMaintenancePage/AddNewArtistForm.vue";
import EditAndDeleteOptions from "@/components/ImageCollectionPlatform/ArtistMaintenancePage/EditAndDeleteOptions.vue";
import Footer from "@/components/ImageCollectionPlatform/ArtistMaintenancePage/Footer.vue";
</script>
<style>
@import url("@/style.css");
</style>
    