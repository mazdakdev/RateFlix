

import { storeToRefs } from 'pinia'; 
import { useAuthStore } from '~/store/auth'; //

export default defineNuxtRouteMiddleware((to) => {
  const { authenticated, access_expire, refresh_expire } = storeToRefs(useAuthStore());
  const token = useCookie('token');
  const refreshToken = useCookie('refreshToken'); 

  if (token.value) {
    authenticated.value = true;
  }

  // if token exists and url is /login redirect to homepage
  if (token.value && to?.name === 'login') {
    console.log("ne")
    return navigateTo('/');
  }

  // if token doesn't exist redirect to log in
  if (!token.value && to?.name !== 'login') {
    abortNavigation();
    const currentTime = new Date().getTime();

    if (refreshToken.value){
        refreshAccessToken(refreshToken.value)
        .then((newToken: any) => {
          // Update the token and its expiration time in the cookies
          token.value = newToken.access;
          const newExpirationTime = new Date().getTime() + 15 * 1000; // 15 minutes
          const new_token = useCookie('token', { expires: new Date(newExpirationTime) });
          new_token.value = newToken.access
          authenticated.value = true;
        })
        .catch(() => {
          useAuthStore().logUserOut();
        
          return navigateTo('/login');
          
        });
      } else {
        // No refresh token available, log the user out
        console.log("else")
        useAuthStore().logUserOut();
        
        return navigateTo('/login');
    
      }
    }


 
});


  // ...

  // Function to refresh the access token using the refresh token
  async function refreshAccessToken(refreshToken: string) {
    const { data } = await useFetch('http://localhost:8000/api/auth/login/refresh/', {
      method: 'post',
      headers: { 'Content-Type': 'application/json' },
      body: {
        refresh: refreshToken,
      },
    });
    return data.value;
  }


// TODO: Clean the Code
// TODO: add ui
//TODO: fix linting problems
//TODO: add Authorization page