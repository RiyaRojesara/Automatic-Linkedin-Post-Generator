import os
import uuid

BASE_DIR = "uploads"
IMG_DIR = f"{BASE_DIR}/images"
PDF_DIR = f"{BASE_DIR}/pdfs"

os.makedirs(IMG_DIR, exist_ok=True)
os.makedirs(PDF_DIR, exist_ok=True)

def save_images(images):
    paths = []
    for img in images:
        name = f"{uuid.uuid4()}_{img.name}"
        path = f"{IMG_DIR}/{name}"
        with open(path, "wb") as f:
            f.write(img.getbuffer())
        paths.append(path)
    return paths

def save_pdf(pdf):
    name = f"{uuid.uuid4()}_{pdf.name}"
    path = f"{PDF_DIR}/{name}"
    with open(path, "wb") as f:
        f.write(pdf.getbuffer())
    return path
