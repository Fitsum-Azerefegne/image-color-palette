 🎨 Image Color Palette Extractor 

A Flask web application that analyzes uploaded images and extracts their top 10 dominant colors in HEX format.

 🌟 Features
- Upload any image (JPG, PNG, etc.)
- Displays the uploaded image
- Extracts and shows the top 10 dominant colors
- Presents colors with their HEX codes
- Responsive design works on all devices

 🛠️ Technologies Used
- **Python** (Flask backend)
- **Pillow (PIL)** for image processing
- **NumPy** for color analysis
- **HTML/CSS** for the frontend
- **Base64** for image encoding

 ⚙️ Setup Instructions

 Prerequisites
- Python 3.8+
- Pip package manager

 Installation
1. Clone the repository:
```bash
git clone https://github.com/yourusername/image-color-palette.git
cd image-color-palette
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install flask pillow numpy
```

 Running the Application
```bash
python app.py
```
Then open `http://localhost:5000` in your browser.

 📂 Project Structure
```
image-color-palette/
├── app.py                # Main Flask application
├── static/
│   └── styles.css        # CSS styles
├── templates/
│   ├── index.html        # Upload page
│   └── results.html      # Results page
└── README.md
```

 🖼️ How It Works
1. User uploads an image
2. The backend:
   - Converts the image to RGB format
   - Analyzes pixel colors
   - Counts color occurrences
   - Extracts the top 10 most common colors
3. Results are displayed with:
   - The uploaded image
   - Color swatches with HEX codes

 🎨 Example Output
After uploading an image, you'll see:
- The original image displayed
- A list of 10 color boxes with their HEX codes
- Colors ordered by dominance in the image

 🌈 Potential Uses
- Graphic design color schemes
- Website theming
- Art analysis
- Brand color extraction

Tip: For best results, use images with clear color patterns rather than complex photos with many subtle shades.
