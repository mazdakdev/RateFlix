<template>
    <ion-page>
      <ion-header :translucent="true">
        <ion-toolbar>
          <ion-buttons slot="start">
            <ion-menu-button color="primary"></ion-menu-button>
          </ion-buttons>
          <ion-title>نتایج</ion-title>
        </ion-toolbar>
      </ion-header>

      <ion-content class="ion-padding">
        
        <div class="relative overflow-x-auto">
            <table class="w-full text-sm text-left text-gray-400 shadow-lg">
                <tbody>
                    <tr class="border-b bg-gray-900 border-gray-700">
                        <th scope="row" class="px-6 py-4 font-medium  whitespace-nowrap text-gray-200">
                          #1 toy story
                        </th>
                 
                    </tr>
                    <tr class="border-b bg-gray-900 border-gray-700">
                        <th scope="row" class="px-6 py-4 font-medium whitespace-nowrap text-white">
                           #2 jumanji
                        </th>
                  
                    </tr>
                    <tr class="bg-gray-900">
                        <th scope="row" class="px-6 py-4 font-medium whitespace-nowrap text-white">
                            #3 better call saul
                        </th>
                   
                    </tr>
                </tbody>
            </table>
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
  