import io
import torch
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from PIL import Image
from torchvision import transforms
from src.models import load_trained_detector, LABELS

# Model ve preprocess ayarları
MODEL_PATH = 'src/models/detector_best.pth'
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = load_trained_detector(MODEL_PATH, device=DEVICE)
preprocess = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
])

app = FastAPI()

# CORS ayarı (gerekirse frontend için aç)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    image_bytes = await file.read()
    image = Image.open(io.BytesIO(image_bytes)).convert('RGB')
    input_tensor = preprocess(image).unsqueeze(0).to(DEVICE)
    with torch.no_grad():
        outputs = model(input_tensor)
        probs = torch.softmax(outputs, dim=1).cpu().numpy()[0]
        pred_idx = int(outputs.argmax(dim=1).cpu().numpy()[0])
        label = LABELS[pred_idx]
        confidence = float(probs[pred_idx])
    return {"label": label, "confidence": confidence} 