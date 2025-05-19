import os
import torch
import random
from PIL import Image
import numpy as np
from tqdm import tqdm

# Klasör yolları
BACKUP_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'backup_real')
PROCESSED_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'processed', 'real')
SPLITS = {'train': 1000, 'val': 100, 'test': 100}

for split, num_samples in SPLITS.items():
    src_dir = os.path.join(BACKUP_DIR, split)
    dst_dir = os.path.join(PROCESSED_DIR, split)
    os.makedirs(dst_dir, exist_ok=True)
    pt_files = [f for f in os.listdir(src_dir) if f.endswith('.pt')]
    if len(pt_files) < num_samples:
        print(f"UYARI: {split} için sadece {len(pt_files)} dosya bulundu, {num_samples} isteniyor!")
        num_samples = len(pt_files)
    selected_files = random.sample(pt_files, num_samples)
    for i, fname in enumerate(tqdm(selected_files, desc=f"{split} split için .pt -> .png")):
        pt_path = os.path.join(src_dir, fname)
        tensor = torch.load(pt_path)
        # Eğer batch ise, ilk görseli al
        if tensor.ndim == 4:
            tensor = tensor[0]
        # (C, H, W) ise (H, W, C)'ye çevir
        if tensor.shape[0] == 3:
            img = tensor.permute(1, 2, 0).cpu().numpy()
        elif tensor.shape[-1] == 3:
            img = tensor.cpu().numpy()
        else:
            raise ValueError(f"Beklenmeyen tensör boyutu: {tensor.shape} ({fname})")
        # [0,1] veya [-1,1] aralığındaysa [0,255]'e çevir
        if img.max() <= 1.0:
            img = (img * 255).clip(0, 255)
        elif img.min() < 0:
            img = ((img + 1) / 2 * 255).clip(0, 255)
        img = img.astype(np.uint8)
        im = Image.fromarray(img)
        out_path = os.path.join(dst_dir, f"real_{i:05d}.png")
        im.save(out_path)
    print(f"{split} split için {num_samples} .pt dosyası .png'ye dönüştürüldü ve kaydedildi.") 