/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        // "The Living Farm Companion" Palette
        ivory: {
          DEFAULT: '#F5F1E8',
          light: '#FAF7F0',
          dark: '#EBE5D8',
          border: '#E2D9C8',
        },
        forest: {
          DEFAULT: '#183B2B',
          950: '#0E241A',
          900: '#133023',
          800: '#183B2B',
          700: '#23503B',
          600: '#2E664C',
          500: '#3D8262',
          muted: '#4A6B5B',
          surface: '#153325',
        },
        sage: {
          DEFAULT: '#A8B58A',
          light: '#DEE4D2',
          muted: '#C5CEB4',
          dark: '#738255',
        },
        harvest: {
          DEFAULT: '#D7A85B',
          light: '#F8ECCF',
          muted: '#E6C488',
          dark: '#B08233',
        },
        terracotta: {
          DEFAULT: '#C66F4E',
          light: '#F5DDD3',
          muted: '#DA8E72',
          dark: '#9E4E30',
        },
        charcoal: {
          DEFAULT: '#282C27',
          light: '#4B5249',
          muted: '#727B70',
          dark: '#1A1C19',
        },
        // Backward-compatible semantic references
        bglight: '#F5F1E8',
        ktext: {
          primary: '#282C27',
          muted: '#636B61',
        }
      },
      fontFamily: {
        sans: ['"DM Sans"', 'system-ui', '-apple-system', 'sans-serif'],
        kannada: ['"Noto Sans Kannada"', '"DM Sans"', 'system-ui', 'sans-serif'],
        mono: ['"JetBrains Mono"', 'monospace'],
      },
      boxShadow: {
        'editorial': '0 1px 2px rgba(24, 59, 43, 0.04), 0 4px 12px rgba(24, 59, 43, 0.03)',
        'editorial-hover': '0 2px 4px rgba(24, 59, 43, 0.06), 0 12px 24px rgba(24, 59, 43, 0.06)',
        'dossier': '0 4px 20px -2px rgba(24, 59, 43, 0.06), 0 1px 3px rgba(24, 59, 43, 0.04)',
        'studio-glow': '0 0 50px -10px rgba(215, 168, 91, 0.25)',
        'mic-glow': '0 0 40px rgba(198, 111, 78, 0.35)',
      },
      borderRadius: {
        'editorial': '1.25rem',
        'badge': '2rem',
      }
    },
  },
  plugins: [],
}
