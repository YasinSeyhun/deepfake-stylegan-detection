from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.model.detector import load_trained_detector, LABELS
from app.utils.image_utils import read_imagefile
from torchvision import transforms
import torch

app = FastAPI()

# CORS ayarları (frontend adresini ekle!)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend adresini ekle!
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

device = torch.device("cpu")
model = load_trained_detector("app/model/model_weights.pth", device=device)
preprocess = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.5, 0.5, 0.5], [0.5, 0.5, 0.5])
])

@app.post("/analyze")
async def analyze_image(file: UploadFile = File(...)):
    if not file.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="Yalnızca görsel dosyası yükleyebilirsiniz.")
    image = read_imagefile(file)
    input_tensor = preprocess(image).unsqueeze(0).to(device)
    with torch.no_grad():
        outputs = model(input_tensor)
        probs = torch.softmax(outputs, dim=1).cpu().numpy()[0]
        pred_idx = int(outputs.argmax(dim=1).cpu().numpy()[0])
        label = LABELS[pred_idx]
        confidence = float(probs[pred_idx])
    return {
        "result": label,
        "score": round(confidence * 100, 2)
    } 