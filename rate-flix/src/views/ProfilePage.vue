<style scoped>
  .center {
    display: flex;
    align-items: center;
    justify-content: center;
  }
</style>

<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-title>حساب کاربری</ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content class="center">
    
      <div>
      <ion-avatar>
          <img alt="Silhouette of a person's head" src="https://ionicframework.com/docs/img/demos/avatar.svg" />

        </ion-avatar>
        <ion-avatar>
          <img alt="Silhouette of a person's head" src="https://ionicframework.com/docs/img/demos/avatar.svg" />

        </ion-avatar>
      </div>
  
      <ion-segment value="default">
    <ion-segment-button value="default">
      <ion-label>حساب کاربری</ion-label>
    </ion-segment-button>
    <ion-segment-button value="segment">
      <ion-label>اعلان ها</ion-label>
    </ion-segment-button>
  </ion-segment>

    </ion-content>
  </ion-page>
</template>

<script lang="ts">
  import { IonHeader, IonToolbar, IonTitle, IonContent, IonPage, IonLabel, IonSegment, IonSegmentButton, IonAvatar } from '@ionic/vue';


  export default {
    components: { IonHeader, IonToolbar, IonTitle, IonContent, IonPage, IonLabel, IonSegment, IonSegmentButton, IonAvatar },
  };

</script>