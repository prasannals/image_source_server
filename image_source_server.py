from flask import Flask
from flask import request
from datetime import datetime
import os
import sys

class ImageSourceServer:
    def __init__(self, train, predict, storage_dir = './data/', incoming_fname = 'image',
            image_format = '.jpg', datetime_delimiter = '_'):
        '''
        train - a function
        train(data_folder)
            data_folder - Location(string) of the folder containing all the categories of
                images saved through the /data route

        predict - a function
        predict(image_uri)
            image_uri - uri of the image on which the prediction is to be made
        '''
        self.train = train
        self.predict = predict
        self.storage_dir = storage_dir
        self.incoming_fname = incoming_fname
        self.image_format = image_format
        self.datetime_delimiter = datetime_delimiter
        self.data_dir = self.storage_dir + 'images/'  # TODO replace both this and following with os.path.join
        self.predict_dir = self.storage_dir + 'test/'
        self.app = Flask(__name__)


        @self.app.route('/data', methods=['POST'])
        def data():
            save_dir = os.path.join(self.data_dir, request.form['category'])
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)
            nextImgNum = len(os.listdir(save_dir))
            imgName = str(nextImgNum) + self.image_format
            save_path = os.path.join(save_dir, imgName)
            request.files[self.incoming_fname].save(save_path)
            return 'done'


        @self.app.route('/train', methods=['POST'])
        def train():
            stdout = sys.stdout
            log = Log(stdout)
            sys.stdout = log
            trainRes = self.train(self.data_dir, request.json)
            print(request.json)
            print(trainRes)
            sys.stdout = stdout
            return log.buffer

        @self.app.route('/predict', methods=['POST'])
        def predict():
            imgName = str(datetime.now())[:-7].replace(':', self.datetime_delimiter) + self.image_format
            save_dir = self.predict_dir
            if not os.path.exists(save_dir):
                os.makedirs(save_dir)
            save_path = os.path.join(save_dir, imgName)
            request.files[self.incoming_fname].save(save_path)

            return str(self.predict(save_path))

    def run(self, host= '0.0.0.0', port_number=12221, threaded=False):
        self.app.run(host=host, port=port_number, threaded=threaded)

class Log:
    def __init__(self, stdout):
        self.buffer = ''
        self.stdout = stdout

    def write(self, data):
        self.buffer = self.buffer + data
        self.stdout.write(data)

    def flush(self):
        self.stdout.flush()
