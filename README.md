# 3D Model Generator

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python 3.8+">
  <img src="https://img.shields.io/badge/Gradio-3.35+-orange.svg" alt="Gradio 3.35+">
  <img src="https://img.shields.io/badge/License-MIT-green.svg" alt="License: MIT">
</div>

<p align="center">
  <b>Convert images or text descriptions into 3D models with ease</b>
</p>

## 🌟 Features

- 💬 **Text-to-3D**: Generate 3D models from text descriptions
- 🖼️ **Image-to-3D**: Convert images into 3D models
- 🔄 **Multiple Export Formats**: Export as .obj or .stl files
- 🎨 **User-Friendly Interface**: Clean and intuitive Gradio UI
- 🚀 **Easy to Use**: No technical expertise required

## 📋 Overview

This application allows users to generate simple 3D models from either text descriptions or images. The system analyzes the input and creates appropriate 3D representations that can be downloaded and used in various 3D modeling software.

<p align="center">
  <i>Perfect for prototyping, creative projects, or educational purposes!</i>
</p>

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Abhirup0/2D-Text-to-3D-Basic.git
   cd 2D-Text-to-3D-Basic
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

1. Start the application:
   ```bash
   python app.py
   ```

2. Open your browser and navigate to:
   ```
   http://127.0.0.1:7860
   ```

3. Choose between the "Image to 3D" or "Text to 3D" tab:
   - For **Text to 3D**: Enter a description of the object you want to create
   - For **Image to 3D**: Upload an image to convert to a 3D model

4. Click the "Generate 3D Model" button and wait for processing

5. Download your 3D model in the desired format

## 🧠 How It Works

### Text-to-3D:
The system analyzes keywords in your text description to determine the most appropriate 3D shape. For example:
- "Round," "sphere," "ball," or "circular" will generate a sphere
- "Cylinder," "tube," "pipe," or "column" will generate a cylinder
- "Cone," "pyramid," or "triangular" will generate a cone
- Other descriptions will default to a cube

### Image-to-3D:
The system analyzes the color information in your image to determine the shape:
- Images with predominantly red colors generate cylinders
- Images with predominantly green colors generate spheres
- Other images default to cubes

## 📁 Project Structure

```
project/
├── app.py          # Main Gradio application
├── processor.py    # Core processing logic
├── utils.py        # Helper functions
├── requirements.txt
├── README.md
├── static/         # CSS and static files
└── samples/        # Sample inputs/outputs
```

## 🤝 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/Abhirup0">Abhirup</a>
</p> 