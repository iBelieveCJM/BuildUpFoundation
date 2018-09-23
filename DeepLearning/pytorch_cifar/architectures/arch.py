#!coding:utf-8
from architectures.lenet import LeNet
from architectures.vgg import VGG11, VGG13, VGG16, VGG19
from architectures.resnet import ResNet18, ResNet34, ResNet50, ResNet101, ResNet152

arch = {
        'lenet': LeNet,
        'vgg11': VGG11,
        'vgg13': VGG13,
        'vgg16': VGG16,
        'vgg19': VGG19,
        'resnet18': ResNet18,
        'resnet34': ResNet34,
        'resnet50': ResNet50,
        'resnet101': ResNet101,
        'resnet152': ResNet152,
        }
