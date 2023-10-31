<style scoped>
  .main {
    overflow-x: scroll 
  }
  .scrolling-wrapper {
  overflow-x: scroll;
  overflow-y: hidden;
  white-space: nowrap;
}
.scrolling-wrapper .card {
  display: inline-block;
}

.scrolling-wrapper-flexbox {
  display: flex;
  flex-wrap: nowrap;
  overflow-x: auto;
}
.scrolling-wrapper-flexbox .card {
  flex: 0 0 auto;
  margin-right: 3px;
}

.card {
  border: 2px solid #4a4848;
  width: 150px;
  height: 75px;
  background: black;
}

.scrolling-wrapper, .scrolling-wrapper-flexbox {
  height: 80px;
  margin-bottom: 20px;
  width: 100%;
  -webkit-overflow-scrolling: touch;
}
.scrolling-wrapper::-webkit-scrollbar, .scrolling-wrapper-flexbox::-webkit-scrollbar {
  display: none;
}
</style>

<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-title>خانه</ion-title>
      </ion-toolbar>
    </ion-header>
    <ion-content>
      <div class="">
        <div class="">
        <ion-label>پیشنهادی</ion-label>
          <div class="scrolling-wrapper">
            <div class="card">
              <h2>Card</h2>
            </div>
            <div class="card"><h2>Card</h2></div>
            <div class="card"><h2>Card</h2></div>
            <div class="card"><h2>Card</h2></div>
            <div class="card"><h2>Card</h2></div>
            <div class="card"><h2>Card</h2></div>
            <div class="card"><h2>Card</h2></div>
            <div class="card"><h2>Card</h2></div>
            <div class="card"><h2>Card</h2></div>
          </div>
      </div>
      </div>

      <div class="">
        <ion-label>داغ</ion-label>
          <div class="scrolling-wrapper">
            <div class="card">
              <h2>Card</h2>
            </div>
            <div class="card"><h2>Card</h2></div>
            <div class="card"><h2>Card</h2></div>
            <div class="card"><h2>Card</h2></div>
            <div class="card"><h2>Card</h2></div>
            <div class="card"><h2>Card</h2></div>
            <div class="card"><h2>Card</h2></div>
            <div class="card"><h2>Card</h2></div>
            <div class="card"><h2>Card</h2></div>
          </div>
      </div>
    </ion-content>
  </ion-page>
</template>

<script lang="ts">
  import { IonHeader, IonToolbar, IonTitle, IonContent, IonPage } from '@ionic/vue';

  export default {
    components: { IonHeader, IonToolbar, IonTitle, IonContent, IonPage },
  };
</script>