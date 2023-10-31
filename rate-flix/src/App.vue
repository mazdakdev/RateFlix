<template>
  <ion-app>
    <ion-router-outlet></ion-router-outlet>
    <ion-avatar>
    <img alt="Silhouette of a person's head" src="https://ionicframework.com/docs/img/demos/avatar.svg" />
  </ion-avatar>
  </ion-app>
</template>

<script lang="ts">
  
  import { IonApp, IonRouterOutlet } from '@ionic/vue';
  
  import { defineComponent } from 'vue';
  
  import Navigation from './components/BottomNavigation.vue';
  
  document.dir = "rtl";
  
  export default defineComponent({
    name: 'App',
    components: { IonApp, IonRouterOutlet },
  });
</script>