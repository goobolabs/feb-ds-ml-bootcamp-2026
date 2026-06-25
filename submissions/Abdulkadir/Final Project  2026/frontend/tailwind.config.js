/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{js,jsx}"],
  theme: {
    extend: {
      fontFamily: {
        sans: ['"Inter"', "system-ui", "sans-serif"],
        display: ['"Plus Jakarta Sans"', '"Inter"', "system-ui", "sans-serif"]
      },
      colors: {
        brand: {
          50: "#eef6ff",
          100: "#d9ebff",
          200: "#bcdcff",
          300: "#8cc3ff",
          400: "#56a0ff",
          500: "#2c7df5",
          600: "#1f65d8",
          700: "#1d52af",
          800: "#1d488f",
          900: "#1e3f76"
        },
        accent: {
          50: "#ecfdf6",
          100: "#d1fae8",
          200: "#a8f4d4",
          300: "#72e8bc",
          400: "#37d39d",
          500: "#16b982",
          600: "#0f986c",
          700: "#10795a",
          800: "#105f49",
          900: "#0f4f3e"
        }
      },
      boxShadow: {
        soft: "0 14px 34px rgba(15, 23, 42, 0.08)",
        glow: "0 8px 24px rgba(44, 125, 245, 0.24)"
      }
    }
  },
  plugins: []
};

