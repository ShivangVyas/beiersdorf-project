import matplotlib.pyplot as plt
import pickle
import os

import numpy as np
import torch
from torch import nn
from torch import optim
import torch.nn.functional as F
from torchvision import datasets, transforms, models
from PIL import Image
from torch.autograd import Variable


def classify_image(img_path):

    img = Image.open(img_path)

    transformation = transforms.Compose([
                                         transforms.Resize(256),
                                         transforms.CenterCrop(224),
                                         transforms.ToTensor(),
                                         transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
                                         ])

    transformed_img = transformation(img)
    batch_img = torch.unsqueeze(transformed_img, 0)

    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model = torch.load('grocerymodel_resnet_v3.pth', map_location=device)
    model.eval()
    output = model(batch_img)
    # print('output: \n', output)
    index = output.data.cpu().numpy().argmax()
    print('index: ', index)

    # load class labels from json file
    label_file_path = "class_label_list.pickle"
    # print(label_file_path)
    class_labels = pickle.load(open(label_file_path, "rb"))

    img_label = class_labels[index]
    print("Class label: ", img_label)
    return img_label




if __name__ == '__main__':

    snapshot_dir = 'snapshots/banana_1.jpg'
    classify_image(snapshot_dir)