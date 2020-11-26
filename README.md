# Cotton-Disease-Prediction

<p float="left">
  <img src="models/images/strealit2.png" width="100" />
  <img src="models/images/strealit2" width="100" /> 
</p>

### Data
Cotton disease dataset: https://drive.google.com/drive/folders/1vdr9CC9ChYVW2iXp6PlfyMOGD-4Um1ue

### Model training
Cotton disease prediction model training was done using,
 - pre-trained models such as **ResNet50, ResNet152V2, VGG19, InceptionV3** 
 - an **optimized CNN model**
 
All models were trained on Google Colab environment using GPUs.

### Model Evaluation
All models except ResNet50 showed excellent accuracy but ultimately **VGG19** model was chosen because of it's ***less model size*** compared to others.

 - *CNN Model showed great accuracy but it had the largest model size. Used Data augmentation techniques and keras-tuner to find optimal set of model parameters to obtain the best CNN model*

***Major kudos to Krish Naik's channel for the idea.***

### Pre-requisites
Create a new virtual environment and install the dependencies from the requirements.txt file.
```
  pip install -r requirements.txt
```
### Run Streamlit Application
Streamlit is an open-source library for rapid ML prototyping
```
  streamlit run app.py
```
### To run flask application
To run the flask server, use the following command on project dir:
```
  python app.py
```
