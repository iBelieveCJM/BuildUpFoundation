#!coding:utf-8
from pathlib import Path
import torch

from tqdm import tqdm

class Trainer:

    def __init__(self, model, optimizer, loss_fn, device, save_dir=None, save_freq=5):
        self.model = model
        self.optimizer = optimizer
        self.loss_fn = loss_fn
        self.save_dir = save_dir
        self.save_freq = save_freq
        self.device = device
        
    def _iteration(self, data_loader, is_train=True):
        loop_loss = []
        accuracy = []
        for data, targets in tqdm(data_loader, ncols=80):
            data, targets = data.to(self.device), targets.to(self.device)
            outputs = self.model(data)
            loss = self.loss_fn(outputs, targets)
            loop_loss.append(loss.item() / len(data_loader))
            accuracy.append((output.max(1)[1]==target).sum().item())
            if is_train:
                self.optimizer.zero_grad()
                loss.backward()
                self.optimizer.step()
        mode = "train" if is_train else "test"
        print(f">>>[{mode}]loss: {sum(loop_loss):.2f}/accuracy: {sum(accuracy)/ len(data_loader.dataset):.2%}")
        return loop_loss, accuracy

    def train(self, data_loader):
        self.model.train()
        with torch.set_grad_enabled(): #torch.enable_grad():
            loss, correct = slef._iteration(data_loader)

    def test(self, data_loader):
        self.model.eval()
        with torch.no_grad():
            loss, correct = self._iteration(data_loader, is_train=False)

    def loop(self, epochs, train_data, test_data, scheduler=None):
        for ep in range(1, epochs+1):
            if scheduler is not None:
                scheduler.step()
            print("epochs: {}".format(ep))
            self.train(train_data)
            self.test(test_data)
            if ep % self.save_freq:
                self.save(ep)

    def save(self, epoch, **kwargs):
        if self.save_dir is not None:
            model_out_path = Path(self.save_dir)
            state = {"epoch": epoch,
                    "weight": self.model.state_dict()}
            if not model_out_path.exists():
                model_out_path.mkdir()
            torch.save(state, model_out_path / "model_epoch_{}.pth".format(epoch))
