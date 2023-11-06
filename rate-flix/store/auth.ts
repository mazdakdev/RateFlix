// store/auth.ts

import { defineStore } from 'pinia';

interface UserPayloadInterface {
  email: string;
  password: string;
}

export const useAuthStore = defineStore('auth', {
  state: () => ({
    authenticated: false,
    loading: false,
    access_expire: new Date().getTime() + 30 * 60 * 1000, // 30 minutes
    refresh_expire: new Date().getTime() + 3 * 3600 * 1000 // 3 hours
  }),
  actions: {
    async authenticateUser({ email, password }: UserPayloadInterface) {
      // useFetch from nuxt 3
      const { data, pending }: any = await useFetch('http://localhost:8000/api/auth/login/', {
        method: 'post',
        headers: { 'Content-Type': 'application/json' },
        body: {
          email,
          password,
        },
      });
      this.loading = pending;

      if (data.value) {
        // Set the token expiration time
        const expirationTime = this.access_expire;
        const token = useCookie('token', { expires: new Date(expirationTime) });

        const refreshTokenExpirationTime =  this.refresh_expire;
        const refreshToken = useCookie('refreshToken', { expires: new Date(refreshTokenExpirationTime) });

        const user = useCookie('user');

        user.value = data?.value?.user;
        token.value = data?.value?.access;
        refreshToken.value = data?.value?.refresh;

        this.authenticated = true;
  
   
      }
    },
    logUserOut() {
      const token = useCookie('token'); // useCookie new hook in nuxt 3
      const user = useCookie('user');
      const refreshToken = useCookie('refreshToken');
      this.authenticated = false; // set authenticated  state value to false
      token.value = null; // clear the token cookie
      user.value = null
      refreshToken.value = null;
    },
  },
});