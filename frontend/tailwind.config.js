/** @type {import('tailwindcss').Config} */

module.exports = {
  content: [
    "./templates/**/*.html",  // Adjust the path to your Django templates
    "./src/**/*.{js,jsx,ts,tsx}",  // Path to your JavaScript or TypeScript files
    // Add other paths that include Tailwind classes
  ],
  theme: {
    extend: {
      colors: {
        'text-color': '#32456F',
      },
    },
  },
  plugins: [],
}
