import os
import numpy as np
from PIL import Image
import tempfile
import trimesh
import re

# Placeholder for actual 3D model generation
# In a real implementation, this would use point-e or another model
def process_3d_model(image_input=None, text_input=None):
    """
    Process input (image or text) and generate a 3D model
    
    Args:
        image_input (numpy.ndarray, optional): Input image
        text_input (str, optional): Input text prompt
        
    Returns:
        tuple: (file_path, preview_data) for the generated 3D model
    """
    try:
        # Create output directory if it doesn't exist
        os.makedirs('samples/output_models', exist_ok=True)
        
        # Generate a filename for the output
        if text_input:
            # Create a safe filename from the text input
            base_name = re.sub(r'[^\w\s-]', '', text_input.lower())
            base_name = re.sub(r'[\s-]+', '_', base_name)
            filename = f"{base_name[:30]}.obj"
        else:
            filename = "model.obj"
            
        output_path = os.path.join('samples/output_models', filename)
        
        if image_input is not None:
            # Check if the input is already a numpy array
            if not isinstance(image_input, np.ndarray):
                image_input = np.array(image_input)
                
            print(f"Processing image input of shape {image_input.shape}")
            
            # Extract color information to determine shape
            # This is a very simplistic approach for the prototype
            # In a real implementation, this would be a more sophisticated image analysis
            avg_color = np.mean(image_input, axis=(0, 1))
            
            # Use color information to choose a shape
            if avg_color[0] > 150:  # More red
                mesh = create_simple_mesh("cylinder")
            elif avg_color[1] > 150:  # More green
                mesh = create_simple_mesh("sphere")
            else:  # Default
                mesh = create_simple_mesh("cube")
            
        elif text_input is not None:
            print(f"Processing text input: {text_input}")
            # Simple keyword matching for shape selection
            text = text_input.lower()
            
            if any(word in text for word in ["round", "sphere", "ball", "circular"]):
                mesh = create_simple_mesh("sphere")
            elif any(word in text for word in ["cylinder", "tube", "pipe", "column"]):
                mesh = create_simple_mesh("cylinder")
            elif any(word in text for word in ["cone", "pyramid", "triangular"]):
                mesh = create_simple_mesh("cone")
            else:
                mesh = create_simple_mesh("cube")
            
        else:
            raise ValueError("Either image or text input must be provided")
        
        # Export the mesh
        mesh.export(output_path)
        
        # Return the file path and a message
        return output_path, f"Generated 3D model: {os.path.basename(output_path)}"
        
    except Exception as e:
        print(f"Error in processing: {str(e)}")
        raise e

def create_simple_mesh(primitive_type="cube"):
    """
    Create a simple mesh for prototype purposes
    
    Args:
        primitive_type (str): Type of primitive to create
        
    Returns:
        trimesh.Trimesh: The generated mesh
    """
    if primitive_type == "cube":
        return trimesh.creation.box()
    elif primitive_type == "sphere":
        return trimesh.creation.icosphere(subdivisions=2, radius=1.0)
    elif primitive_type == "cylinder":
        return trimesh.creation.cylinder(radius=1.0, height=2.0)
    elif primitive_type == "cone":
        return trimesh.creation.cone(radius=1.0, height=2.0)
    else:
        return trimesh.creation.box()

# Image preprocessing function
def preprocess_image(image):
    """
    Preprocess an image for 3D model generation
    
    Args:
        image (numpy.ndarray or PIL.Image): Input image
        
    Returns:
        numpy.ndarray: Processed image
    """
    # Convert to PIL Image if needed
    if isinstance(image, np.ndarray):
        image = Image.fromarray(
            image.astype(np.uint8) if image.dtype != np.uint8 else image
        )
    
    # Resize to fixed size
    image = image.resize((224, 224))
    
    # Convert to RGB if needed
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    # Convert to numpy array
    image_np = np.array(image)
    
    return image_np 