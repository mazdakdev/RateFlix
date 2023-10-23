<template>
    <ion-page >
      <ion-header :translucent="true">
        <ion-toolbar>
          <ion-buttons slot="start">
            <ion-menu-button color="primary"></ion-menu-button>
          </ion-buttons>
          <ion-title>توسعه دهندگان</ion-title>
        </ion-toolbar>
      </ion-header>
  
      <ion-content class="ion-padding">
        <div class="container my-12 mx-auto md:px-6">
        <!-- Section: Design Block -->
        <section class="text-center">
            <h2 class="mb-12 text-3xl font-bold">
                با تیم آشنا شو !
            </h2>

            <div class="lg:gap-xl-12 grid gap-x-6 md:grid-cols-3 xl:grid-cols-3">
                <div class="mb-12">
                    <img src="https://avatars.githubusercontent.com/u/60855141?v=4"
                    class="mx-auto mb-4 rounded-full shadow-lg dark:shadow-black/20" alt="" style="max-width: 100px" />

                    <p class="mb-2 font-bold">Mazdak Pakaghideh</p>
                    <p class="text-neutral-500 dark:text-neutral-300">Team Member</p>
                </div>

                <div class="mb-12">
                    <img src="https://avatars.githubusercontent.com/u/117342306?v=4"
                    class="mx-auto mb-4 rounded-full shadow-lg dark:shadow-black/20" alt="" style="max-width: 100px" />

                    <p class="mb-2 font-bold">Mahbod ZamanPour</p>
                    <p class="text-neutral-500 dark:text-neutral-300">Team Member</p>
                </div>

                <div class="mb-12">
                    <img src="@/assets/images/saleh.jpg"
                    class="mx-auto mb-4 rounded-full shadow-lg dark:shadow-black/20" alt="" style="max-width: 100px" />
                    <p class="mb-2 font-bold">Saleh Talebi</p>
                    <p class="text-neutral-500 dark:text-neutral-300">
                        Team Member
                    </p>
                </div>
      
            </div>
        </section>
        <!-- Section: Design Block -->
        </div>
  
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
  