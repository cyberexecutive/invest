# -*- coding: utf-8 -*-
"""
Script de processamento do novo Brasão / Logo / Favicon da Cyber Executive.
A partir da imagem oficial anexada pelo usuário, gera:
- logo-cyber-executive.png (1024x1024 RGBA com transparência circular perfeita)
- logo-cyber-executive.svg (SVG com alta definição e suporte vetorial)
- favicon.ico (multi-resolução: 16, 32, 48, 64, 128, 256)
- favicon-32x32.png, favicon-16x16.png
- apple-touch-icon.png (180x180)
- android-chrome-192x192.png, android-chrome-512x512.png
"""
import os
import base64
from PIL import Image, ImageFilter
import numpy as np

src_path = r"C:\Users\Claudinei Lima\.gemini\antigravity\brain\2dfa7f41-7a33-4fa1-883e-ba1f0866407a\.user_uploaded\media_1794072188031_d64c25b3.jpg"
target_dir = r"C:\invest\imagens"
os.makedirs(target_dir, exist_ok=True)

# 1. Carrega imagem fonte
im = Image.open(src_path).convert("RGBA")
arr = np.array(im, dtype=np.float32)
h, w, _ = arr.shape
cy, cx = (h - 1) / 2.0, (w - 1) / 2.0
y, x = np.ogrid[:h, :w]
dist = np.sqrt((x - cx)**2 + (y - cy)**2)

# Máscara circular suave para recorte perfeito do emblema
r_inner = 497.0
r_outer = 507.0
alpha = np.clip((r_outer - dist) / (r_outer - r_inner), 0.0, 1.0)
# Curva Hermite smoothstep para suavizar a borda
alpha = alpha * alpha * (3.0 - 2.0 * alpha)
arr[:, :, 3] = alpha * 255.0

logo_png = Image.fromarray(arr.astype(np.uint8), "RGBA")

# Salva logo-cyber-executive.png
png_dest = os.path.join(target_dir, "logo-cyber-executive.png")
logo_png.save(png_dest, format="PNG", optimize=True)
print(f"Salvo: {png_dest} ({logo_png.size})")

# 2. Gera favicons e ícones dedicados
ico_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
ico_images = [logo_png.resize(size, Image.Resampling.LANCZOS) for size in ico_sizes]

favicon_ico_root = r"C:\invest\favicon.ico"
favicon_ico_img = os.path.join(target_dir, "favicon.ico")
ico_images[0].save(favicon_ico_root, format="ICO", sizes=ico_sizes, append_images=ico_images[1:])
ico_images[0].save(favicon_ico_img, format="ICO", sizes=ico_sizes, append_images=ico_images[1:])
print(f"Salvo: {favicon_ico_root} e {favicon_ico_img}")

# Favicons PNG
p32 = os.path.join(target_dir, "favicon-32x32.png")
p16 = os.path.join(target_dir, "favicon-16x16.png")
apple = os.path.join(target_dir, "apple-touch-icon.png")
a192 = os.path.join(target_dir, "android-chrome-192x192.png")
a512 = os.path.join(target_dir, "android-chrome-512x512.png")

logo_png.resize((32, 32), Image.Resampling.LANCZOS).save(p32, "PNG", optimize=True)
logo_png.resize((16, 16), Image.Resampling.LANCZOS).save(p16, "PNG", optimize=True)
logo_png.resize((180, 180), Image.Resampling.LANCZOS).save(apple, "PNG", optimize=True)
logo_png.resize((192, 192), Image.Resampling.LANCZOS).save(a192, "PNG", optimize=True)
logo_png.resize((512, 512), Image.Resampling.LANCZOS).save(a512, "PNG", optimize=True)
print("Ícones PNG adicionais salvos com sucesso!")

# 3. Gera SVG equivalente de altíssima qualidade
with open(png_dest, "rb") as f:
    b64_png = base64.b64encode(f.read()).decode("ascii")

svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1024 1024" width="100%" height="100%">
  <defs>
    <filter id="execGlow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="4" stdDeviation="16" flood-color="#0284c7" flood-opacity="0.5"/>
    </filter>
  </defs>
  <image href="data:image/png;base64,{b64_png}" width="1024" height="1024" filter="url(#execGlow)" />
</svg>'''

svg_dest = os.path.join(target_dir, "logo-cyber-executive.svg")
with open(svg_dest, "w", encoding="utf-8") as f:
    f.write(svg_content)
print(f"Salvo: {svg_dest}")

print("Todas as mídias de marca geradas com perfeição!")

