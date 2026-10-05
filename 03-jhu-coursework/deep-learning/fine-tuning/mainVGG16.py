# coding: utf-8
# +
import sys
sys.path.append('/Downloads/HW of DL/DL_Hw3_Reynold Hu')  # path contains python_file.py

import vgg16
# -
import numpy as np

import keras
from vgg16 import VGG16
from keras.layers import Dense, Activation, Flatten
from keras.layers import merge, Input
from keras.models import Model
from keras.layers import Dense, Activation
from sklearn import metrics

from utils import getTrainTestData, convertToCategorical, calRoc

# load data
trainTensors, yTrain, validTensors, yValid, testTensors, yTest, numberClasses = getTrainTestData(vggModel=True)

learningRate = 0.001
numEpochs = 3
batchSize = 20

imageInput = Input(shape=(224, 224, 3))
model = VGG16(include_top=True, input_tensor=imageInput, weights='imagenet')
#model.summary()

print('classes: ', numberClasses)
lastLayer = model.get_layer('block5_pool').output
x = Flatten(name='flatten')(lastLayer)
x = Dense(1024, activation='relu', name='fc1')(x)
x = Dense(128, activation='relu', name='fc2')(x)
out = Dense(numberClasses, activation='softmax', name='output')(x)
vggModel = Model(imageInput, out)

vggModel.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.SGD(lr=learningRate),
              metrics=['accuracy'])

for layer in vggModel.layers[:-3]:
    layer.trainable = False

# vggModel.summary()

last_layer = model.get_layer('fc2').output
out = Dense(numberClasses, activation='softmax', name='output')(last_layer)
normalModel = Model(imageInput, out)
#normalModel.summary()

normalModel.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.SGD(lr=learningRate),
              metrics=['accuracy'])

hist = vggModel.fit(trainTensors, yTrain,
          batch_size=batchSize,
          epochs=numEpochs,
          verbose=1,
          validation_data=(validTensors, yValid))
          #,callbacks=[history])

(loss, accuracy) = vggModel.evaluate(testTensors, yTest, batch_size=10, verbose=1)
print("[VGG16 MODEL TESTING RESULTS (WITH FINE-TUNING)] loss={:.4f}, accuracy: {:.4f}%".format(loss, accuracy * 100))

(loss, accuracy) = normalModel.evaluate(testTensors, yTest, batch_size=10, verbose=1)
print("[VGG16 MODEL TESTING RESULTS (WITHOUT FINE-TUNING)] loss={:.4f}, accuracy: {:.4f}%".format(loss, accuracy * 100))


pred = vggModel.predict(testTensors)
pred = np.argmax(pred, axis=1)
yPred = convertToCategorical(pred, numClasses=numberClasses)

yCompare = np.argmax(yTest, axis=1)
score = metrics.accuracy_score(yCompare, pred)
print('accuracy with metrics: ', score)

calRoc(numberClasses, yTest, yPred, 'vggModelResults')
