

import { storeToRefs } from 'pinia'; 
import { useAuthStore } from '~/store/auth'; //

export default defineNuxtRouteMiddleware((to) => {
  const { authenticated } = storeToRefs(useAuthStore());
  const token = useCookie('token');
  const refreshToken = useCookie('refreshToken'); 


  // if token exists and url is /login redirect to homepage
  if (token.value && to?.name === 'login') {
    return navigateTo('/');
  }

  // if token and refresh_token doesn't exist redirect to log in 
  if (!token.value && to?.name !== 'login') {
    abortNavigation();

    if (refreshToken.value){
        refreshAccessToken(refreshToken.value)
        .then((newToken: any) => {
          // Update the token and its expiration time in the cookies
          token.value = newToken.access;
          const newExpirationTime = new Date().getTime() + 15 * 60 * 1000; // 15 minutes
          const new_token = useCookie('token', { expires: new Date(newExpirationTime) });
          new_token.value = newToken.access
          authenticated.value = true;
        }).catch(async () => {
          useAuthStore().logUserOut();
          return await navigateTo('/login');
        })
      
      } else {
        console.log('3')
        // No refresh token available, log the user out
        useAuthStore().logUserOut();
        return navigateTo('/login');
    
      }
    }
});


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

// TODO: add ui