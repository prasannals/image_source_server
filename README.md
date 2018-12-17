# image_source_server

Server for <a href="https://expo.io/@prasannals/image-source">Image Source</a> app

### Usage

```
from image_source_server import ImageSourceServer

def train(train_dir_uri):
    print('Training on data from : ' + train_dir_uri)
    return 'Trained' # return value is returned to the Image Source App in the HTTP Response

def predict(img_uri):
    print('Predicting on ' + img_uri)
    return 'Cat'  # return value is returned to the Image Source App in the HTTP Response

serv = ImageSourceServer(train=train, predict=predict)
serv.run()
```

ImageSourceServer requires "train" and "predict" methods to be provided.

"train" method will be called with the uri of the folder containing the training images when "Train" button is pressed on the app.

"predict" method will be called with the uri of the image provided by the app for prediction. The value returned by the predict method will be returned to the app and displayed as an alert to the user.
