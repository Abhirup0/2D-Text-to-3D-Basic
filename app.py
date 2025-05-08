import gradio as gr
import numpy as np
from PIL import Image
import os
from processor import process_3d_model

def process_image(image):
    """Process image and generate 3D model"""
    try:
        if image is not None:
            output_path, message = process_3d_model(image_input=image)
            return output_path
    except Exception as e:
        return gr.Error(str(e))

def process_text(text):
    """Process text and generate 3D model"""
    try:
        if text:
            output_path, message = process_3d_model(text_input=text)
            return output_path
    except Exception as e:
        return gr.Error(str(e))

# Create Gradio interface
with gr.Blocks(css="static/style.css") as demo:
    gr.Markdown("# 3D Model Generator")
    gr.Markdown("Convert images or text descriptions into 3D models")
    
    with gr.Tab("Image to 3D"):
        with gr.Row():
            with gr.Column():
                image_input = gr.Image(label="Upload Image")
                image_button = gr.Button("Generate 3D Model", variant="primary")
            with gr.Column():
                image_output = gr.File(label="Download 3D Model")
                # Note: Preview may not work without additional setup
                preview = gr.Model3D(label="Preview", visible=False)
    
    with gr.Tab("Text to 3D"):
        with gr.Row():
            with gr.Column():
                text_input = gr.Textbox(
                    placeholder="Describe the object (e.g., 'A small toy car', 'A spherical ball')",
                    label="Text Description"
                )
                text_button = gr.Button("Generate 3D Model", variant="primary")
            with gr.Column():
                text_output = gr.File(label="Download 3D Model")
                # Note: Preview may not work without additional setup
                text_preview = gr.Model3D(label="Preview", visible=False)
    
    # Event handlers
    image_button.click(
        fn=process_image,
        inputs=[image_input],
        outputs=[image_output]
    )
    
    text_button.click(
        fn=process_text,
        inputs=[text_input],
        outputs=[text_output]
    )
    
    # Footer
    gr.Markdown("---")
    gr.Markdown("### About")
    gr.Markdown("""
    This application converts images or text descriptions into simple 3D models.
    Currently supports basic shapes (cube, sphere, cylinder, cone) based on input analysis.
    Download the generated .obj files and open them in any 3D model viewer.
    """)

if __name__ == "__main__":
    demo.launch() 