<template>
    <ion-page>
      <ion-header :translucent="true">
        <ion-toolbar>
          <ion-buttons slot="start">
            <ion-menu-button color="primary"></ion-menu-button>
          </ion-buttons>
          <ion-title>بیا شروع کنیم، نکنیم؟</ion-title>
        </ion-toolbar>
      </ion-header>

      <ion-content class="ion-padding">
        <h1 class="text-xl">فیلمتو انتخاب کن، بهش امتیاز بده</h1>
        <h4 class="mr-3 text-sm text-gray-200">-- یا حتی می تونیم تصادفی پیش بریم </h4>
        <ion-grid>
    <ion-row>
        <ion-col size="6" size-md="4">
            <ion-card>
                <img alt="Silhouette of mountains" src="https://ionicframework.com/docs/img/demos/card-media.png" />
                <ion-card-header>
                <ion-card-title class="text-xl">آواتار</ion-card-title>
                <ion-card-subtitle>5/5</ion-card-subtitle>
                </ion-card-header>

                <ion-card-content>
                جالبه
                </ion-card-content>

                <ion-button fill="clear">افزودن <ion-icon class="mr-1" :icon="addCircleOutline"></ion-icon></ion-button>
            </ion-card>
        </ion-col>
    </ion-row>
  </ion-grid>
        
        </ion-content>
  

    </ion-page>

  </template>
  
  <script lang="ts">
  import { IonButtons, IonContent, IonHeader, IonMenuButton, IonPage, IonTitle, IonToolbar } from '@ionic/vue';
  import { IonCard, IonCardContent, IonCardHeader, IonCardSubtitle, IonCardTitle, IonIcon} from '@ionic/vue';
  import { addCircleOutline } from 'ionicons/icons';
  import { defineComponent } from 'vue';

  export default defineComponent({
    components: { IonCard, IonCardContent, IonCardHeader, IonCardSubtitle, IonCardTitle, IonIcon },
    setup(){
        return {addCircleOutline}
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
  