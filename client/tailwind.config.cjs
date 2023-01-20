/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      animation: {
        "tracking-in-expand-fwd": "tracking-in-expand-fwd 0.8s cubic-bezier(0.215, 0.610, 0.355, 1.000)   both"
      },
      keyframes: {
        "tracking-in-expand-fwd": {
          "0%": {
            "letter-spacing": "-.5em",
            transform: "translateZ(-700px)",
            opacity: "0"
          },
          "40%": {
            opacity: ".6"
          },
          to: {
            transform: "translateZ(0)",
            opacity: "1"
          }
        }
      }
    },
  },
  daisyui: {
    themes: [
      {
        mytheme: {
          "primary": "#570DF8",
          "secondary": "#F000B8",
          "accent": "#37CDBE",
          "neutral": "#3D4451",
          "base-100": "#FFFFFF",
          "info": "#3ABFF8",
          "success": "#36D399",
          "warning": "#FBBD23",
          "error": "#F87272",
        },
      },
    ],
  },
  plugins: [require("daisyui")],
}
