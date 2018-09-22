import sys
import torch

import main

def parameters():
    defaults = {
        # Technical details
        'is_parallell': True,
        'workers': 2,
        'checkpoint_epochs': 20,

        # Data
        'dataset': 'cifar10',
        #'train_subdir': 'train+val',
        #'eval_subdir': 'test',

        # Data sampling
        'base_batch_size': 100, #128,

        # Architecture
        'arch': 'cifar_cnn',

        # Optimization
        'epochs': 400,
        'base_lr': 0.1,
        'nesterov': True,
    }

def run(title, base_batch_size, base_lr, n_labels, data_seed, is_parallel, **kwargs):
    if is_parallel:
        ngpu = torch.cuda.device_count()
    else:
        ngpu = 1
    adapted_args = {
        'batch_size': base_batch_size * ngpu,
        'labeled_batch_size': base_labeled_batch_size * ngpu,
        'lr': base_lr * ngpu,
    }
    main.args = parse_dict_args(**adapted_args, **kwargs)
    main.main(context)


if __name__ == "__main__":
    for run_params in parameters():
        run(**run_params)
