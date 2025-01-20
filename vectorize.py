import os
import pandas as pd
import json

from PIL import Image
from sentence_transformers import SentenceTransformer

images_dir = "images"

max_images = 10000

model = SentenceTransformer("clip-ViT-B-32")

image_files = [os.path.join(images_dir, file) for file in os.listdir(images_dir)][:max_images]

images = []
image_labels = []
for image_file in image_files:
    images.append(Image.open(image_file))
    base, ext = os.path.splitext(os.path.basename(image_file))
    image_labels.append(base)

img_emb = model.encode(images)
columns = [f"{i}dim" for i in range(1, img_emb[0].size + 1)]

df = pd.DataFrame(img_emb, columns=columns, index=image_labels)
df.index.name = "name"
mapping = json.load(open("mapping.json", "r"))
df["unicode"] = [mapping.get(name) for name in image_labels]
df.to_parquet("./df.parquet", compression="zstd")
