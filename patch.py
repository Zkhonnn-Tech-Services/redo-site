#!/usr/bin/env python3
"""patch_update.py — Update ReDo site with dual images per product"""

import os
import re
import shutil
from datetime import datetime

TARGET = "index.html"

if not os.path.isfile(TARGET):
    print(f"❌ Not found: {TARGET}")
    exit(1)

with open(TARGET, "r", encoding="utf-8") as f:
    text = f.read()

# ── 1. Update Hero & About Text (Idagdag ang Egg Trays) ──
text = text.replace(
    "Sustainable products made from <strong>discarded garlic peels</strong> and <strong>recycled paper pulp</strong> — giving waste a second life.",
    "Sustainable products made from <strong>discarded garlic peels</strong>, <strong>egg trays</strong>, and <strong>recycled paper pulp</strong> — giving waste a second life."
)

# ── 2. Replace the entire Products Section ──
# We find the grid and replace it completely
products_regex = r'<div class="products-grid">.*?</section>'
new_products = '''<div class="products-grid">
                <!-- Product 1: Brown Organizer -->
                <div class="product-card">
                    <div class="product-image" style="display: flex; gap: 10px; background: transparent;">
                        <div style="flex: 1; background: #FAF6EE; border-radius: 8px; overflow: hidden; display: flex; align-items: center; justify-content: center;">
                            <img src="brown.png" alt="ReDo Basic Organizer Empty" style="width: 100%; height: 100%; object-fit: cover;">
                        </div>
                        <div style="flex: 1; background: #FAF6EE; border-radius: 8px; overflow: hidden; display: flex; align-items: center; justify-content: center;">
                            <img src="brown_pens.png" alt="ReDo Basic Organizer with Pens" style="width: 100%; height: 100%; object-fit: cover;">
                        </div>
                    </div>
                    <div class="product-info">
                        <h3 class="product-name">ReDo Basic Organizer</h3>
                        <p class="product-desc">
                            A minimalist cup-shaped organizer made from discarded garlic peels, egg trays, and recycled paper pulp. Perfect for pens, office supplies, and everyday items.
                        </p>
                        <div class="product-details">
                            <div class="detail-item">
                                <span class="detail-label">Material:</span>
                                <span class="detail-value">Garlic Peel & Paper</span>
                            </div>
                            <div class="detail-item">
                                <span class="detail-label">Design:</span>
                                <span class="detail-value">Raw / Minimalist</span>
                            </div>
                        </div>
                        <div class="product-footer">
                            <div class="product-price">₱20</div>
                            <a href="#order" class="btn btn-small">Order Now</a>
                        </div>
                    </div>
                </div>

                <!-- Product 2: Floral Organizer -->
                <div class="product-card">
                    <div class="product-image" style="display: flex; gap: 10px; background: transparent;">
                        <div style="flex: 1; background: #FAF6EE; border-radius: 8px; overflow: hidden; display: flex; align-items: center; justify-content: center;">
                            <img src="flower.png" alt="ReDo Floral Organizer Empty" style="width: 100%; height: 100%; object-fit: cover;">
                        </div>
                        <div style="flex: 1; background: #FAF6EE; border-radius: 8px; overflow: hidden; display: flex; align-items: center; justify-content: center;">
                            <img src="flower_brushes.png" alt="ReDo Floral Organizer with Brushes" style="width: 100%; height: 100%; object-fit: cover;">
                        </div>
                    </div>
                    <div class="product-info">
                        <h3 class="product-name">ReDo Floral Organizer</h3>
                        <p class="product-desc">
                            Upgrade your desk or vanity with our fuzzy wire design! Made from upcycled materials, it's perfect for makeup brushes, pens, and accessories.
                        </p>
                        <div class="product-details">
                            <div class="detail-item">
                                <span class="detail-label">Material:</span>
                                <span class="detail-value">Garlic Peel & Paper</span>
                            </div>
                            <div class="detail-item">
                                <span class="detail-label">Design:</span>
                                <span class="detail-value">Fuzzy Wire Flower</span>
                            </div>
                        </div>
                        <div class="product-footer">
                            <div class="product-price">₱35</div>
                            <a href="#order" class="btn btn-small">Order Now</a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>'''
        
text = re.sub(products_regex, new_products, text, flags=re.DOTALL)

# ── 3. Update Hero Stats Price ──
text = text.replace('<div class="stat-num">₱50</div>', '<div class="stat-num">₱20</div>')

# ── 4. Save ──
ts = datetime.now().strftime("%Y%m%d_%H%M%S")
shutil.copy2(TARGET, f"{TARGET}.bak_{ts}")

with open(TARGET, "w", encoding="utf-8") as f:
    f.write(text)

print(f"✅ Updated Products with dual images!")
print(f"✅ Prices: ₱20 (Basic) and ₱35 (Floral)")
print(f"✅ Backup saved.")
print(f"🚀 Next: git add . && git commit -m 'Update products' && git push")