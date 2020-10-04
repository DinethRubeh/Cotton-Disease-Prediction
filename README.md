# Cotton-Disease-Prediction
Cotton disease prediction model training was done using,
 - pre-trained models such as **ResNet50, ResNet152V2, VGG19, InceptionV3** 
 - an **optimized CNN model**

All models except ResNet50 showed excellent accuracy but ultimately **VGG19** model was chosen because of it's ***less model size*** compared to others.

 - *CNN Model showed great accuracy but it had the largest model size. Used Data augmentation techniques and keras-tuner to find optimal set of model parameters to obtain the best CNN model*

All models were trained on Google Colab environment using GPUs.

Cotton disease dataset: https://www.youtube.com/redirect?q=https%3A%2F%2Fdrive.google.com%2Fdrive%2Ffolders%2F1vdr9CC9ChYVW2iXp6PlfyMOGD-4Um1ue&redir_token=QUFFLUhqbEo3QzRld1EwZmVxR0FlS2dlZWtCR3FvdktXZ3xBQ3Jtc0tsR25sTDZLZVJLN1NQQ244OHZPUkxQT3FKNmRGMnRMaWdocTFUdi1wTUQ0ODA3VFVWbU1jbFNhNHV5aEZDYmZCeENqdGduZVJySktPOHBuN3R6NmMxTmloWGNROFIzMjg2bHNmckR5Uy11aWtwMmJMYw%3D%3D&v=-vDwY1kOfNw&event=video_description

#### Major kudos to Krish Naik's channel for the idea.

### Prerequisites
Create a new virtual environment and install the dependencies from the requirements.txt file.
```
  pip install -r requirements.txt
```

### Run the backend service
To run the flask server, use the following command on project dir:
```
  python app.py
```
### Here Swagger api from flasgger is used to emulate a simple front-end (Swagger is used for API documentation)
Access from browser using ip:port followed by /apidocs
```
  localhost:5000/apidocs/
```
