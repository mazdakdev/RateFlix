<template>
  <ion-page>
    <ion-header>
      <ion-toolbar>
        <ion-title>Profile</ion-title>
      </ion-toolbar>
    </ion-header>

    <ion-content>
    


      <div class="container mx-auto">
      <div class="flex flex-col justify-center items-center mt-3">
        
        <img alt="Silhouette of a person's head" class="rounded-full w-16 h-16" src="https://ionicframework.com/docs/img/demos/avatar.svg" />
        <ion-label class="text-center mt-2">علی علیزاده</ion-label>
      </div>


        <div class="flex text-center justify-center mt-3">
          <div class="flex flex-col">
            <ion-label>1</ion-label>
            <ion-label >Following</ion-label>
          </div>
          <div class="flex flex-col ml-10">
            <ion-label>100k</ion-label>
            <ion-label >Follower</ion-label>
          </div>
        </div>


    
    <ion-list :inset="true" class="list mt-3">
      <ion-item :button="true" detail="false">
      <ion-label>
        <strong>Reset Password</strong>
      </ion-label>
      </ion-item>
        <ion-item>
          <ion-toggle>
            <ion-label>Enable two-step verfication</ion-label>
            <ion-note color="medium">Secure your account</ion-note>
          </ion-toggle>
        </ion-item>
      </ion-list>
    </div>

    </ion-content>
  </ion-page>
</template>


