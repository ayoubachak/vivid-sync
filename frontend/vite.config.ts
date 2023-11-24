import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'

// https://vitejs.dev/config/
export default defineConfig(({ mode }) => ({
  base: mode === 'production' ? '/static/frontend/' : '/',
  plugins: [react()],
  build:{
    outDir:'./static/frontend',
    rollupOptions: {
      output: {
        // Overwrite the default entry chunk name:
        entryFileNames: 'assets/main.js', // Always outputs main.js
        // Overwrite default asset chunk name:
        chunkFileNames: 'assets/main-[name].js',
        // Overwrite default CSS name:
        assetFileNames: assetInfo => {
          if (assetInfo.name === 'style.css') return 'assets/main.css';
          return 'assets/[name].[ext]';
        },
      },
    },
    manifest: false,
    minify: mode === 'production',
  }
}));
