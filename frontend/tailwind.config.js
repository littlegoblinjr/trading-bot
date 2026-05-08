/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'binance-bg': '#0b0e11',
        'binance-card': '#1e2329',
        'binance-green': '#00ff88',
        'binance-red': '#ff4d4d',
        'binance-gray': '#848e9c',
      },
    },
  },
  plugins: [],
}
