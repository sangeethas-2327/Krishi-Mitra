import os
from pathlib import Path
from PIL import Image

def generate_assets():
    src_path = Path(r"C:/Users/SANGEETHA S/.gemini/antigravity/brain/e620c2ad-4191-4cef-8383-fedaccc3eeb5/.user_uploaded/media_1793409006757_2cbf3fd1.jpg")
    output_dir = Path(r"C:/Users/SANGEETHA S/.gemini/antigravity/scratch/krishi-mitra/frontend/public")
    output_dir.mkdir(parents=True, exist_ok=True)

    img = Image.open(src_path).convert("RGB")
    bg_color = (251, 252, 238)  # Exact sampled border color #FBFCEE

    # 1. Save original full-proportions logo as PNG & JPG
    img.save(output_dir / "krishi-mitra-logo.png", format="PNG", optimize=True)
    img.save(output_dir / "krishi-mitra-logo.jpg", format="JPEG", quality=98)
    print("Saved original logo files (PNG & JPG).")

    # 2. Create square icon canvas with centered emblem for favicons and square icons
    # Emblem bbox in source: (94, 51, 902, 807), width 808, height 756
    # Center: cx = 498, cy = 429
    # To maintain balanced margin around the emblem on a square canvas:
    # Max dimension is 808. Let's make a square canvas of 920x920 centered at (498, 429).
    square_size = 920
    cx, cy = 498, 429
    half = square_size // 2

    square_canvas = Image.new("RGB", (square_size, square_size), bg_color)
    paste_x = half - cx
    paste_y = half - cy
    square_canvas.paste(img, (paste_x, paste_y))

    # Save master square icon
    square_canvas.save(output_dir / "krishi-mitra-icon.png", format="PNG", optimize=True)
    print("Saved master square icon.")

    # 3. Generate high-quality rescaled icons using Lanczos resampling
    sizes = {
        "favicon-16x16.png": 16,
        "favicon-32x32.png": 32,
        "favicon-48x48.png": 48,
        "apple-touch-icon.png": 180,
        "icon-192.png": 192,
        "icon-512.png": 512,
    }

    for filename, sz in sizes.items():
        resized = square_canvas.resize((sz, sz), Image.Resampling.LANCZOS)
        resized.save(output_dir / filename, format="PNG", optimize=True)
        print(f"Generated {filename} ({sz}x{sz})")

    # 4. Generate multi-resolution favicon.ico containing 16x16, 32x32, 48x48
    ico_img = square_canvas.resize((48, 48), Image.Resampling.LANCZOS)
    ico_img.save(
        output_dir / "favicon.ico",
        format="ICO",
        sizes=[(16, 16), (32, 32), (48, 48)]
    )
    print("Generated favicon.ico (multi-size: 16, 32, 48)")

    # 5. Generate manifest.json
    manifest_content = '''{
  "short_name": "Krishi Mitra",
  "name": "Krishi Mitra (ಕೃಷಿ ಮಿತ್ರ) — The Living Farm Companion",
  "description": "Vernacular AI Companion & Government Schemes Guide for Karnataka Farmers",
  "icons": [
    {
      "src": "/favicon.ico",
      "sizes": "48x48 32x32 16x16",
      "type": "image/x-icon"
    },
    {
      "src": "/icon-192.png",
      "type": "image/png",
      "sizes": "192x192"
    },
    {
      "src": "/icon-512.png",
      "type": "image/png",
      "sizes": "512x512"
    },
    {
      "src": "/apple-touch-icon.png",
      "type": "image/png",
      "sizes": "180x180"
    }
  ],
  "start_url": "/",
  "background_color": "#FAF7F0",
  "theme_color": "#183B2B",
  "display": "standalone",
  "orientation": "portrait"
}
'''
    with open(output_dir / "manifest.json", "w", encoding="utf-8") as f:
        f.write(manifest_content)
    print("Generated manifest.json")

if __name__ == "__main__":
    generate_assets()

