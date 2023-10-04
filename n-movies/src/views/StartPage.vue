<template>
    <ion-page>
        <ion-header :translucent="true">
            <ion-toolbar>
            <ion-buttons slot="start">
                <ion-menu-button color="primary"></ion-menu-button>
            </ion-buttons>
            <ion-title>به فیلمات امتیاز بده ⭐️ </ion-title>
            </ion-toolbar>
        </ion-header>

        <ion-content class="ion-padding">
            <ion-grid>
                <ion-row>
                    <ion-col v-for="movie in movies" :key="movie.id" size="6" size-md="4" class="ion-align-items-center ion-justify-content-center i">
                        <ion-card>
                            <img alt="Silhouette of mountains" :src="movie.photo" />
                            <ion-card-header>
                            <ion-card-title class="text-xl">{{ movie.title }}</ion-card-title>
                            <ion-card-subtitle>{{ movie.score }}</ion-card-subtitle>
                            </ion-card-header>

                            <ion-card-content>
                                {{ movie.comment }}
                            </ion-card-content>

                            <ion-button id="open-modal" fill="clear">افزودن <ion-icon class="mr-1" :icon="addCircleOutline"></ion-icon></ion-button>
                        </ion-card>
                    </ion-col>
                </ion-row>
            </ion-grid>

            <ion-modal ref="modal" trigger="open-modal" @willDismiss="onWillDismiss">
                <ion-header>
                    <ion-toolbar>
                    <ion-buttons slot="start">
                        <ion-button @click="cancel()">لغو</ion-button>
                    </ion-buttons>
                    <ion-title>اضافه کردن فیلم</ion-title>
                    <ion-buttons slot="end">
                        <ion-button :strong="true" @click="confirm()">تایید</ion-button>
                    </ion-buttons>
                    </ion-toolbar>
                </ion-header>
                <ion-content class="ion-padding">
                    <ion-item>
                        <ion-label position="stacked">اسم فیلم را جستجو کنید</ion-label>
                        <ion-input ref="input" type="text" placeholder="The Lord of the Rings"></ion-input>
                    </ion-item>

                    <ion-item class="mt-3">
                        <ion-label position="stacked">نظرتان ؟</ion-label>
                        <ion-textarea placeholder="به نظرم فیلم جالبی بود اما میتونستن تو انتخاب بازیگرا بیشتر دقت کنن" ></ion-textarea>
                    </ion-item>
                </ion-content>
             </ion-modal>

        </ion-content>
    </ion-page>
</template>
  
<script setup lang="ts">
    import { IonButtons, IonContent, IonHeader, IonMenuButton, IonPage, IonTitle, IonToolbar } from '@ionic/vue';
    import { IonCard, IonCardContent, IonCardHeader, IonCardSubtitle, IonCardTitle, IonIcon} from '@ionic/vue';
    import { IonButton, IonModal, IonItem, IonInput, IonLabel, IonTextarea} from '@ionic/vue';
    import { addCircleOutline } from 'ionicons/icons';
    import { ref } from 'vue';

    const movies = ref(Array.from({length: 5}, (_, index) => ({
        id: index + 1,
        title: 'بدون عنوان',
        comment: 'بدون نظر',
        photo: require('@/assets/images/post.png'),
        score: '0/0'
    })));

    const modal = ref();
  const input = ref();

  const cancel = () => modal.value.$el.dismiss(null, 'cancel');
  const message = ref('This modal example uses triggers to automatically open a modal when the button is clicked.');

  const confirm = () => {
    const name = input.value.$el.value;
    modal.value.$el.dismiss(name, 'confirm');
  };

  const onWillDismiss = (ev: CustomEvent<OverlayEventDetail>) => {
    if (ev.detail.role === 'confirm') {
      message.value = `Hello, ${ev.detail.data}!`;
    }
  };

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

    ion-content{
        --background: #fff url('@/assets/images/poster.jpeg') no-repeat center center / cover;
    }


</style>
  