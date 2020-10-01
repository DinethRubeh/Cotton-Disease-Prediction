from flask import Flask, request
from werkzeug.utils import secure_filename
import os
import flasgger
from flasgger import Swagger

from predict import predict

# image upload path
UPLOAD_FOLDER = '/uploads'

# create directory if path does not exist
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Define a flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
Swagger(app)

# save request image file
def save_image(im):
    """
    So what does that secure_filename() function actually do? 
    Now the problem is that there is that principle called “never trust user input”. This is also true for the filename of an uploaded file. 
    All submitted form data can be forged, and filenames can be dangerous. For the moment just remember: 
    always use that function to secure a filename before storing it directly on the filesystem.

    Source - https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/
    """
    # upload path
    img_name = secure_filename(im.filename)
    img_path = os.path.join(app.config['UPLOAD_FOLDER'], img_name)
    # save image
    im.save(img_path)

    return img_path


@app.route('/')
def home():
    return "Hello random person"

@app.route('/predict', methods=['POST'])
def predict_uploaded_image():

    """Predict Cotton Disease from image file
    This is using docstrings for specifications.
    ---
    parameters:
      - name: file
        in: formData
        type: file
        required: true
      
    responses:
        200:
            description: Success
        
    """

    # get image
    uploaded_img = request.files['file']

    # save image
    saved_image_path = save_image(uploaded_img)

    # predict class from saved path
    pred = predict(saved_image_path)

    return pred

if __name__=='__main__':
    app.run(debug=True)