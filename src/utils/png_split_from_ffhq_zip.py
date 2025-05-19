import os
import random
import shutil
from glob import glob
from tqdm import tqdm

# Klasör yolları
FFHQ_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'raw', 'ffhq-512x512-unzipped')
PROCESSED_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'processed', 'real')
SPLITS = {'train': 1000, 'val': 100, 'test': 100}

# Tüm alt klasörlerdeki .png dosyalarını topla
all_pngs = glob(os.path.join(FFHQ_DIR, '*', '*.png'))
print(f"Toplam {len(all_pngs)} .png dosyası bulundu.")

# Karıştır ve splitlere ayır
random.shuffle(all_pngs)
train_pngs = all_pngs[:SPLITS['train']]
val_pngs = all_pngs[SPLITS['train']:SPLITS['train']+SPLITS['val']]
test_pngs = all_pngs[SPLITS['train']+SPLITS['val']:SPLITS['train']+SPLITS['val']+SPLITS['test']]
split_map = {'train': train_pngs, 'val': val_pngs, 'test': test_pngs}

for split, files in split_map.items():
    dst_dir = os.path.join(PROCESSED_DIR, split)
    os.makedirs(dst_dir, exist_ok=True)
    for i, src_path in enumerate(tqdm(files, desc=f"{split} split için .png kopyalanıyor")):
        ext = os.path.splitext(src_path)[1]
        dst_path = os.path.join(dst_dir, f"real_{i:05d}{ext}")
        shutil.copy2(src_path, dst_path)
    print(f"{split} split için {len(files)} .png dosyası kopyalandı.") 