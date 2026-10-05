import warnings
from PIL import Image
import os
import os.path
import numpy as np
import torch
import codecs
import string
from typing import Any, Callable, Dict, List, Optional, Tuple
from urllib.error import URLError
import shutil
import torchvision.datasets.mnist as mnist

class MNIST():

    def __init__(
            self,
            target_label: int = 0,
            train: bool = True,
            transform: Optional[Callable] = None) -> None:
        
        self.train = train  # training set or test set
        self.transform = transform
        self.data, self.targets = self._load_data()
        self.target_label = target_label

    def _load_data(self):
        if self.train:
            image_file = './data/raw/train-images-idx3-ubyte'
            label_file = './data/raw/train-labels-idx1-ubyte'
            sample_size = 20000
        else:
            image_file = './data/raw/t10k-images-idx3-ubyte'
            label_file = './data/raw/t10k-labels-idx1-ubyte'
            sample_size = 2000
         
        data = mnist.read_image_file(image_file)[:sample_size]
        targets = mnist.read_label_file(label_file)[:sample_size]
        return data, targets

    def __getitem__(self, index: int) -> Tuple[Any, Any]:
        img = self.data[index]
        if int(self.targets[index]) == self.target_label:
            target = float(1.0)
        else:
            target = float(0.0)
        img = Image.fromarray(img.numpy(), mode='L')
        if self.transform is not None:
            img = self.transform(img)
        return img, target

    def __len__(self) -> int:
        return len(self.data)
