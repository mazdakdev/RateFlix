<template>
    <ion-page>
      <ion-header :translucent="true">
        <ion-toolbar>
          <ion-buttons slot="start">
            <ion-menu-button color="primary"></ion-menu-button>
          </ion-buttons>
          <ion-title>درباره</ion-title>
        </ion-toolbar>
      </ion-header>

      <ion-content class="ion-padding">
        <h1>About This App</h1>
        <p>Lorem, ipsum dolor sit amet consectetur adipisicing elit. Exercitationem voluptatum ipsa nisi. Commodi recusandae voluptatem quidem ut, magnam minima deserunt temporibus alias ipsum praesentium dolore, eveniet aut illum libero modi?</p>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Porro praesentium omnis qui suscipit quis officiis enim aperiam ratione sapiente veritatis explicabo expedita, pariatur illo eius consequuntur repellendus optio. Nobis, veritatis.</p>
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
  </style>
  