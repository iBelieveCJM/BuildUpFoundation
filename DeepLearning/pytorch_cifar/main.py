#!coding:utf-8
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F

import torchvision
import torchvision.transforms as transforms
from tensorboardX import SummaryWriter

from util import datasets, Trainer
from architectures.arch import arch

def create_data_loaders(train_transform, 
                        eval_transform, 
                        datadir,
                        config):
    trainset = torchvision.datasets.CIFAR10(root=datadir,
                                            train=True,
                                            download=True,
                                            transform=train_transform)
    train_loader = torch.utils.data.DataLoader(trainset,
                                               batch_size=config.batch_size,
                                               shuffle=True,
                                               num_workers=config.workers)

    evalset = torchvision.datasets.CIFAR10(root=datadir,
                                           train=False,
                                           download=True,
                                           transform=eval_transform)
    eval_loader = torch.utils.data.DataLoader(evalset,
                                              batch_size=config.batch_size,
                                              shuffle=False,
                                              num_workers=config.workers)
    return train_loader, eval_loader

def create_loss_fn(config):
    if config.loss == 'mse':
        criterion = nn.mseloss()
    elif config.loss == 'soft':
        criterion = nn.CrossEntropyLoss()
    return criterion

def create_optim(params, config):
    if config.optim == 'sgd':
        optimizer = optim.SGD(params, config.lr,
                              momentum=config.momentum,
                              weight_decay=config.weight_decay,
                              nesterov=config.nesterov)
    elif config.optim == 'adam':
        optimizer = optim.ADAM(params, config.lr)
    return optimizer


def main(config):
    writer = SummaryWriter()

    device = 'cuda:6' if torch.cuda.is_available() else 'cpu'

    dataset_config = datasets.cifar10()
    num_classess = dataset_config.pop('num_classes')
    train_loader, eval_loader = create_data_loaders(**dataset_config, config=config)
    
    criterion = create_loss_fn(config)
    net = arch[config.arch]()
    optimizer = create_optim(net.parameters(), config)

    trainer = Trainer.Trainer(net, optimizer, criterion, device, writer)
    trainer.loop(config.epochs, train_loader, eval_loader, print_freq=config.print_freq)

    writer.close()
