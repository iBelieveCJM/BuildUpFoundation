#!coding:utf-8
from pathlib import Path
import torch

class Trainer:

    def __init__(self, model, optimizer, loss_fn, device, writer=None, save_dir=None, save_freq=5):
        self.model = model # model.to(device)
        self.optimizer = optimizer
        self.loss_fn = loss_fn
        self.save_dir = save_dir
        self.save_freq = save_freq
        self.device = device
        self.writer = writer
        self.global_step = 0
        self.epoch = 0
        
    def _iteration(self, data_loader, print_freq, is_train=True):
        loop_loss = []
        accuracy = []
        mode = "train" if is_train else "test"
        for batch_idx, (data, targets) in enumerate(data_loader):
            self.global_step += batch_idx
            data, targets = data.to(self.device), targets.to(self.device)
            outputs = self.model(data)
            loss = self.loss_fn(outputs, targets)
            if is_train:
                self.optimizer.zero_grad()
                loss.backward()
                self.optimizer.step()

            loop_loss.append(loss.item() / len(data_loader))
            acc = (outputs.max(1)[1]==targets).sum().item()
            accuracy.append(acc)
            if print_freq>0 and (batch_idx%print_freq)==0:
                print(f"[{mode}]loss[{batch_idx:<3}]\t loss: {loss.item():.3f}\t Acc: {acc/data.size(0):.3%}")
            if self.writer:
                self.writer.add_scalar(mode+'_global_loss', loss.item(), self.global_step)
                self.writer.add_scalar(mode+'_global_accuracy', acc/data.size(0), self.global_step)
        print(f">>>[{mode}]loss\t loss: {sum(loop_loss):.3f}\t Acc: {sum(accuracy)/len(data_loader.dataset):.3%}")
        if self.writer:
            self.writer.add_scalar(mode+'_epoch_loss', sum(loop_loss), self.epoch)
            self.writer.add_scalar(mode+'_epoch_accuracy', sum(accuracy)/len(data_loader.dataset), self.epoch)

        return loop_loss, accuracy

    def train(self, data_loader, print_freq=20):
        self.model.train()
        with torch.enable_grad(): #torch.enable_grad():
            loss, correct = self._iteration(data_loader, print_freq)

    def test(self, data_loader, print_freq=10):
        self.model.eval()
        with torch.no_grad():
            loss, correct = self._iteration(data_loader, print_freq, is_train=False)

    def loop(self, epochs, train_data, test_data, scheduler=None, print_freq=-1):
        for ep in range(epochs):
            self.epoch = ep
            if scheduler is not None:
                scheduler.step()
            print("------ Training epochs: {} ------".format(ep))
            self.train(train_data, print_freq)
            print("------ Testing epochs: {} ------".format(ep))
            self.test(test_data, print_freq)
            if ep % self.save_freq == 0:
                self.save(ep)


    def save(self, epoch, **kwargs):
        if self.save_dir is not None:
            model_out_path = Path(self.save_dir)
            state = {"epoch": epoch,
                    "weight": self.model.state_dict()}
            if not model_out_path.exists():
                model_out_path.mkdir()
            torch.save(state, model_out_path / "model_epoch_{}.pth".format(epoch))
