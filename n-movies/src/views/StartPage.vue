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
            <ion-grid >
                <ion-row>
                    <ion-col v-for="movie in movies" :key="movie.id" size="11" size-md="4">
                        <ion-card>
                            <img alt="Silhouette of mountains" :src="movie.photo" />
                            <ion-card-header>
                            <ion-card-title class="text-xl">{{ movie.title }}</ion-card-title>
                            <ion-card-subtitle>{{ movie.score }}</ion-card-subtitle>
                            </ion-card-header>

                            <ion-card-content>
                                {{ movie.comment }}
                            </ion-card-content>

                            <ion-button fill="clear">افزودن <ion-icon class="mr-1" :icon="addCircleOutline"></ion-icon></ion-button>
                        </ion-card>
                    </ion-col>
                </ion-row>
            </ion-grid>

        </ion-content>
    </ion-page>
</template>
  
<script lang="ts">
  import { IonButtons, IonContent, IonHeader, IonMenuButton, IonPage, IonTitle, IonToolbar } from '@ionic/vue';
  import { IonCard, IonCardContent, IonCardHeader, IonCardSubtitle, IonCardTitle, IonIcon} from '@ionic/vue';
  import { addCircleOutline, returnUpBack } from 'ionicons/icons';
  import { defineComponent } from 'vue';

  export default{
    components: { IonCard, IonCardContent, IonCardHeader, IonCardSubtitle, IonCardTitle, IonIcon },

    data(){
        return{
            addCircleOutline,
            movies: Array.from({length: 5}, (_, index) => ({
                id: index + 1,
                title: 'بدون عنوان',
                comment: 'بدون نظر',
                photo: require('@/assets/images/post.png'),
                score: '0/0',
            })),
        };
    },
    methods: {
        addMovie(){
            //TODO: Updated the movie card
        }
    }

  }

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
  