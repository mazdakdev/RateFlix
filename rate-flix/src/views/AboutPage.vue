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
        <h1>درباره این برنامه</h1>
        <p class="mt-4">توسط این برنامه شما می توانید فیلم های مورد علاقه ی خود را انتخاب کرده برای انها نظری بنویسید و بعدش ما یه لیستی از فیلم هایی که فکر می کنیم شما دوست دارید رو در اخیتارتون می زاریم</p>
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
  