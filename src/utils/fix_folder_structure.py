import os
import shutil

splits = ['train', 'val', 'test']
base_dir = 'data/processed'

for split in splits:
    for cls in ['real', 'fake']:
        src = os.path.join(base_dir, cls, split, cls)
        dst = os.path.join(base_dir, split, cls)
        os.makedirs(dst, exist_ok=True)
        if os.path.exists(src):
            for fname in os.listdir(src):
                shutil.move(os.path.join(src, fname), os.path.join(dst, fname))

# Eski ana klasörleri sil
for cls in ['real', 'fake']:
    dir_to_remove = os.path.join(base_dir, cls)
    if os.path.exists(dir_to_remove):
        shutil.rmtree(dir_to_remove)

print('Klasör yapısı başarıyla düzeltildi ve eski klasörler silindi.') 