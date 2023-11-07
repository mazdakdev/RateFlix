<template>  
        <main class="flex-1 py-10  px-5 sm:px-10 overflow-y-auto h-screen">

            <header class=" font-bold text-lg flex items-center  gap-x-3 md:hidden mb-12 ">
                <span class="mr-6">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-7 w-7  text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h7" />
                      </svg>
                </span>
                <svg class="h-8 w-8 fill-red-600 shrink-0" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                    <path d="M10 15.5v-7c0-.41.47-.65.8-.4l4.67 3.5c.27.2.27.6 0 .8l-4.67 3.5c-.33.25-.8.01-.8-.4Zm11.96-4.45c.58 6.26-4.64 11.48-10.9 10.9 -4.43-.41-8.12-3.85-8.9-8.23 -.26-1.42-.19-2.78.12-4.04 .14-.58.76-.9 1.31-.7v0c.47.17.75.67.63 1.16 -.2.82-.27 1.7-.19 2.61 .37 4.04 3.89 7.25 7.95 7.26 4.79.01 8.61-4.21 7.94-9.12 -.51-3.7-3.66-6.62-7.39-6.86 -.83-.06-1.63.02-2.38.2 -.49.11-.99-.16-1.16-.64v0c-.2-.56.12-1.17.69-1.31 1.79-.43 3.75-.41 5.78.37 3.56 1.35 6.15 4.62 6.5 8.4ZM5.5 4C4.67 4 4 4.67 4 5.5 4 6.33 4.67 7 5.5 7 6.33 7 7 6.33 7 5.5 7 4.67 6.33 4 5.5 4Z"></path>
                </svg>        
                <div class="tracking-wide text-white flex-1">RateFlix<span class="text-red-600">.</span></div>

                <div class="relative items-center content-center flex ml-2">
                    <span class="text-gray-400 absolute left-4 cursor-pointer">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
                        </svg>
                    </span>
                    <input type="text" class="text-xs ring-1 bg-transparent ring-gray-200  focus:ring-red-300 pl-10 pr-5  text-white  py-3 rounded-full w-full outline-none focus:ring-1" placeholder="Search ...">
                </div>
            </header>
            <section>
                <nav class="flex space-x-6 font-medium">
                    <a href="#" class="hover:text-gray-700 text-white font-semibold">Home</a>
                    <a href="#" class="hover:text-gray-700 text-gray-400">TV Series</a>
                    <a href="#" class="hover:text-gray-700 text-gray-400">Movies</a>
                    <a href="#" class="hover:text-gray-700 text-gray-400">Animes</a>
                </nav>
            
                <Poster :genres="testGenres">The Inception</Poster>

            </section>

            <section class="mt-9">
                <div class="flex items-center justify-between">
                    <span class="font-semibold  text-base text-white">Top Stars</span>
                    <div class="flex items-center space-x-2 fill-gray-500">
                        <svg class="h-7 w-7 rounded-full border p-1 hover:border-red-600 hover:fill-red-600 fill-white " xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                            <path d="M13.293 6.293L7.58 12l5.7 5.7 1.41-1.42 -4.3-4.3 4.29-4.293Z"></path>
                        </svg>
                        <svg class="h-7 w-7 rounded-full border p-1 hover:border-red-600 hover:fill-red-600 fill-white " xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                            <path d="M10.7 17.707l5.7-5.71 -5.71-5.707L9.27 7.7l4.29 4.293 -4.3 4.29Z"></path>
                        </svg>
                    </div>
                </div>
               
           
                <div class="mt-4 grid grid-cols-2  sm:grid-cols-4 gap-x-5 gap-y-5">
                    <TopActor
                        image="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/WP_-_random_-5_%2814094372762%29.jpg/319px-WP_-_random_-5_%2814094372762%29.jpg"
                        movies="25"
                    >
                        Mohammad Ahamadi
                    </TopActor>
                    
                    <TopActor
                        image="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/WP_-_random_-5_%2814094372762%29.jpg/319px-WP_-_random_-5_%2814094372762%29.jpg"
                        movies="34"
                    >
                        Asghar Bbaei
                    </TopActor>
                    
                    <TopActor
                        image="https://img.zeit.de/kultur/film/2020-12/elliot-page-tranmann/wide__450x253__mobile__scale_1"
                        movies="15"
                    >
                        Joseph Babania
                    </TopActor>
                    
                    <TopActor
                        image="https://de.web.img3.acsta.net/c_310_420/pictures/16/01/19/11/06/274206.jpg"
                        movies="15"
                    >
                        Tom Hardy
                    </TopActor>   
                
                </div>
            </section>

            <section class="mt-9">
                <div class="flex items-center justify-between">
                    <span class="font-semibold text-base text-white">Similar Movies</span>
                    <div class="flex items-center space-x-2 fill-gray-500">
                        <svg class="h-7 w-7 rounded-full border p-1 hover:border-red-600  fill-white hover:fill-red-600" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                            <path d="M13.293 6.293L7.58 12l5.7 5.7 1.41-1.42 -4.3-4.3 4.29-4.293Z"></path>
                        </svg>
                        <svg class="h-7 w-7 rounded-full border p-1 hover:border-red-600 fill-white hover:fill-red-600" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                            <path d="M10.7 17.707l5.7-5.71 -5.71-5.707L9.27 7.7l4.29 4.293 -4.3 4.29Z"></path>
                        </svg>
                    </div>
                </div>
               
                <div class="mt-4 grid grid-cols-2 gap-y-5 sm:grid-cols-3 gap-x-5 ">
                    <MovieCard score="4" poster="https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg">The Lord of ...</MovieCard>
                    <MovieCard score="4" poster="https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg">The Lord of ...</MovieCard>
                    <MovieCard score="4" poster="https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg">The Lord of ...</MovieCard>
                </div>
            </section>

        </main>

  </template>
  
<script setup lang="ts">
    definePageMeta({
        layout: 'sidebar',
        middleware: 'auth'
    })

    const testGenres = ["Action", "Mystrious", "Romance"]
</script>