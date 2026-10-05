
# coding: utf-8

import os
import cv2
import numpy as np
import tensorflow as tf

from datetime import datetime
from alexnet import AlexNet
import matplotlib.pyplot as plt
from datagenerator import ImageDataGenerator

from glob import glob
from keras.preprocessing import image                  
from tqdm import tqdm

from sklearn.datasets import fetch_lfw_people
from sklearn.metrics import auc
from sklearn.metrics import roc_curve
from sklearn import metrics
from scipy import interp

from utils import getTrainTestData, convertToCategorical, calRoc

# load data
trainFile, testFile, validFile, numberClasses = getTrainTestData(vggModel=False)

# model params
learningRate = 0.001
numEpochs = 1
batchSize = 20
dropRate = 0.5
finetuneModel = False

import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()

x = tf.placeholder(tf.float32, [batchSize, 227, 227, 3])
y = tf.placeholder(tf.float32, [None, numberClasses])
keepProb = tf.placeholder(tf.float32)

# Initialize model with trainLayers
if finetuneModel:
    trainLayers = ['fc8', 'fc7']
    model = AlexNet(x, keepProb, numberClasses, trainLayers)
else:
    trainLayers = ['fc8']
    model = AlexNet(x, keepProb, numberClasses, trainLayers)

with tf.name_scope("modelF"):
    # Loss op
    logit = model.fc8
    pred = tf.nn.softmax(logit, name='pred')
    varList = [v for v in tf.trainable_variables() if v.name.split('/')[0] in trainLayers]
    print(varList)
    loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits = logit, labels = y))
    # Train op
    gradients = list(zip(tf.gradients(loss, varList), varList))
    optimizer = tf.train.GradientDescentOptimizer(learningRate)
    
    trainOp = optimizer.apply_gradients(grads_and_vars=gradients)
    # Evaluation op
    curPred = tf.equal(tf.argmax(logit, 1), tf.argmax(y, 1))
    accuracy = tf.reduce_mean(tf.cast(curPred, tf.float32))

trainGenerator = ImageDataGenerator(trainFile, horizontal_flip = True, nb_classes = numberClasses)
testGenerator = ImageDataGenerator(testFile, nb_classes = numberClasses)
validGenerator = ImageDataGenerator(validFile, nb_classes = numberClasses)

trainBatches = np.floor(trainGenerator.data_size / batchSize).astype(np.int16)
testBatches = np.floor(testGenerator.data_size / batchSize).astype(np.int16)
validBatches = np.floor(validGenerator.data_size / batchSize).astype(np.int16)

ckptPath = "alexnetModel/"
if not os.path.isdir(ckptPath): os.mkdir(ckptPath)
# Initialize an saver for store model checkpoints
saver = tf.train.Saver()

with tf.Session() as sess:
    # Initialize all variables
    sess.run(tf.global_variables_initializer())

    # Load the pretrained weights into the non-trainable layer
    model.load_initial_weights(sess)
    
    if 1:
      for i in range(0, 1):
        for epoch in range(numEpochs):
            print("Epoch number: {}".format(epoch + 1))
            step = 1
            # train the model
            while step < trainBatches:
                batchX, batchY = trainGenerator.next_batch(batchSize)
                sess.run(trainOp, feed_dict={x: batchX, y: batchY, keepProb: dropRate})
                step += 1
            # validate the model
            validAcc = 0.0
            for _ in range(validBatches):
                batchX, batchY = validGenerator.next_batch(batchSize)
                acc = sess.run(accuracy, feed_dict={x: batchX, y: batchY, keepProb: 1.0})
                validAcc += acc
            validAcc /= validBatches
            print("Start validation with valid acc {}".format(validAcc))

            # Reset
            validGenerator.reset_pointer()
            trainGenerator.reset_pointer()
    # Calculate Test Accuracy
    yPred = []
    yTest = []
    orgYPred = []
    testAccT = 0.0
    # orgTestAcc = 0.0
    for _ in range(testBatches):
        testBatchX, testBatchY = testGenerator.next_batch(batchSize)
        yTest.append(testBatchY)
        testAcc, testPred = sess.run([accuracy, logit], feed_dict={x: testBatchX, y: testBatchY, keepProb: 1.0})
        # orgTestAcc, orgTestPred = sess.run([orgAcc, orgLogits], feed_dict={x: testBatchX, y: testBatchY, keepProb: 1.0})
        #print(test_pred.shape)
        yPred.append(np.argmax(testPred, 1))
        # orgYPred.append(np.argmax(orgTestPred, 1))
        testAccT += testAcc
        # orgTestAcc += orgTestAcc
    # print('Org Testing Accuracy: {}'.format(orgTestAcc / testBatches))
    if finetuneModel:
        print('finetuneModel Testing Accuracy: {}'.format(testAccT / testBatches))
    else:
        print('Org Testing Accuracy: {}'.format(testAccT / testBatches))

yTest = np.array(yTest).reshape((-1, numberClasses))
yPred = np.squeeze(np.array(yPred).reshape((-1, 1)))
yPred = convertToCategorical(yPred, numClasses=numberClasses)

if finetuneModel:
    saveName = 'alexnetModelResultsWithFinetune'
else:
    saveName = 'alexnetModelResultsWithoutFinetune'
calRoc(numberClasses, np.array(yTest), np.array(yPred), saveName)


