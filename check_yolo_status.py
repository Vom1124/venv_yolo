#!/usr/bin/env python3
import ultralytics
from ultralytics import YOLO
import numpy as np
import os

# Disable update checks and telemetry
# ultralytics.SETTINGS["check_updates"] = False
# ultralytics.SETTINGS["sync"] = False

print("✅ Ultralytics imported successfully")
print(f"🔢 NumPy version: {np.__version__}")

try:
    model = YOLO("yolov8n.pt")
    print("🧠 YOLO model loaded successfully!")
except Exception as e:
    print(f"⚠️ Could not load model: {e}")

print("🚀 YOLO environment ready!")

# --- Force immediate exit ---
os._exit(0)
