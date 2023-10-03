<template>
    <ion-page>
      <ion-header :translucent="true">
        <ion-toolbar>
          <ion-buttons slot="start">
            <ion-menu-button color="primary"></ion-menu-button>
          </ion-buttons>
          <ion-title>Let's Start Shall We.. ?</ion-title>
        </ion-toolbar>
      </ion-header>

      <ion-content class="ion-padding">
        <h1>Choose</h1>
        <ion-grid>
            <ion-row justify-content-center align-items-center>
                <ion-col size="6">
                    <ion-button shape="round" fill="outline">Randomly</ion-button>
                </ion-col>
                <ion-col size="6">
                    <ion-button shape="round" fill="outline">Manually</ion-button>
                </ion-col>
            </ion-row>
        </ion-grid>

        <h2>How To Choose</h2>
        <h3 class="ml-3">Random Mode</h3>
        <p class="ml-3">Lorem ipsum dolor sit amet consectetur adipisicing elit. Atque numquam eaque reprehenderit ullam rerum est perspiciatis aspernatur ipsum harum explicabo? In quidem nesciunt nam earum beatae dolores ipsam reprehenderit adipisci.</p>
        <h3 class="ml-3">Manuall Mode</h3>
        <p class="ml-3">Lorem ipsum dolor sit amet consectetur adipisicing elit. Atque numquam eaque reprehenderit ullam rerum est perspiciatis aspernatur ipsum harum explicabo? In quidem nesciunt nam earum beatae dolores ipsam reprehenderit adipisci.</p>
         
      </ion-content>

    </ion-page>

  </template>
  
  <script setup lang="ts">
  import { IonButtons, IonContent, IonHeader, IonMenuButton, IonPage, IonTitle, IonToolbar } from '@ionic/vue';
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

  .ml-3{
    margin-left: 0.75rem;
  }

  .ml-4{
    margin-left: 1rem;
  }
  </style>
  