import sys
import torch

import main
from util.Config import parse_dict_args

def parameters():
    defaults = {
        # Technical details
        'is_parallel': False,
        'workers': 2,
        'checkpoint_epochs': 20,

        # Data
        'dataset': 'cifar10',
        'base_batch_size': 128,
        'print_freq': 30,

        # Architecture
        #'arch': 'lenet',
        #'arch': 'vgg19',
        #'arch': 'resnet152',
        #'arch': 'preact_resnet152',
        #'arch': 'densenet',
        #'arch': 'resnext29_2x64d',
        'arch': 'senet',

        # Optimization
        'loss': 'soft',
        'optim': 'sgd',
        'epochs': 500,
        'base_lr': 0.01,
        'momentum': 0.9,
        'weight_decay': 5e-4,
        'nesterov': True,

        # lr_schedular
        'lr_scheduler': 'multistep',
        'steps': '80,120,300',
    }

    yield {**defaults}

def run(base_batch_size, base_lr, is_parallel, **kwargs):
    if is_parallel and torch.cuda.is_available():
        ngpu = torch.cuda.device_count()
    else:
        ngpu = 1
    adapted_args = {
        'batch_size': base_batch_size * ngpu,
        'lr': base_lr * ngpu,
    }
    args = parse_dict_args(**adapted_args, **kwargs)
    main.main(args)


if __name__ == "__main__":
    for run_params in parameters():
        run(**run_params)
