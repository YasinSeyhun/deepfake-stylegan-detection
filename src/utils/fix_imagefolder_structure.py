import os
import shutil
from glob import glob

PROCESSED_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'data', 'processed')
SPLITS = ['train', 'val', 'test']
CLASSES = ['real', 'fake']

for cls in CLASSES:
    for split in SPLITS:
        split_dir = os.path.join(PROCESSED_DIR, cls, split)
        class_dir = os.path.join(split_dir, cls)
        os.makedirs(class_dir, exist_ok=True)
        # Sadece .png dosyalarını taşı
        for img_path in glob(os.path.join(split_dir, '*.png')):
            shutil.move(img_path, os.path.join(class_dir, os.path.basename(img_path)))
        print(f"{split_dir} içindeki görseller {class_dir} altına taşındı.") 