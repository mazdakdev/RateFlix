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
                    <ion-col v-for="(movie, index) in movies" :key="movie.id" size="12" size-md="4" class="ion-align-items-center ion-justify-content-center">
                        <ion-card>
                            <img alt="Silhouette of mountains" :src="movie.photo" />
                            <ion-card-header>
                            <ion-card-title class="text-xl">{{ movie.title }}</ion-card-title>
                            <ion-card-subtitle>{{ movie.score }}</ion-card-subtitle>
                            </ion-card-header>

                            <ion-card-content>
                                {{ movie.comment }}
                            </ion-card-content>

                            <ion-button @click="openModal(index)" fill="clear">افزودن <ion-icon class="mr-1" :icon="addCircleOutline"></ion-icon></ion-button>
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
                        <ion-button @click="closeModal()">لغو</ion-button>
                    </ion-buttons>
                    </ion-toolbar>
                </ion-header>

                <ion-content class="ion-padding">

                    <div class="flex flex-col items-center">
                        <img  :src="moviePoster"
                        alt="Poster" class="w-32 h-32 h-auto text-center" />
                        <star-rating class="mt-1" read-only="true" star-size="20" rating="3.5" increment="0.01" rtl="true" text-class="hidden"></star-rating>
                    </div>
                    <ion-item class="mt-5">
                        <ion-label position="stacked">جستجوی فیلم</ion-label>
                        <ion-input v-model="searchQuery" @input="searchMovies" type="text" placeholder="The lord of the rings"></ion-input>
                    </ion-item>

                    <ion-list class="searchlist" v-if="showResults">
                        <ion-item  v-for="search in searchResult" :key="search.imdbID" @click="selectMovie(search)">{{ search.Title }}</ion-item>
                    </ion-list>

                    <ion-item class="mt-5"><ion-textarea  label="نظر شما" v-model="comment" labelPlacement="floating" placeholder="فیلم بسیار مهیج و جالبی هستش"></ion-textarea></ion-item>

                    <div class="flex mt-10 justify-center">
                        <ion-button color="tertiary" fill="outline">حدس امتیاز</ion-button>
                        <ion-button color="primary" @click="submitMovie" fill="outline">ثبت و ادامه</ion-button>
                    </div>
                </ion-content>
                
        </ion-modal>

        </ion-content>
    </ion-page>
</template>
  
<script setup lang="ts">
    import { IonButtons, IonContent, IonHeader, IonMenuButton, IonPage, IonTitle, IonToolbar } from '@ionic/vue';
    import { IonCard, IonCardContent, IonCardHeader, IonCardSubtitle, IonCardTitle, IonIcon} from '@ionic/vue';
    import { IonButton, IonModal, IonItem, IonInput, IonLabel, IonTextarea} from '@ionic/vue';
    import { addCircleOutline, arrowBackOutline, contractOutline } from 'ionicons/icons';
    import thumbnail from '@/assets/images/thumbnail.svg'
    import { ref, watch } from 'vue';
    import axios from 'axios';
    import StarRating from 'vue-star-rating'


    const movies = ref(Array.from({length: 6}, (_, index) => ({
        id: index + 1,
        title: 'بدون عنوان',
        comment: 'بدون نظر',
        photo: require('@/assets/images/post.png'),
        score: '0/0'
    })));

    const isOpen = ref(false);
    const searchQuery = ref('');
    const searchListClasses = ref('')
    const searchResult = ref([]);
    const moviePoster = ref(thumbnail);
    const showResults = ref(false);

    const currentMovieIndex = ref(0)
    const comment = ref('')

    const openModal = (index : any) => {
        isOpen.value = true;
        currentMovieIndex.value = index;
    }

    const closeModal = () => {
        isOpen.value = false;
        currentMovieIndex.value = 0;
    }

    const searchMovies = async () => {
        if (searchQuery.value) {
            try {
            const response = await axios.get('http://www.omdbapi.com', {
                params: {
                apikey: 'cbc2d94a',
                s: searchQuery.value,
                },
            });
            searchListClasses.value = '';
            searchResult.value = response.data.Search.slice(0, -5);
            showResults.value = true;

            }
            catch (error) {
                console.error(error);
            }
        } else {
            searchResult.value = [];
        }
    };

    const selectMovie = (movie: { Title: string; Poster: any; }) => {
        searchQuery.value = movie.Title;
        showResults.value = false;
        moviePoster.value = movie.Poster;

    };

    const submitMovie = () => {
       movies.value[currentMovieIndex.value].title = searchQuery.value;
       movies.value[currentMovieIndex.value].photo = moviePoster.value;
       movies.value[currentMovieIndex.value].comment = comment.value;
       comment.value = '';
       moviePoster.value = thumbnail;
       searchQuery.value = '';
       isOpen.value = false;
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

    @media (max-width: 767px) {
        ion-col {
            text-align: center !important;
        }
    }

    .searchlist{
        width: 70%;
    }
</style>
  