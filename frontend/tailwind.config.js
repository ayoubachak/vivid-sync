/** @type {import('tailwindcss').Config} */

module.exports = {
  content: [
    "./templates/**/*.html",  // Adjust the path to your Django templates
    "./src/**/*.{js,jsx,ts,tsx}",  // Path to your JavaScript or TypeScript files
    // Add other paths that include Tailwind classes
  ],
  darkMode: 'class',  
  theme: {
    extend: {
      colors: {
        'text-color': '#32456F',
        'light-orange': '#FFF2EF',
        'intense-orange': '#E36B4B',
        'color-primary': '#32456F', // this is dark blue
        'color-secondary': '#E36B4B', // this is dark orange
        'color-tertiary': '#FFF2EF', // this is light orange
      },
    },
  },
  plugins: [],
}
