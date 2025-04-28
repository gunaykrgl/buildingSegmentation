import numpy as np
import utils
from keras.models import load_model
import matplotlib.pyplot as plt
import gradio as gr

model = load_model("building_segmentation_model.keras")

def segment(img):
    mask = utils.predict(model, img)
    mask = mask[..., 0]
    
    # Set masked regions to blue with 70% transparency
    blue_color = np.array([255, 0, 0], dtype=np.uint8)  # Red color
    transparency = 0.7
    
    masked_image = img.copy()
    masked_image[mask == 1] = masked_image[mask == 1] * (1 - transparency) +  transparency * blue_color
    
    return masked_image

demo = gr.Interface(
    fn = segment,
    inputs=[gr.Image()],
    outputs=[gr.Image()],
    examples=[
        "images/22678945_15.png",
        "images/22828930_15.png",
        "images/23429080_15.png",
        "images/23729035_15.png",
        "images/24179065_15.png",
    ]
)

if __name__ == "__main__":
    demo.launch() 
