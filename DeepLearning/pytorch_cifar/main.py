#!coding:utf-8
import torch
import torch.nn as nn
import torch.optim as optim
import torch.nn.functional as F
from torch.optim import lr_scheduler

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

def create_lr_scheduler(optimizer, config):
    if config.lr_scheduler == 'cos':
        scheduler = lr_scheduler.CosineAnnealingLR(optimizer,
                                                   T_max=config.epochs,
                                                   eta_min=config.min_lr)
    elif config.lr_scheduler == 'multistep':
        if config.steps=="":
            return None
        scheduler = lr_scheduler.MultiStepLR(optimizer,
                                             milestones=config.steps,
                                             gamma=config.gamma)
    return scheduler

def main(config):
    with SummaryWriter(comment='_{}_{}'.format(config.arch,config.dataset)) as writer:
        dataset_config = datasets.cifar10()
        num_classes = dataset_config.pop('num_classes')
        train_loader, eval_loader = create_data_loaders(**dataset_config, config=config)

        dummy_input = (torch.randn(10,3,32,32),)
        net = arch[config.arch](num_classes)
        writer.add_graph(net, dummy_input)

        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        criterion = create_loss_fn(config)
        if config.is_parallel:
            net = torch.nn.DataParallel(net).to(device)
        else:
            net = net.to(device)
        optimizer = create_optim(net.parameters(), config)
        scheduler = create_lr_scheduler(optimizer, config)

        trainer = Trainer.Trainer(net, optimizer, criterion, device, writer)
        trainer.loop(config.epochs, train_loader, eval_loader, scheduler=scheduler, print_freq=config.print_freq)
