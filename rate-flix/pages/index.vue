<template>
    <div class="flex min-h-screen  2xl:max-w-screen-2xl 2xl:mx-auto 2xl:border-x-2 2xl:border-gray-200 dark:2xl:border-zinc-700 ">
        <!-- Left Sidebar -->
        <aside class=" w-1/6 py-10 pl-10  min-w-min  border-r border-gray-300 dark:border-zinc-700  hidden md:block ">

            <div class=" font-bold text-lg flex items-center gap-x-3">  
                <div class="tracking-wide dark:text-white">RateFlix</div>
            </div>

            <!-- Menu -->
            <div class="mt-12 flex flex-col gap-y-4 text-gray-500 fill-gray-500 text-sm">
                <div class="text-gray-400/70  font-medium uppercase">Menu</div>
                <a class="flex items-center space-x-2 py-1 dark:text-white  font-semibold  border-r-4 border-r-red-600 pr-20 " href="#">                  
                    <svg class="h-5 w-5 fill-red-600 " xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" >
                        <path d="M5 22h14v0c1.1 0 2-.9 2-2v-9 0c0-.27-.11-.53-.29-.71l-8-8v0c-.4-.39-1.02-.39-1.41 0l-8 8h0c-.2.18-.3.44-.3.71v9 0c0 1.1.89 2 2 2Zm5-2v-5h4v5Zm-5-8.59l7-7 7 7V20h-3v-5 0c0-1.11-.9-2-2-2h-4v0c-1.11 0-2 .89-2 2v5H5Z"></path>
                    </svg>
                    <span>Home</span>
                </a>
                <a class="flex items-center space-x-2 py-1  group hover:border-r-4 text-gray-200 hover:border-r-red-600 hover:font-semibold dark:hover:text-white " href="#">                  
                    <svg class="h-5 w-5 group-hover:fill-red-600" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                        <g>
                            <path d="M19 2H9c-1.11 0-2 .89-2 2v5.586l-4.707 4.7v0c-.4.39-.4 1.02 0 1.41 .18.18.44.29.7.29v5 0c0 .55.44 1 1 1h16v0c.55 0 1-.45 1-1v-17c0-1.11-.9-2-2-2Zm-8 18H5v-5.586l3-3 3 3V20Zm8 0h-6v-4 0c.55 0 .99-.45 1-1 0-.27-.11-.53-.3-.72L8.99 9.57V3.984h10v16Z"></path>
                            <path d="M11 6h2v2h-2Zm4 0h2v2h-2Zm0 4.03h2v1.96h-2Zm0 3.96h2v2h-2Zm-8 1h2v2H7Z"></path>
                        </g>
                    </svg>
                    <span>Community</span>
                </a>
                <a class=" flex items-center space-x-2 py-1  group hover:border-r-4  text-gray-200 hover:border-r-red-600 hover:font-semibold dark:hover:text-white" href="#">                  
                    <svg class="h-5 w-5 group-hover:fill-red-600" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                        <g>
                            <path d="M12 2C6.48 2 2 6.48 2 12c0 5.51 4.48 10 10 10 5.51 0 10-4.49 10-10 0-5.52-4.49-10-10-10Zm0 18c-4.42 0-8-3.59-8-8 0-4.42 3.58-8 8-8 4.41 0 8 3.58 8 8 0 4.41-3.59 8-8 8Z"></path>
                            <path d="M8 16l5.991-2 2-6 -6 2Z"></path>
                        </g>
                    </svg>
                    <span>Discovery</span>
                </a>
                <a class=" flex items-center space-x-2 py-1  group hover:border-r-4  text-gray-200 hover:border-r-red-600 hover:font-semibold dark:hover:text-white " href="#">
                    <svg class="h-5 w-5 group-hover:fill-red-600" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                        <g>
                            <path d="M12 2C6.48 2 2 6.48 2 12c0 5.51 4.48 10 10 10 5.51 0 10-4.49 10-10 0-5.52-4.49-10-10-10Zm0 18c-4.42 0-8-3.59-8-8 0-4.42 3.58-8 8-8 4.41 0 8 3.58 8 8 0 4.41-3.59 8-8 8Z"></path>
                            <path d="M13 7h-2v5.414l3.29 3.29 1.41-1.42 -2.71-2.71Z"></path>
                        </g>
                    </svg>
                    <span>Coming Soon</span>
                </a>
                
                <div class="mt-8 text-gray-400/70  font-medium uppercase">Social</div>
                <a class=" flex items-center space-x-2 py-1  group hover:border-r-4  text-gray-200 hover:border-r-red-600 hover:font-semibold dark:hover:text-white " href="#">                  
                    <svg class="h-5 w-5 group-hover:fill-red-600" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                        <path d="M12 2v0C9.23 2 7 4.23 7 7c0 2.76 2.23 5 5 5 2.76 0 5-2.24 5-5v0c0-2.77-2.24-5-5-5Zm0 8v0c-1.66 0-3-1.35-3-3 0-1.66 1.34-3 3-3 1.65 0 3 1.34 3 3v0c0 1.65-1.35 3-3 3Zm9 11v-1 0c0-3.87-3.14-7-7-7h-4v0c-3.87 0-7 3.13-7 7v1h2v-1 0c0-2.77 2.23-5 5-5h4v0c2.76 0 5 2.23 5 5v1Z"></path>
                    </svg>
                    <span>Profile</span>
                </a>
                <a class=" flex items-center space-x-2 py-1  group hover:border-r-4  text-gray-200 hover:border-r-red-600 hover:font-semibold dark:hover:text-white " href="#">                  
                    <svg class="h-5 w-5 group-hover:fill-red-600" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                        <g>
                            <path d="M16.6 11.04v-.001c.6-1.04.87-2.25.75-3.44 -.18-1.79-1.18-3.37-2.81-4.44l-1.11 1.66c1.11.742 1.8 1.79 1.91 2.974l-.001 0c.11 1.1-.29 2.2-1.08 2.98l-1.2 1.19 1.61.47c4.23 1.24 4.28 5.49 4.28 5.53h2c0-1.79-.96-5.285-4.4-6.952Z"></path>
                            <path d="M9.5 12c2.2 0 4-1.8 4-4 0-2.21-1.8-4-4-4 -2.21 0-4 1.79-4 4 0 2.2 1.79 4 4 4Zm0-6c1.1 0 2 .89 2 2 0 1.1-.9 2-2 2 -1.11 0-2-.9-2-2 0-1.11.89-2 2-2Zm1.5 7H8c-3.31 0-6 2.69-6 6v1h2v-1c0-2.21 1.79-4 4-4h3c2.2 0 4 1.79 4 4v1h2v-1c0-3.31-2.7-6-6-6Z"></path>
                        </g>
                    </svg>
                    <span>Friends</span>
                </a> 
                <a class=" flex items-center space-x-2 py-1  group hover:border-r-4  text-gray-200 hover:border-r-red-600 hover:font-semibold dark:hover:text-white " href="#">                  
                    <svg class="h-5 w-5 group-hover:fill-red-600" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                        <g>
                            <path d="M12 2v0C6.47 2 2 6.47 2 12c0 5.52 4.47 10 10 10 5.52 0 10-4.48 10-10v-.001c0-5.53-4.48-10-10-10Zm0 18v0c-4.42 0-8-3.59-8-8 0-4.42 3.58-8 8-8 4.41 0 8 3.58 8 8v0c0 4.41-3.59 8-8 8Z"></path>
                            <path d="M12 8v0c-2.21 0-4 1.79-4 4 0 2.2 1.79 4 4 4 2.2 0 4-1.8 4-4v0c0-2.21-1.8-4-4-4Zm0 6v0c-1.11 0-2-.9-2-2 0-1.11.89-2 2-2 1.1 0 2 .89 2 2v0c0 1.1-.9 2-2 2Z"></path>
                        </g>
                    </svg>
                    <span>Media</span>
                </a>
               
            <div class="mt-8  font-medium uppercase">General</div>
                <a class=" flex items-center space-x-2 py-1  group hover:border-r-4 text-gray-200 hover:border-r-red-600 hover:font-semibold dark:hover:text-white" href="#">                  
                    <svg class="h-5 w-5 group-hover:fill-red-600" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                        <g>
                            <path d="M16 13v-2H7V8l-5 4 5 4v-3Z"></path>
                            <path d="M20 3h-9c-1.11 0-2 .89-2 2v4h2V5h9v14h-9v-4H9v4c0 1.1.89 2 2 2h9c1.1 0 2-.9 2-2V5c0-1.11-.9-2-2-2Z"></path>
                        </g>
                    </svg>
                    <span>Logout</span>
                </a> 
                <a class=" flex items-center space-x-2 py-1  group hover:border-r-4 text-gray-200 hover:border-r-red-600 hover:font-semibold dark:hover:text-white" href="#">                  
                    <svg class="h-5 w-5 group-hover:fill-red-600" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                        <g>
                            <path d="M16 13v-2H7V8l-5 4 5 4v-3Z"></path>
                            <path d="M20 3h-9c-1.11 0-2 .89-2 2v4h2V5h9v14h-9v-4H9v4c0 1.1.89 2 2 2h9c1.1 0 2-.9 2-2V5c0-1.11-.9-2-2-2Z"></path>
                        </g>
                    </svg>
                    <span>Logout</span>
                </a> 

            </div><!-- /Menu -->

        </aside><!-- /Left Sidebar -->

        <main class=" flex-1 py-10  px-5 sm:px-10 ">

            <header class=" font-bold text-lg flex items-center  gap-x-3 md:hidden mb-12 ">
                <span class="mr-6">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-7 w-7 text-gray-700 dark:text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
                        <path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h16M4 18h7" />
                      </svg>
                </span>
                <svg class="h-8 w-8 fill-red-600 shrink-0" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                    <path d="M10 15.5v-7c0-.41.47-.65.8-.4l4.67 3.5c.27.2.27.6 0 .8l-4.67 3.5c-.33.25-.8.01-.8-.4Zm11.96-4.45c.58 6.26-4.64 11.48-10.9 10.9 -4.43-.41-8.12-3.85-8.9-8.23 -.26-1.42-.19-2.78.12-4.04 .14-.58.76-.9 1.31-.7v0c.47.17.75.67.63 1.16 -.2.82-.27 1.7-.19 2.61 .37 4.04 3.89 7.25 7.95 7.26 4.79.01 8.61-4.21 7.94-9.12 -.51-3.7-3.66-6.62-7.39-6.86 -.83-.06-1.63.02-2.38.2 -.49.11-.99-.16-1.16-.64v0c-.2-.56.12-1.17.69-1.31 1.79-.43 3.75-.41 5.78.37 3.56 1.35 6.15 4.62 6.5 8.4ZM5.5 4C4.67 4 4 4.67 4 5.5 4 6.33 4.67 7 5.5 7 6.33 7 7 6.33 7 5.5 7 4.67 6.33 4 5.5 4Z"></path>
                </svg>        
                <div class="tracking-wide dark:text-white flex-1">RateFlix<span class="text-red-600">.</span></div>

                <div class="relative items-center content-center flex ml-2">
                    <span class="text-gray-400 absolute left-4 cursor-pointer">
                        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
                        </svg>
                    </span>
                    <input type="text" class="text-xs ring-1 bg-transparent ring-gray-200 dark:ring-zinc-600 focus:ring-red-300 pl-10 pr-5 text-gray-600 dark:text-white  py-3 rounded-full w-full outline-none focus:ring-1" placeholder="Search ...">
                </div>
            </header>
           
            <section>
                <nav class="flex space-x-6 text-gray-400 font-medium">
                    <a href="#" class="hover:text-gray-700 text-gray-300 dark:hover:text-white">TV Series</a>
                    <a href="#" class="hover:text-gray-700 text-gray-300 dark:text-white font-semibold">Movies</a>
                    <a href="#" class="hover:text-gray-700 text-gray-300 dark:hover:text-white ">Animes</a>
                </nav>

                <div class="flex flex-col justify-between mt-4 bg-black/10 bg-blend-multiply rounded-3xl h-80 overflow-hidden bg-cover bg-center px-7 pt-4 pb-6 text-white"
                 style="background-image: url('https://mazyar1128.github.io/tailwindcss-movie-dashboard/images/inception.jpg');" >
                    <!-- <img class="object-cover w-full h-full" src="images/inception.jpg" alt=""> -->
                    <div class="flex -space-x-1 items-center ">
                        <img class="rounded-full w-7 h-7 shadow-lg border border-white"
                            src="https://api.lorem.space/image/face?w=32&amp;h=32&amp;hash=zsrj8csk" alt="" srcset="">
                        <img class="rounded-full w-7 h-7 shadow-lg border border-white"
                            src="https://api.lorem.space/image/face?w=32&amp;h=32&amp;hash=zsrj8cck"
                            alt="" srcset="">
                        <img class="rounded-full w-7 h-7 shadow-lg border border-white"
                            src="https://api.lorem.space/image/face?w=32&amp;h=32&amp;hash=zsfj8cck"
                            alt="" srcset="">
                        <span class="pl-4 text-xs drop-shadow-lg">+8 friends are watching</span>
                    </div>
                    
                    <div class="bg-gradient-to-r from-black/30 to-transparent -mx-7 -mb-6 px-7 pb-6 pt-2">
                        <span class="uppercase text-3xl font-semibold drop-shadow-lg ">Inception</span>
                        <div class="mt-2">
                            <a href="#" class="text-gray-200 text-xs">Action</a>,
                            <a href="#" class="text-gray-200 text-xs">Adventure</a>,
                            <a href="#" class="text-gray-200 text-xs">Sci-Fi</a>
                        </div>
                        <div class="mt-4 flex space-x-3 items-center">
                            <a href="#" class="px-5 py-2.5 bg-red-600 hover:bg-red-700 text-white rounded-lg text-xs inline-block">Watch</a>
                            <a href="#" class="p-2.5 bg-gray-800/80 rounded-lg hover:bg-red-600">
                                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
                                    <path fill-rule="evenodd" d="M10 3a1 1 0 011 1v5h5a1 1 0 110 2h-5v5a1 1 0 11-2 0v-5H4a1 1 0 110-2h5V4a1 1 0 011-1z" clip-rule="evenodd" />
                                </svg>
                            </a>
                        </div>
                    </div>
                </div>
            </section>

            <section class="mt-9">
                <div class="flex items-center justify-between">
                    <span class="font-semibold text-gray-700 text-base dark:text-white">Top Stars</span>
                    <div class="flex items-center space-x-2 fill-gray-500">
                        <svg class="h-7 w-7 rounded-full border p-1 hover:border-red-600 hover:fill-red-600 dark:fill-white dark:hover:fill-red-600" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                            <path d="M13.293 6.293L7.58 12l5.7 5.7 1.41-1.42 -4.3-4.3 4.29-4.293Z"></path>
                        </svg>
                        <svg class="h-7 w-7 rounded-full border p-1 hover:border-red-600 hover:fill-red-600 dark:fill-white dark:hover:fill-red-600" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                            <path d="M10.7 17.707l5.7-5.71 -5.71-5.707L9.27 7.7l4.29 4.293 -4.3 4.29Z"></path>
                        </svg>
                    </div>
                </div>
               
                <div class="mt-4 grid grid-cols-2  sm:grid-cols-4 gap-x-5 gap-y-5">
                  
                    <div class="relative rounded-xl overflow-hidden ">
                        <img src="data:image/jpeg;base64,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" class="object-cover w-full h-full -z-10" alt="">
                        <div class="absolute top-0 h-full w-full bg-gradient-to-t from-black/50 p-3 flex flex-col justify-between">
                         
                                <a href="#" class="p-2.5 bg-gray-800/80 rounded-lg text-white self-end hover:bg-red-600/80">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
                                        <path fill-rule="evenodd" d="M10 3a1 1 0 011 1v5h5a1 1 0 110 2h-5v5a1 1 0 11-2 0v-5H4a1 1 0 110-2h5V4a1 1 0 011-1z" clip-rule="evenodd" />
                                    </svg>
                                </a>
                            
                            <div class="self-center flex flex-col items-center space-y-2">
                                <span class="capitalize text-white font-medium drop-shadow-md">Ahmad Mousavi</span>
                                <span class="text-gray-300 text-xs">+24 Movies</span>

                            </div>
                        </div>
                    </div>      <div class="relative rounded-xl overflow-hidden ">
                        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cb/WP_-_random_-5_%2814094372762%29.jpg/319px-WP_-_random_-5_%2814094372762%29.jpg" class="object-cover w-full h-full -z-10" alt="">
                        <div class="absolute top-0 h-full w-full bg-gradient-to-t from-black/50 p-3 flex flex-col justify-between">
                         
                                <a href="#" class="p-2.5 bg-gray-800/80 rounded-lg text-white self-end hover:bg-red-600/80">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
                                        <path fill-rule="evenodd" d="M10 3a1 1 0 011 1v5h5a1 1 0 110 2h-5v5a1 1 0 11-2 0v-5H4a1 1 0 110-2h5V4a1 1 0 011-1z" clip-rule="evenodd" />
                                    </svg>
                                </a>
                            
                            <div class="self-center flex flex-col items-center space-y-2">
                                <span class="capitalize text-white font-medium drop-shadow-md">Joseph Gordon-Levitt</span>
                                <span class="text-gray-300 text-xs">+24 Movies</span>

                            </div>
                        </div>
                    </div>
                    <div class="relative rounded-xl overflow-hidden ">
                        <img src="https://img.zeit.de/kultur/film/2020-12/elliot-page-tranmann/wide__450x253__mobile__scale_1" class="object-cover h-full w-full -z-10" alt="">
                        <div class="absolute top-0 h-full w-full bg-gradient-to-t from-black/50 p-3 flex flex-col justify-between">
                         
                                <a href="#" class="p-2.5 bg-gray-800/80 rounded-lg text-white self-end hover:bg-red-600/80">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
                                        <path fill-rule="evenodd" d="M10 3a1 1 0 011 1v5h5a1 1 0 110 2h-5v5a1 1 0 11-2 0v-5H4a1 1 0 110-2h5V4a1 1 0 011-1z" clip-rule="evenodd" />
                                    </svg>
                                </a>
                            
                            <div class="self-center flex flex-col items-center space-y-2">
                                <span class="capitalize text-white font-medium drop-shadow-md">Elliot Page</span>
                                <span class="text-gray-300 text-xs">+10 Movies</span>

                            </div>
                        </div>
                    </div>
                    <div class="relative rounded-xl overflow-hidden ">
                        <img src="https://de.web.img3.acsta.net/c_310_420/pictures/16/01/19/11/06/274206.jpg" class="object-cover h-full w-full -z-10" alt="">
                        <div class="absolute top-0 h-full w-full bg-gradient-to-t from-black/50 p-3 flex flex-col justify-between">
                         
                                <a href="#" class="p-2.5 bg-gray-800/80 rounded-lg text-white self-end hover:bg-red-600/80">
                                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" viewBox="0 0 20 20" fill="currentColor">
                                        <path fill-rule="evenodd" d="M10 3a1 1 0 011 1v5h5a1 1 0 110 2h-5v5a1 1 0 11-2 0v-5H4a1 1 0 110-2h5V4a1 1 0 011-1z" clip-rule="evenodd" />
                                    </svg>
                                </a>
                            
                            <div class="self-center flex flex-col items-center space-y-2">
                                <span class="capitalize text-white font-medium drop-shadow-md">Tom Hardy</span>
                                <span class="text-gray-300 text-xs">+27 Movies</span>

                            </div>
                        </div>
                    </div>
                </div>
            </section>

            <section class="mt-9">
                <div class="flex items-center justify-between">
                    <span class="font-semibold text-gray-700 text-base dark:text-white">Similar Movies</span>
                    <div class="flex items-center space-x-2 fill-gray-500">
                        <svg class="h-7 w-7 rounded-full border p-1 hover:border-red-600 hover:fill-red-600 dark:fill-white dark:hover:fill-red-600" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                            <path d="M13.293 6.293L7.58 12l5.7 5.7 1.41-1.42 -4.3-4.3 4.29-4.293Z"></path>
                        </svg>
                        <svg class="h-7 w-7 rounded-full border p-1 hover:border-red-600 hover:fill-red-600 dark:fill-white dark:hover:fill-red-600" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
                            <path d="M10.7 17.707l5.7-5.71 -5.71-5.707L9.27 7.7l4.29 4.293 -4.3 4.29Z"></path>
                        </svg>
                    </div>
                </div>
               
                <div class="mt-4 grid grid-cols-2 gap-y-5 sm:grid-cols-3 gap-x-5 ">
                    <div class="flex flex-col rounded-xl overflow-hidden aspect-square border dark:border-zinc-600">
                        <img src="https://upload.wikimedia.org/wikipedia/en/1/14/Tenet_movie_poster.jpg" class=" h-4/5 object-cover w-full  " alt="">
                        <div class="w-full h-1/5 bg-white dark:bg-zinc-800 dark:text-white px-3 flex items-center justify-between border-t-2 border-t-red-600">
                         <span class="capitalize  font-medium truncate">Tenet</span>
                         <div class="flex space-x-2 items-center text-xs">
                            <svg class="w-8 h-5" xmlns="http://www.w3.org/2000/svg" width="64" height="32" viewBox="0 0 64 32" version="1.1"><g fill="#F5C518"><rect x="0" y="0" width="100%" height="100%" rx="4"></rect></g><g transform="translate(8.000000, 7.000000)" fill="#000000" fill-rule="nonzero"><polygon points="0 18 5 18 5 0 0 0"></polygon><path d="M15.6725178,0 L14.5534833,8.40846934 L13.8582008,3.83502426 C13.65661,2.37009263 13.4632474,1.09175121 13.278113,0 L7,0 L7,18 L11.2416347,18 L11.2580911,6.11380679 L13.0436094,18 L16.0633571,18 L17.7583653,5.8517865 L17.7707076,18 L22,18 L22,0 L15.6725178,0 Z"></path><path d="M24,18 L24,0 L31.8045586,0 C33.5693522,0 35,1.41994415 35,3.17660424 L35,14.8233958 C35,16.5777858 33.5716617,18 31.8045586,18 L24,18 Z M29.8322479,3.2395236 C29.6339219,3.13233348 29.2545158,3.08072342 28.7026524,3.08072342 L28.7026524,14.8914865 C29.4312846,14.8914865 29.8796736,14.7604764 30.0478195,14.4865461 C30.2159654,14.2165858 30.3021941,13.486105 30.3021941,12.2871637 L30.3021941,5.3078959 C30.3021941,4.49404499 30.272014,3.97397442 30.2159654,3.74371416 C30.1599168,3.5134539 30.0348852,3.34671372 29.8322479,3.2395236 Z"></path><path d="M44.4299079,4.50685823 L44.749518,4.50685823 C46.5447098,4.50685823 48,5.91267586 48,7.64486762 L48,14.8619906 C48,16.5950653 46.5451816,18 44.749518,18 L44.4299079,18 C43.3314617,18 42.3602746,17.4736618 41.7718697,16.6682739 L41.4838962,17.7687785 L37,17.7687785 L37,0 L41.7843263,0 L41.7843263,5.78053556 C42.4024982,5.01015739 43.3551514,4.50685823 44.4299079,4.50685823 Z M43.4055679,13.2842155 L43.4055679,9.01907814 C43.4055679,8.31433946 43.3603268,7.85185468 43.2660746,7.63896485 C43.1718224,7.42607505 42.7955881,7.2893916 42.5316822,7.2893916 C42.267776,7.2893916 41.8607934,7.40047379 41.7816216,7.58767002 L41.7816216,9.01907814 L41.7816216,13.4207851 L41.7816216,14.8074788 C41.8721037,15.0130276 42.2602358,15.1274059 42.5316822,15.1274059 C42.8031285,15.1274059 43.1982131,15.0166981 43.281155,14.8074788 C43.3640968,14.5982595 43.4055679,14.0880581 43.4055679,13.2842155 Z"></path></g></svg>
                            <span>7.4</span>
                        </div>
                        </div>
                    </div>
                    <div class="flex flex-col rounded-xl overflow-hidden aspect-square border dark:border-zinc-600">
                        <img src="https://upload.wikimedia.org/wikipedia/en/f/fc/Fight_Club_poster.jpg" class=" h-4/5 object-cover w-full  " alt="">
                        <div class="w-full h-1/5 bg-white dark:bg-zinc-800 dark:text-white px-3 flex items-center justify-between border-t-2 border-t-red-600">
                         <span class="capitalize  font-medium truncate">Fight Club</span>
                         <div class="flex space-x-2 items-center text-xs">
                            <svg class="w-8 h-5" xmlns="http://www.w3.org/2000/svg" width="64" height="32" viewBox="0 0 64 32" version="1.1"><g fill="#F5C518"><rect x="0" y="0" width="100%" height="100%" rx="4"></rect></g><g transform="translate(8.000000, 7.000000)" fill="#000000" fill-rule="nonzero"><polygon points="0 18 5 18 5 0 0 0"></polygon><path d="M15.6725178,0 L14.5534833,8.40846934 L13.8582008,3.83502426 C13.65661,2.37009263 13.4632474,1.09175121 13.278113,0 L7,0 L7,18 L11.2416347,18 L11.2580911,6.11380679 L13.0436094,18 L16.0633571,18 L17.7583653,5.8517865 L17.7707076,18 L22,18 L22,0 L15.6725178,0 Z"></path><path d="M24,18 L24,0 L31.8045586,0 C33.5693522,0 35,1.41994415 35,3.17660424 L35,14.8233958 C35,16.5777858 33.5716617,18 31.8045586,18 L24,18 Z M29.8322479,3.2395236 C29.6339219,3.13233348 29.2545158,3.08072342 28.7026524,3.08072342 L28.7026524,14.8914865 C29.4312846,14.8914865 29.8796736,14.7604764 30.0478195,14.4865461 C30.2159654,14.2165858 30.3021941,13.486105 30.3021941,12.2871637 L30.3021941,5.3078959 C30.3021941,4.49404499 30.272014,3.97397442 30.2159654,3.74371416 C30.1599168,3.5134539 30.0348852,3.34671372 29.8322479,3.2395236 Z"></path><path d="M44.4299079,4.50685823 L44.749518,4.50685823 C46.5447098,4.50685823 48,5.91267586 48,7.64486762 L48,14.8619906 C48,16.5950653 46.5451816,18 44.749518,18 L44.4299079,18 C43.3314617,18 42.3602746,17.4736618 41.7718697,16.6682739 L41.4838962,17.7687785 L37,17.7687785 L37,0 L41.7843263,0 L41.7843263,5.78053556 C42.4024982,5.01015739 43.3551514,4.50685823 44.4299079,4.50685823 Z M43.4055679,13.2842155 L43.4055679,9.01907814 C43.4055679,8.31433946 43.3603268,7.85185468 43.2660746,7.63896485 C43.1718224,7.42607505 42.7955881,7.2893916 42.5316822,7.2893916 C42.267776,7.2893916 41.8607934,7.40047379 41.7816216,7.58767002 L41.7816216,9.01907814 L41.7816216,13.4207851 L41.7816216,14.8074788 C41.8721037,15.0130276 42.2602358,15.1274059 42.5316822,15.1274059 C42.8031285,15.1274059 43.1982131,15.0166981 43.281155,14.8074788 C43.3640968,14.5982595 43.4055679,14.0880581 43.4055679,13.2842155 Z"></path></g></svg>
                            <span>8.8</span>
                        </div>
                        </div>
                    </div>
                    <div class="flex flex-col rounded-xl overflow-hidden aspect-square border dark:border-zinc-600">
                        <img src="https://upload.wikimedia.org/wikipedia/en/8/8e/Dune_%282021_film%29.jpg" class=" h-4/5 object-cover w-full  " alt="">
                        <div class="w-full h-1/5 bg-white dark:bg-zinc-800 dark:text-white px-3 flex items-center justify-between border-t-2 border-t-red-600">
                         <span class="capitalize  font-medium truncate">Dune</span>
                         <div class="flex space-x-2 items-center text-xs">
                            <svg class="w-8 h-5" xmlns="http://www.w3.org/2000/svg" width="64" height="32" viewBox="0 0 64 32" version="1.1"><g fill="#F5C518"><rect x="0" y="0" width="100%" height="100%" rx="4"></rect></g><g transform="translate(8.000000, 7.000000)" fill="#000000" fill-rule="nonzero"><polygon points="0 18 5 18 5 0 0 0"></polygon><path d="M15.6725178,0 L14.5534833,8.40846934 L13.8582008,3.83502426 C13.65661,2.37009263 13.4632474,1.09175121 13.278113,0 L7,0 L7,18 L11.2416347,18 L11.2580911,6.11380679 L13.0436094,18 L16.0633571,18 L17.7583653,5.8517865 L17.7707076,18 L22,18 L22,0 L15.6725178,0 Z"></path><path d="M24,18 L24,0 L31.8045586,0 C33.5693522,0 35,1.41994415 35,3.17660424 L35,14.8233958 C35,16.5777858 33.5716617,18 31.8045586,18 L24,18 Z M29.8322479,3.2395236 C29.6339219,3.13233348 29.2545158,3.08072342 28.7026524,3.08072342 L28.7026524,14.8914865 C29.4312846,14.8914865 29.8796736,14.7604764 30.0478195,14.4865461 C30.2159654,14.2165858 30.3021941,13.486105 30.3021941,12.2871637 L30.3021941,5.3078959 C30.3021941,4.49404499 30.272014,3.97397442 30.2159654,3.74371416 C30.1599168,3.5134539 30.0348852,3.34671372 29.8322479,3.2395236 Z"></path><path d="M44.4299079,4.50685823 L44.749518,4.50685823 C46.5447098,4.50685823 48,5.91267586 48,7.64486762 L48,14.8619906 C48,16.5950653 46.5451816,18 44.749518,18 L44.4299079,18 C43.3314617,18 42.3602746,17.4736618 41.7718697,16.6682739 L41.4838962,17.7687785 L37,17.7687785 L37,0 L41.7843263,0 L41.7843263,5.78053556 C42.4024982,5.01015739 43.3551514,4.50685823 44.4299079,4.50685823 Z M43.4055679,13.2842155 L43.4055679,9.01907814 C43.4055679,8.31433946 43.3603268,7.85185468 43.2660746,7.63896485 C43.1718224,7.42607505 42.7955881,7.2893916 42.5316822,7.2893916 C42.267776,7.2893916 41.8607934,7.40047379 41.7816216,7.58767002 L41.7816216,9.01907814 L41.7816216,13.4207851 L41.7816216,14.8074788 C41.8721037,15.0130276 42.2602358,15.1274059 42.5316822,15.1274059 C42.8031285,15.1274059 43.1982131,15.0166981 43.281155,14.8074788 C43.3640968,14.5982595 43.4055679,14.0880581 43.4055679,13.2842155 Z"></path></g></svg>
                            <span>8.1</span>
                        </div>
                        </div>
                    </div>
                    

                  
                </div>
            </section>

        </main>

        <!-- Right Sidebar -->
        <aside class=" w-1/5 py-10 px-10  min-w-min  border-l border-gray-300 dark:border-zinc-700 hidden lg:block ">

            <div class="relative items-center content-center flex">
                <span class="text-gray-400 absolute left-4 cursor-pointer">
                    <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
                    </svg>
                </span>
                <input type="text" class="text-xs ring-1 bg-transparent ring-gray-200 dark:ring-zinc-600 focus:ring-red-300 pl-10 pr-5 text-gray-600 dark:text-white  py-3 rounded-full w-full outline-none focus:ring-1" placeholder="Search ...">
            </div>

            <div class="mt-10">
                <span class="font-semibold text-gray-700 dark:text-white">Popular Movies</span>
                <ul class="mt-4 text-gray-400 text-xs space-y-3">
                    <li class="flex space-y-3 space-x-3 ">
                        <img src="https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg" class="w-1/3 rounded-md" alt="">
                        <div class="flex flex-col justify-between  ">
                            <div class="flex flex-col space-y-1">
                                <span class="text-gray-700 dark:text-white font-semibold">The Shawshank Redemption</span>
                                <span class="text-xxs hidden xl:block">Drama</span>
                            </div>
                            <div class="flex space-x-2 items-center">
                                <svg class="w-8 h-5" xmlns="http://www.w3.org/2000/svg" width="64" height="32" viewBox="0 0 64 32" version="1.1"><g fill="#F5C518"><rect x="0" y="0" width="100%" height="100%" rx="4"></rect></g><g transform="translate(8.000000, 7.000000)" fill="#000000" fill-rule="nonzero"><polygon points="0 18 5 18 5 0 0 0"></polygon><path d="M15.6725178,0 L14.5534833,8.40846934 L13.8582008,3.83502426 C13.65661,2.37009263 13.4632474,1.09175121 13.278113,0 L7,0 L7,18 L11.2416347,18 L11.2580911,6.11380679 L13.0436094,18 L16.0633571,18 L17.7583653,5.8517865 L17.7707076,18 L22,18 L22,0 L15.6725178,0 Z"></path><path d="M24,18 L24,0 L31.8045586,0 C33.5693522,0 35,1.41994415 35,3.17660424 L35,14.8233958 C35,16.5777858 33.5716617,18 31.8045586,18 L24,18 Z M29.8322479,3.2395236 C29.6339219,3.13233348 29.2545158,3.08072342 28.7026524,3.08072342 L28.7026524,14.8914865 C29.4312846,14.8914865 29.8796736,14.7604764 30.0478195,14.4865461 C30.2159654,14.2165858 30.3021941,13.486105 30.3021941,12.2871637 L30.3021941,5.3078959 C30.3021941,4.49404499 30.272014,3.97397442 30.2159654,3.74371416 C30.1599168,3.5134539 30.0348852,3.34671372 29.8322479,3.2395236 Z"></path><path d="M44.4299079,4.50685823 L44.749518,4.50685823 C46.5447098,4.50685823 48,5.91267586 48,7.64486762 L48,14.8619906 C48,16.5950653 46.5451816,18 44.749518,18 L44.4299079,18 C43.3314617,18 42.3602746,17.4736618 41.7718697,16.6682739 L41.4838962,17.7687785 L37,17.7687785 L37,0 L41.7843263,0 L41.7843263,5.78053556 C42.4024982,5.01015739 43.3551514,4.50685823 44.4299079,4.50685823 Z M43.4055679,13.2842155 L43.4055679,9.01907814 C43.4055679,8.31433946 43.3603268,7.85185468 43.2660746,7.63896485 C43.1718224,7.42607505 42.7955881,7.2893916 42.5316822,7.2893916 C42.267776,7.2893916 41.8607934,7.40047379 41.7816216,7.58767002 L41.7816216,9.01907814 L41.7816216,13.4207851 L41.7816216,14.8074788 C41.8721037,15.0130276 42.2602358,15.1274059 42.5316822,15.1274059 C42.8031285,15.1274059 43.1982131,15.0166981 43.281155,14.8074788 C43.3640968,14.5982595 43.4055679,14.0880581 43.4055679,13.2842155 Z"></path></g></svg>
                                <span>9.2</span>
                            </div>
                        </div>
                    </li>
                    <li class="flex space-x-3 ">
                        <img src="https://upload.wikimedia.org/wikipedia/en/1/1c/The_Dark_Knight_%282008_film%29.jpg" class="object-cover w-1/3 rounded-md" alt="">
                        <div class="flex flex-col justify-between  ">
                            <div class="flex flex-col space-y-1">
                                <span class="text-gray-700 dark:text-white font-semibold">The Dark Knight</span>
                                <span class="text-xxs hidden xl:block">Action, Crime, Drama</span>
                            </div>
                            <div class="flex space-x-2 items-center">
                                <svg class="w-8 h-5" xmlns="http://www.w3.org/2000/svg" width="64" height="32" viewBox="0 0 64 32" version="1.1"><g fill="#F5C518"><rect x="0" y="0" width="100%" height="100%" rx="4"></rect></g><g transform="translate(8.000000, 7.000000)" fill="#000000" fill-rule="nonzero"><polygon points="0 18 5 18 5 0 0 0"></polygon><path d="M15.6725178,0 L14.5534833,8.40846934 L13.8582008,3.83502426 C13.65661,2.37009263 13.4632474,1.09175121 13.278113,0 L7,0 L7,18 L11.2416347,18 L11.2580911,6.11380679 L13.0436094,18 L16.0633571,18 L17.7583653,5.8517865 L17.7707076,18 L22,18 L22,0 L15.6725178,0 Z"></path><path d="M24,18 L24,0 L31.8045586,0 C33.5693522,0 35,1.41994415 35,3.17660424 L35,14.8233958 C35,16.5777858 33.5716617,18 31.8045586,18 L24,18 Z M29.8322479,3.2395236 C29.6339219,3.13233348 29.2545158,3.08072342 28.7026524,3.08072342 L28.7026524,14.8914865 C29.4312846,14.8914865 29.8796736,14.7604764 30.0478195,14.4865461 C30.2159654,14.2165858 30.3021941,13.486105 30.3021941,12.2871637 L30.3021941,5.3078959 C30.3021941,4.49404499 30.272014,3.97397442 30.2159654,3.74371416 C30.1599168,3.5134539 30.0348852,3.34671372 29.8322479,3.2395236 Z"></path><path d="M44.4299079,4.50685823 L44.749518,4.50685823 C46.5447098,4.50685823 48,5.91267586 48,7.64486762 L48,14.8619906 C48,16.5950653 46.5451816,18 44.749518,18 L44.4299079,18 C43.3314617,18 42.3602746,17.4736618 41.7718697,16.6682739 L41.4838962,17.7687785 L37,17.7687785 L37,0 L41.7843263,0 L41.7843263,5.78053556 C42.4024982,5.01015739 43.3551514,4.50685823 44.4299079,4.50685823 Z M43.4055679,13.2842155 L43.4055679,9.01907814 C43.4055679,8.31433946 43.3603268,7.85185468 43.2660746,7.63896485 C43.1718224,7.42607505 42.7955881,7.2893916 42.5316822,7.2893916 C42.267776,7.2893916 41.8607934,7.40047379 41.7816216,7.58767002 L41.7816216,9.01907814 L41.7816216,13.4207851 L41.7816216,14.8074788 C41.8721037,15.0130276 42.2602358,15.1274059 42.5316822,15.1274059 C42.8031285,15.1274059 43.1982131,15.0166981 43.281155,14.8074788 C43.3640968,14.5982595 43.4055679,14.0880581 43.4055679,13.2842155 Z"></path></g></svg>
                                <span>9.1</span>
                            </div>
                        </div>
                    </li>
                    <li class="flex space-x-3 ">
                        <img src="https://m.media-amazon.com/images/I/81vZ6tNxuoL._SY500_.jpg" class="object-cover w-1/3 rounded-md" alt="">
                        <div class="flex flex-col justify-between  ">
                            <div class="flex flex-col space-y-1">
                                <span class="text-gray-700 dark:text-white font-semibold">John Wick 4</span>
                                <span class="text-xxs hidden xl:block">Action, Crime, Thriller</span>
                            </div>
                            <div class="flex space-x-2 items-center">
                                <svg class="w-8 h-5" xmlns="http://www.w3.org/2000/svg" width="64" height="32" viewBox="0 0 64 32" version="1.1"><g fill="#F5C518"><rect x="0" y="0" width="100%" height="100%" rx="4"></rect></g><g transform="translate(8.000000, 7.000000)" fill="#000000" fill-rule="nonzero"><polygon points="0 18 5 18 5 0 0 0"></polygon><path d="M15.6725178,0 L14.5534833,8.40846934 L13.8582008,3.83502426 C13.65661,2.37009263 13.4632474,1.09175121 13.278113,0 L7,0 L7,18 L11.2416347,18 L11.2580911,6.11380679 L13.0436094,18 L16.0633571,18 L17.7583653,5.8517865 L17.7707076,18 L22,18 L22,0 L15.6725178,0 Z"></path><path d="M24,18 L24,0 L31.8045586,0 C33.5693522,0 35,1.41994415 35,3.17660424 L35,14.8233958 C35,16.5777858 33.5716617,18 31.8045586,18 L24,18 Z M29.8322479,3.2395236 C29.6339219,3.13233348 29.2545158,3.08072342 28.7026524,3.08072342 L28.7026524,14.8914865 C29.4312846,14.8914865 29.8796736,14.7604764 30.0478195,14.4865461 C30.2159654,14.2165858 30.3021941,13.486105 30.3021941,12.2871637 L30.3021941,5.3078959 C30.3021941,4.49404499 30.272014,3.97397442 30.2159654,3.74371416 C30.1599168,3.5134539 30.0348852,3.34671372 29.8322479,3.2395236 Z"></path><path d="M44.4299079,4.50685823 L44.749518,4.50685823 C46.5447098,4.50685823 48,5.91267586 48,7.64486762 L48,14.8619906 C48,16.5950653 46.5451816,18 44.749518,18 L44.4299079,18 C43.3314617,18 42.3602746,17.4736618 41.7718697,16.6682739 L41.4838962,17.7687785 L37,17.7687785 L37,0 L41.7843263,0 L41.7843263,5.78053556 C42.4024982,5.01015739 43.3551514,4.50685823 44.4299079,4.50685823 Z M43.4055679,13.2842155 L43.4055679,9.01907814 C43.4055679,8.31433946 43.3603268,7.85185468 43.2660746,7.63896485 C43.1718224,7.42607505 42.7955881,7.2893916 42.5316822,7.2893916 C42.267776,7.2893916 41.8607934,7.40047379 41.7816216,7.58767002 L41.7816216,9.01907814 L41.7816216,13.4207851 L41.7816216,14.8074788 C41.8721037,15.0130276 42.2602358,15.1274059 42.5316822,15.1274059 C42.8031285,15.1274059 43.1982131,15.0166981 43.281155,14.8074788 C43.3640968,14.5982595 43.4055679,14.0880581 43.4055679,13.2842155 Z"></path></g></svg>
                                <span>7.4</span>
                            </div>
                        </div>
                    </li>
                    <li class="pt-1">
                        <a href="#" class="px-5 py-2.5 bg-red-600  hover:bg-red-700 rounded-lg text-center font-medium block text-white">See More</a>
                    </li>

                </ul>
            </div>
            <div class="mt-10">
                <span class="font-semibold text-gray-700 dark:text-white">Favorites</span>
                <ul class="mt-4 text-gray-400 text-xs space-y-3">
                    <li class="flex space-x-3 ">
                        <img src="https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg" class="object-cover w-1/3 rounded-md" alt="">
                        <div class="flex flex-col justify-between  ">
                            <div class="flex flex-col space-y-1">
                                <span class="text-gray-700 dark:text-white font-semibold">The Matrix</span>
                                <span class="text-xxs hidden xl:block">Action, Sci-Fi</span>
                            </div>
                            <div class="flex space-x-2 items-center">
                                <svg class="w-8 h-5" xmlns="http://www.w3.org/2000/svg" width="64" height="32" viewBox="0 0 64 32" version="1.1"><g fill="#F5C518"><rect x="0" y="0" width="100%" height="100%" rx="4"></rect></g><g transform="translate(8.000000, 7.000000)" fill="#000000" fill-rule="nonzero"><polygon points="0 18 5 18 5 0 0 0"></polygon><path d="M15.6725178,0 L14.5534833,8.40846934 L13.8582008,3.83502426 C13.65661,2.37009263 13.4632474,1.09175121 13.278113,0 L7,0 L7,18 L11.2416347,18 L11.2580911,6.11380679 L13.0436094,18 L16.0633571,18 L17.7583653,5.8517865 L17.7707076,18 L22,18 L22,0 L15.6725178,0 Z"></path><path d="M24,18 L24,0 L31.8045586,0 C33.5693522,0 35,1.41994415 35,3.17660424 L35,14.8233958 C35,16.5777858 33.5716617,18 31.8045586,18 L24,18 Z M29.8322479,3.2395236 C29.6339219,3.13233348 29.2545158,3.08072342 28.7026524,3.08072342 L28.7026524,14.8914865 C29.4312846,14.8914865 29.8796736,14.7604764 30.0478195,14.4865461 C30.2159654,14.2165858 30.3021941,13.486105 30.3021941,12.2871637 L30.3021941,5.3078959 C30.3021941,4.49404499 30.272014,3.97397442 30.2159654,3.74371416 C30.1599168,3.5134539 30.0348852,3.34671372 29.8322479,3.2395236 Z"></path><path d="M44.4299079,4.50685823 L44.749518,4.50685823 C46.5447098,4.50685823 48,5.91267586 48,7.64486762 L48,14.8619906 C48,16.5950653 46.5451816,18 44.749518,18 L44.4299079,18 C43.3314617,18 42.3602746,17.4736618 41.7718697,16.6682739 L41.4838962,17.7687785 L37,17.7687785 L37,0 L41.7843263,0 L41.7843263,5.78053556 C42.4024982,5.01015739 43.3551514,4.50685823 44.4299079,4.50685823 Z M43.4055679,13.2842155 L43.4055679,9.01907814 C43.4055679,8.31433946 43.3603268,7.85185468 43.2660746,7.63896485 C43.1718224,7.42607505 42.7955881,7.2893916 42.5316822,7.2893916 C42.267776,7.2893916 41.8607934,7.40047379 41.7816216,7.58767002 L41.7816216,9.01907814 L41.7816216,13.4207851 L41.7816216,14.8074788 C41.8721037,15.0130276 42.2602358,15.1274059 42.5316822,15.1274059 C42.8031285,15.1274059 43.1982131,15.0166981 43.281155,14.8074788 C43.3640968,14.5982595 43.4055679,14.0880581 43.4055679,13.2842155 Z"></path></g></svg>
                                <span>8.7</span>
                            </div>
                        </div>
                    </li>
                    <li class="flex space-x-3 ">
                        <img src="https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg" class="object-cover w-1/3 rounded-md" alt="">
                        <div class="flex flex-col justify-between  ">
                            <div class="flex flex-col space-y-1">
                                <span class="text-gray-700 dark:text-white font-semibold">Interstellar</span>
                                <span class="text-xxs hidden xl:block">Adventure, Crime, Sci-Fi</span>
                            </div>
                            <div class="flex space-x-2 items-center">
                                <svg class="w-8 h-5" xmlns="http://www.w3.org/2000/svg" width="64" height="32" viewBox="0 0 64 32" version="1.1"><g fill="#F5C518"><rect x="0" y="0" width="100%" height="100%" rx="4"></rect></g><g transform="translate(8.000000, 7.000000)" fill="#000000" fill-rule="nonzero"><polygon points="0 18 5 18 5 0 0 0"></polygon><path d="M15.6725178,0 L14.5534833,8.40846934 L13.8582008,3.83502426 C13.65661,2.37009263 13.4632474,1.09175121 13.278113,0 L7,0 L7,18 L11.2416347,18 L11.2580911,6.11380679 L13.0436094,18 L16.0633571,18 L17.7583653,5.8517865 L17.7707076,18 L22,18 L22,0 L15.6725178,0 Z"></path><path d="M24,18 L24,0 L31.8045586,0 C33.5693522,0 35,1.41994415 35,3.17660424 L35,14.8233958 C35,16.5777858 33.5716617,18 31.8045586,18 L24,18 Z M29.8322479,3.2395236 C29.6339219,3.13233348 29.2545158,3.08072342 28.7026524,3.08072342 L28.7026524,14.8914865 C29.4312846,14.8914865 29.8796736,14.7604764 30.0478195,14.4865461 C30.2159654,14.2165858 30.3021941,13.486105 30.3021941,12.2871637 L30.3021941,5.3078959 C30.3021941,4.49404499 30.272014,3.97397442 30.2159654,3.74371416 C30.1599168,3.5134539 30.0348852,3.34671372 29.8322479,3.2395236 Z"></path><path d="M44.4299079,4.50685823 L44.749518,4.50685823 C46.5447098,4.50685823 48,5.91267586 48,7.64486762 L48,14.8619906 C48,16.5950653 46.5451816,18 44.749518,18 L44.4299079,18 C43.3314617,18 42.3602746,17.4736618 41.7718697,16.6682739 L41.4838962,17.7687785 L37,17.7687785 L37,0 L41.7843263,0 L41.7843263,5.78053556 C42.4024982,5.01015739 43.3551514,4.50685823 44.4299079,4.50685823 Z M43.4055679,13.2842155 L43.4055679,9.01907814 C43.4055679,8.31433946 43.3603268,7.85185468 43.2660746,7.63896485 C43.1718224,7.42607505 42.7955881,7.2893916 42.5316822,7.2893916 C42.267776,7.2893916 41.8607934,7.40047379 41.7816216,7.58767002 L41.7816216,9.01907814 L41.7816216,13.4207851 L41.7816216,14.8074788 C41.8721037,15.0130276 42.2602358,15.1274059 42.5316822,15.1274059 C42.8031285,15.1274059 43.1982131,15.0166981 43.281155,14.8074788 C43.3640968,14.5982595 43.4055679,14.0880581 43.4055679,13.2842155 Z"></path></g></svg>
                                <span>8.6</span>
                            </div>
                        </div>
                    </li>
                    <li class="flex space-x-3 ">
                        <img src="https://upload.wikimedia.org/wikipedia/en/8/86/The_Silence_of_the_Lambs_poster.jpg" class="object-cover w-1/3 rounded-md" alt="">
                        <div class="flex flex-col justify-between  ">
                            <div class="flex flex-col space-y-1">
                                <span class="text-gray-700 dark:text-white font-semibold">The Silence of the Lambs</span>
                                <span class="text-xxs hidden xl:block">Crime, Drama, Thriller</span>
                            </div>
                            <div class="flex space-x-2 items-center">
                                <svg class="w-8 h-5" xmlns="http://www.w3.org/2000/svg" width="64" height="32" viewBox="0 0 64 32" version="1.1"><g fill="#F5C518"><rect x="0" y="0" width="100%" height="100%" rx="4"></rect></g><g transform="translate(8.000000, 7.000000)" fill="#000000" fill-rule="nonzero"><polygon points="0 18 5 18 5 0 0 0"></polygon><path d="M15.6725178,0 L14.5534833,8.40846934 L13.8582008,3.83502426 C13.65661,2.37009263 13.4632474,1.09175121 13.278113,0 L7,0 L7,18 L11.2416347,18 L11.2580911,6.11380679 L13.0436094,18 L16.0633571,18 L17.7583653,5.8517865 L17.7707076,18 L22,18 L22,0 L15.6725178,0 Z"></path><path d="M24,18 L24,0 L31.8045586,0 C33.5693522,0 35,1.41994415 35,3.17660424 L35,14.8233958 C35,16.5777858 33.5716617,18 31.8045586,18 L24,18 Z M29.8322479,3.2395236 C29.6339219,3.13233348 29.2545158,3.08072342 28.7026524,3.08072342 L28.7026524,14.8914865 C29.4312846,14.8914865 29.8796736,14.7604764 30.0478195,14.4865461 C30.2159654,14.2165858 30.3021941,13.486105 30.3021941,12.2871637 L30.3021941,5.3078959 C30.3021941,4.49404499 30.272014,3.97397442 30.2159654,3.74371416 C30.1599168,3.5134539 30.0348852,3.34671372 29.8322479,3.2395236 Z"></path><path d="M44.4299079,4.50685823 L44.749518,4.50685823 C46.5447098,4.50685823 48,5.91267586 48,7.64486762 L48,14.8619906 C48,16.5950653 46.5451816,18 44.749518,18 L44.4299079,18 C43.3314617,18 42.3602746,17.4736618 41.7718697,16.6682739 L41.4838962,17.7687785 L37,17.7687785 L37,0 L41.7843263,0 L41.7843263,5.78053556 C42.4024982,5.01015739 43.3551514,4.50685823 44.4299079,4.50685823 Z M43.4055679,13.2842155 L43.4055679,9.01907814 C43.4055679,8.31433946 43.3603268,7.85185468 43.2660746,7.63896485 C43.1718224,7.42607505 42.7955881,7.2893916 42.5316822,7.2893916 C42.267776,7.2893916 41.8607934,7.40047379 41.7816216,7.58767002 L41.7816216,9.01907814 L41.7816216,13.4207851 L41.7816216,14.8074788 C41.8721037,15.0130276 42.2602358,15.1274059 42.5316822,15.1274059 C42.8031285,15.1274059 43.1982131,15.0166981 43.281155,14.8074788 C43.3640968,14.5982595 43.4055679,14.0880581 43.4055679,13.2842155 Z"></path></g></svg>
                                <span>8.6</span>
                            </div>
                        </div>
                    </li>
                    <li class="pt-1">
                        <a href="#" class="px-5 py-2.5 bg-red-600 hover:bg-red-700 rounded-lg text-center font-medium block text-white">See More</a>
                    </li>

                </ul>
            </div>
            
        </aside><!-- /Right Sidebar -->


    </div>
  </template>
  