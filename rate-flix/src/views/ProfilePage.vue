<style scoped>
.flex-container {
  display: flex;
  justify-content: center;
  align-items: center;
}
.flex-row{
  
  flex-direction: row;
}
.flex-col{
  flex-direction: column;
  
}
.profile-image{
  justify-content: right;
  align-items: right;
}

.leble{
  padding: 10px ;
}

.list{
  margin-left: 20%;
  margin-right: 20%;
}
</style>

<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-title>حساب کاربری</ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content>
    
      <div class="flex-container flex-col">
        <div class="flex-row">
          <ion-avatar class="profile-image">
            
            <img alt="Silhouette of a person's head" src="https://ionicframework.com/docs/img/demos/avatar.svg" />
            
          </ion-avatar>
          <ion-label>علی علیزاده</ion-label>
        </div>

        <div class="flex-container flex-row">
          <div>
            <ion-label class="leble">دنبال کننده: 10 هزار نفر</ion-label>
          </div>
          <div>

            <ion-label class="leble">دنبال شونده: 100 نفر</ion-label>
          </div>
        </div>

      </div>
  
      <ion-segment value="default">

        <ion-segment-button value="default">
          <ion-label>حساب کاربری</ion-label>
        </ion-segment-button>
        
        <ion-segment-button value="segment">
          <ion-label>اعلان ها</ion-label>
        </ion-segment-button>
    </ion-segment>

    
    <ion-list :inset="true" class="list">
      <ion-item :button="true" detail="false">
      <ion-label>
        <strong>تغییر رمز عبور</strong>
      </ion-label>
    </ion-item>
        <ion-item>
          <ion-toggle>
            <ion-label>فعالسازی احراز هویت دو مرحله ای</ion-label>
            <ion-note color="medium">حساب خود را ایمن کنید</ion-note>
          </ion-toggle>
        </ion-item>
        

      </ion-list>

    </ion-content>
  </ion-page>
</template>

<script lang="ts">
  import { IonHeader, IonToolbar, IonTitle, IonContent, IonPage, IonLabel, IonSegment, IonSegmentButton, IonAvatar } from '@ionic/vue';


  export default {
    components: { IonHeader, IonToolbar, IonTitle, IonContent, IonPage, IonLabel, IonSegment, IonSegmentButton, IonAvatar },
  };

</script>