import torch
import clip
from PIL import Image

# Load CLIP model
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

# Load images and text queries
images = [Image.open("cat.jpg"), Image.open("dog.jpg")]
image_inputs = torch.stack([preprocess(img) for img in images]).to(device)
text_inputs = clip.tokenize(["a photo of a cat", "a photo of a dog"]).to(device)

# Get features
with torch.no_grad():
    image_features = model.encode_image(image_inputs)
    text_features = model.encode_text(text_inputs)

# Compute similarity
similarity = (image_features @ text_features.T).softmax(dim=-1)
best_match = similarity.argmax(dim=1)
for i, img in enumerate(["cat.jpg", "dog.jpg"]):
    print(f"Best text match for {img}: {['cat', 'dog'][best_match[i]]}")
