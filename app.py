from flask import Flask, request, render_template
from PIL import Image
import io
import base64
from collections import Counter
import numpy as np

app = Flask(__name__)

def get_top_colors(image_data):
    img = Image.open(io.BytesIO(image_data))
    img = img.convert('RGB')
    pixels = np.array(img.getdata())
    color_counts = Counter(map(tuple, pixels))
    top_colors = color_counts.most_common(10)
    hex_colors = []
    for color, count in top_colors:
        hex_color = '#{:02x}{:02x}{:02x}'.format(*color)
        hex_colors.append(hex_color)
    return hex_colors

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image_file = request.files['file']
        if image_file:
            try:
                image_data = image_file.read()
                img = Image.open(io.BytesIO(image_data))

                img_buffer = io.BytesIO()
                img.save(img_buffer, format='PNG')
                img_base64 = base64.b64encode(img_buffer.getvalue()).decode('utf-8')

                colors = get_top_colors(image_data)

                return render_template('results.html', image_data=img_base64, colors=colors)
            except Exception as e:
                return f"Error: {e}"
        else:
            return "No image uploaded."
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)