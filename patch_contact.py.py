#!/usr/bin/env python3
"""patch_contact.py — Update contact info, social links, and payment numbers"""

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

changes = 0

# ── 1. Update Facebook Links ──
old_fb = "https://www.facebook.com/elmer.tinaan#"
new_fb = "https://www.facebook.com/profile.php?id=61594233720257"
if old_fb in text:
    text = text.replace(old_fb, new_fb)
    changes += 1

# Also update the display text
old_fb_text = "facebook.com/elmer.tinaan"
new_fb_text = "facebook.com/profile.php?id=61594233720257"
text = text.replace(old_fb_text, new_fb_text)

# ── 2. Update Instagram Links ──
old_ig = "https://instagram.com/choxdz"
new_ig = "https://www.instagram.com/_letsredo?psln=NDNmZHpsc29uOHJ2"
if old_ig in text:
    text = text.replace(old_ig, new_ig)
    changes += 1

# Update IG display text
old_ig_text = "@choxdz"
new_ig_text = "@_letsredo"
text = text.replace(old_ig_text, new_ig_text)

# ── 3. Update Phone Number & GCash/Maya ──
old_phone = "0912 345 6789"
new_phone = "0926 757 3433"
if old_phone in text:
    text = text.replace(old_phone, new_phone)
    changes += 1

# Update tel: link format (no spaces)
old_tel = "tel:+639123456789"
new_tel = "tel:+639267573433"
text = text.replace(old_tel, new_tel)

# Also check kung may "09123456789" format (walang space)
text = text.replace("09123456789", "09267573433")

# ── 4. Save ──
ts = datetime.now().strftime("%Y%m%d_%H%M%S")
shutil.copy2(TARGET, f"{TARGET}.bak_{ts}")

with open(TARGET, "w", encoding="utf-8") as f:
    f.write(text)

print(f"✅ Updated Facebook link")
print(f"✅ Updated Instagram link")
print(f"✅ Updated Phone & GCash/Maya number")
print(f"✅ Backup saved.")
print(f"🚀 Next: git add . && git commit -m 'Update contact info' && git push")