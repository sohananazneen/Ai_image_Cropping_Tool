from flask import Flask, request, render_template, send_file
from PIL import Image
import io
import base64

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        image_file = request.files['image']
        image_path = 'static/uploads/' + image_file.filename
        image_file.save(image_path)
        return render_template('index.html', image_path=image_path)
    else:
        return render_template('index.html')

@app.route('/crop', methods=['POST'])
def crop():
    cropped_image_data = request.json['croppedImage']
    cropped_image = Image.open(io.BytesIO(base64.b64decode(cropped_image_data.split(',')[1])))
    img_io = io.BytesIO()
    cropped_image.save(img_io, 'JPEG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run(debug=True, port=5001)
