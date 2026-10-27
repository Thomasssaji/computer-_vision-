from ultralytics import YOLO
import torch

print("========== DEVICE CHECK ==========")
print("PyTorch version:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())

if torch.cuda.is_available():
    print("GPU:", torch.cuda.get_device_name(0))
    device = 0
else:
    print("Using CPU for training.")
    device = "cpu"

print("\n========== LOADING MODEL ==========")
model = YOLO("yolo11n.pt")

print("\n========== STARTING TRAINING ==========")

results = model.train(
    data="yolo_dataset/data.yaml",
    epochs=50,
    imgsz=416,
    batch=8,
    device=device,
    workers=2,
    project="runs/traffic_sign",
    name="training",
    patience=10,
    save=True,
    plots=True
)

print("\n========== TRAINING COMPLETED ==========")
print("Best model: runs/traffic_sign/training/weights/best.pt")
print("Last model: runs/traffic_sign/training/weights/last.pt")