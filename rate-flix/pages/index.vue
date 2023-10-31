<template>
    <ion-page>
      <ion-content>
        <ion-tabs>
          <ion-router-outlet />
          
          <ion-tab-bar slot="bottom">
            <ion-tab-button tab="home" href="/home">
              <ion-icon :icon="ioniconsHomeOutline" />
              <ion-label>Home</ion-label>
            </ion-tab-button>
  
            <ion-tab-button tab="movies" href="/movies">
              <ion-icon :icon="ioniconsFilmOutline" />
              <ion-label>Movies</ion-label>
            </ion-tab-button>
  
            <ion-tab-button tab="explore" href="/explore">
              <ion-icon :icon="ioniconsCompassOutline" />
              <ion-label>Explore</ion-label>
            </ion-tab-button>
  
            <ion-tab-button tab="profile" href="/profile">
              <ion-icon :icon="ioniconsPersonOutline" />
              <ion-label>Profile</ion-label>
            </ion-tab-button>
          </ion-tab-bar>
        </ion-tabs>
      </ion-content>
    </ion-page>
  </template>
  