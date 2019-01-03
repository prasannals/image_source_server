# image_source_server

Server for <a href="https://expo.io/@prasannals/image-source">Image Source</a> app

### Usage

1. Install <a href="http://flask.pocoo.org/">Flask</a> if you haven't already (Flask comes preinstalled if you have Anaconda)
```
pip install Flask
```
2. Install image_source_server. 
```
pip install image_source_server
```
3. Create an ImageSourceServer object, implement the "train" and "predict" methods and pass it into the ImageSourceServer constructor (example shown below)
```
from image_source_server import ImageSourceServer

def train(train_dir_uri, params):
    print('Training on data from : ' + train_dir_uri)
    print('Train params : ' + str(params))
    return 'Trained' # return value is returned to the Image Source App in the HTTP Response

def predict(img_uri):
    print('Predicting on ' + img_uri)
    return 'Cat'  # return value is returned to the Image Source App in the HTTP Response

serv = ImageSourceServer(train=train, predict=predict)
serv.run()
```

* "train" method will be called with the uri of the folder containing the training images when "Train" button is pressed on the app.
```
train(train_dir_uri, params)
    train_dir_uri - uri of the directory containing folders which in turn contain the images
    params - training parameters (list of key-value pairs) passed from the Image Source app
```
* "predict" method will be called with the uri of the image provided by the app for prediction. The value returned by the predict method will be returned to the app and displayed as an alert to the user.
```
predict(image_uri)
    image_uri - the uri of the image on which the prediction needs to be made
    return value - will be converted to a string (if not already a string) and sent to the Image Source app. This string will be displayed as an alert to the user
```
* "serv.run()" starts the server
4. Install the Expo app. <a href="https://play.google.com/store/apps/details?id=host.exp.exponent">Play Store Link</a> (Although there is an Expo app for iOS, Apple doesn't allow for other apps to be run on the Expo app. An iOS stand alone Image Source app release is planned in future.)
5. Visit <a href="https://expo.io/@prasannals/image-source">Image Source</a> app page on expo. Scan the QR code on your Expo android app to open the Image Source app.
6. Run the server script (and make sure you've called the "run" method)

#### Configure the app to work with server
1. Go to "Settings" tab on the Image Source app.
2. Click on "Add" button.
3. Next to the "Host" entry, enter your SERVER'S IP ADDRESS(Example: 192.168.1.130 ).
4. Next to the "Port" entry, enter your SERVER'S PORT NUMBER. By default, image source server runs on port 12221. So, if you haven't passed in an argument in the the ImageSourceServer constructor to specify a custom port, enter 12221 here.
5. Click "Save".
6. The Image Source app is now configured to send the data to the specified server. You may add other servers too (but one server is mandatory). 

#### Curating and sending data
1. Click on "Select Image" and select the image and it's category. 
2. Click on "Submit" to add the image to the app.
3. When the pics need to be transfered to server, click on "Send all images to server". This transfers all images to server. You may then check 'data/images' directory on the folder where the server was run to check for the received pics.

#### Training 
1. Go to "Train" tab on the Image Source app.
2. Click on "Add Parameter" to add training parameters. Training parameters are key value pairs. All the key value pairs will be sent to the server which will then pass it to the "train" method.
3. Click on the "Train" button to start training.

#### Prediction
1. Go to "Predict" tab on the Image Source app.
2. Select the image to be sent to server for prediction.
3. Click on "Submit"
4. The image will be sent to server and the prediction will be displayed as an alert once the server responds.
