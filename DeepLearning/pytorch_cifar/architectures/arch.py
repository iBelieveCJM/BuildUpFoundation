#!coding:utf-8
from architectures.lenet import LeNet
from architectures.vgg import VGG11, VGG13, VGG16, VGG19
from architectures.resnet import ResNet18, ResNet34, ResNet50, ResNet101, ResNet152
from architectures.preact_resnet import PreActResNet18, PreActResNet34, PreActResNet50, PreActResNet101, PreActResNet152

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
        'preact_resnet18': PreActResNet18,
        'preact_resnet34': PreActResNet34,
        'preact_resnet50': PreActResNet50,
        'preact_resnet101': PreActResNet101,
        'preact_resnet152': PreActResNet152,
        }
