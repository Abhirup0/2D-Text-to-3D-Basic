import os
import numpy as np
from PIL import Image
import re

def validate_image(image_path):
    """
    Validate if a file is a usable image
    
    Args:
        image_path (str): Path to the image file
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not os.path.exists(image_path):
        return False
    
    try:
        with Image.open(image_path) as img:
            # Check if image mode is supported
            if img.mode not in ['RGB', 'RGBA']:
                return False
            
            # Check if image dimensions are reasonable
            if img.width < 10 or img.height < 10:
                return False
            
            # Try to load it into a numpy array
            _ = np.array(img)
            
            return True
    except Exception:
        return False

def validate_text_prompt(text):
    """
    Validate if a text prompt is suitable for 3D generation
    
    Args:
        text (str): Text prompt
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not text or not isinstance(text, str):
        return False
    
    # Remove extra whitespace
    text = text.strip()
    
    # Check if too short
    if len(text) < 3:
        return False
    
    # Check if too long
    if len(text) > 1000:
        return False
    
    return True

def sanitize_filename(filename):
    """
    Sanitize a filename to be safe for filesystem operations
    
    Args:
        filename (str): Input filename
        
    Returns:
        str: Sanitized filename
    """
    # Remove illegal characters
    filename = re.sub(r'[\\/*?:"<>|]', "_", filename)
    
    # Limit length
    if len(filename) > 255:
        base, ext = os.path.splitext(filename)
        filename = base[:255-len(ext)] + ext
    
    return filename

def format_prompt(text):
    """
    Format a text prompt for better 3D generation results
    
    Args:
        text (str): Input text prompt
        
    Returns:
        str: Formatted prompt
    """
    text = text.strip()
    
    # Ensure it ends with a period
    if not text.endswith(('.', '!', '?')):
        text += '.'
    
    # Ensure first letter is capitalized
    text = text[0].upper() + text[1:]
    
    return text 