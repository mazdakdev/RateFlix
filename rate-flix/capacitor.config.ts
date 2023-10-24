import { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'com.rateflix',
  appName: 'RateFlix',
  webDir: 'dist',
  server: {
    androidScheme: 'https'
  }
};

export default config;
