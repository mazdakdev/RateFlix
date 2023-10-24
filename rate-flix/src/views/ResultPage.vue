<template>
  <ion-page >
    <ion-header :translucent="true">
      <ion-toolbar>
        <ion-buttons slot="start">
          <ion-menu-button color="primary"></ion-menu-button>
        </ion-buttons>
        <ion-title>نتایج</ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content class="ion-padding">
      
      <div class="grid md:grid-cols-3 grid-cols-1">
                <ion-card v-for="(movie, index) in movies" :key="index" class="flex flex-col text-center md:text-right">
                                <img alt="movie's poster" :src="movie.poster" />
                                <ion-card-header>
                                    <ion-card-title class="text-xl">{{ movie.title }}</ion-card-title>
                                    <ion-card-subtitle> سال ساخت: {{ movie.year }}</ion-card-subtitle>
                                </ion-card-header>

                                <ion-card-content class="h-24 overflow-hidden">
                                    {{ movie.genres }}
                                </ion-card-content>
                </ion-card>
      </div>

    </ion-content>

  </ion-page>

</template>

<script setup lang="ts">
  import { IonButtons, IonContent, IonHeader, IonMenuButton, IonPage, IonTitle, IonToolbar } from '@ionic/vue';
  import { useApiResultsStore } from '@/store/apiResults'
  import { ref, onMounted} from 'vue'
  import axios from 'axios';
  

  const movies = ref([]) 
  const apiResultsStore = useApiResultsStore()

  onMounted(async () => {
    movies.value = apiResultsStore.results

      for (const movie of movies.value) {
        const response = await axios.get('https://omdbapi.com', {
          params: {
            apikey: 'cbc2d94a',
            s: movie['title'],
          },});
      
        movie.poster = response.data.Search[0].Poster;

      }
  });



</script>

<style scoped>
#container {
  text-align: center;
  position: absolute;
  left: 0;
  right: 0;
  top: 50%;
  transform: translateY(-50%);
}

#container strong {
  font-size: 20px;
  line-height: 26px;
}

#container p {
  font-size: 16px;
  line-height: 22px;
  color: #8c8c8c;
  margin: 0;
}

#container a {
  text-decoration: none;
}
</style>
