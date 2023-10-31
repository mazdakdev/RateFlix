<template>
  <ion-page>
    <ion-tabs>
      <ion-router-outlet></ion-router-outlet>
      <ion-tab-bar slot="bottom">
        
        <ion-tab-button tab="profile" href="/profile">
          <ion-icon :icon="person" />
          <ion-label>حساب کاربری</ion-label>
        </ion-tab-button>
        
        <ion-tab-button tab="library" href="/library">
          <ion-icon :icon="library" />
          <ion-label>Library</ion-label>
        </ion-tab-button>
        
        <ion-tab-button tab="home" href="/home">
          <ion-icon :icon="home" />
          <ion-label>خانه</ion-label>
        </ion-tab-button>

        <ion-tab-button tab="search" href="/search">
          <ion-icon :icon="search" />
          <ion-label>جستجو</ion-label>
        </ion-tab-button>
        
        <ion-tab-button tab="setting" href="/setting">
          <ion-icon :icon="settings" />
          <ion-label>تنظیمات</ion-label>
        </ion-tab-button>

      </ion-tab-bar>
    </ion-tabs>
  </ion-page>
</template>

<script lang="ts">
  import { IonPage, IonTabs, IonRouterOutlet, IonTabBar, IonTabButton, IonLabel, IonIcon } from '@ionic/vue';

  import { home, person, library, search, settings } from 'ionicons/icons';

  export default {
    components: { IonPage, IonTabs, IonRouterOutlet, IonTabBar, IonTabButton, IonLabel, IonIcon },
    data() {
      return {
        home,
        person,
        library,
        search,
        settings,
      };
    },
  };
</script>

<ion-icon name="person-circle-outline"></ion-icon>