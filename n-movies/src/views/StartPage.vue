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
                    <ion-col v-for="movie in movies" :key="movie.id" size="12" size-md="4" class="ion-align-items-center ion-justify-content-center">
                        <ion-card>
                            <img alt="Silhouette of mountains" :src="movie.photo" />
                            <ion-card-header>
                            <ion-card-title class="text-xl">{{ movie.title }}</ion-card-title>
                            <ion-card-subtitle>{{ movie.score }}</ion-card-subtitle>
                            </ion-card-header>

                            <ion-card-content>
                                {{ movie.comment }}
                            </ion-card-content>

                            <ion-button @click="setOpen(true)" fill="clear">افزودن <ion-icon class="mr-1" :icon="addCircleOutline"></ion-icon></ion-button>
                        </ion-card>
                    </ion-col>

                    
                    <ion-col  class="ion-text-center mt-6">
                        <ion-button shape="round" color="medium" fill="clear">ادامه <ion-icon class="mr-1" :icon="arrowBackOutline"></ion-icon></ion-button>
                    </ion-col>
                    
                    
                </ion-row>
            </ion-grid>
            <ion-modal :is-open="isOpen">
                <ion-header>
                    <ion-toolbar>
                    <ion-title>اضافه کردن فیلم</ion-title>
                    <ion-buttons slot="end">
                        <ion-button @click="setOpen(false)">لغو</ion-button>
                    </ion-buttons>
                    </ion-toolbar>
                </ion-header>

                <ion-content class="ion-padding">
                    <ion-item>
                        <ion-label position="stacked">جستجوی فیلم</ion-label>
                        <ion-input v-model="searchQuery" type="text" placeholder="The lord of the rings"></ion-input>
                    </ion-item>

                    <ion-list>
                       
                    </ion-list>
                </ion-content>
        </ion-modal>

        </ion-content>
    </ion-page>
</template>
  
<script setup lang="ts">
    import { IonButtons, IonContent, IonHeader, IonMenuButton, IonPage, IonTitle, IonToolbar } from '@ionic/vue';
    import { IonCard, IonCardContent, IonCardHeader, IonCardSubtitle, IonCardTitle, IonIcon} from '@ionic/vue';
    import { IonButton, IonModal, IonItem, IonInput, IonLabel, IonTextarea} from '@ionic/vue';
    import { addCircleOutline, arrowBackOutline } from 'ionicons/icons';
    import { ref, watch } from 'vue';

    const movies = ref(Array.from({length: 6}, (_, index) => ({
        id: index + 1,
        title: 'بدون عنوان',
        comment: 'بدون نظر',
        photo: require('@/assets/images/post.png'),
        score: '0/0'
    })));

    const isOpen = ref(false);
    const setOpen = (open: boolean) => (isOpen.value = open);
    const searchQuery = ref('')
    
    // watch(searchQuery, (newValue, oldValue) => {
        
    // });


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

    @media (max-width: 767px) {
        ion-col {
            text-align: center !important;
        }
    }
</style>
  