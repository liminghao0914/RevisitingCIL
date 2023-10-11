import os
import json

# 1. Read the template file in json format
with open('./configs/minghaocil_omnibenchmark.json', 'r') as f:
    config = json.load(f)

# 2. Set the parameters
for alpha in [0,0.2,0.5,0.8]:
    for beta in [0.25, 0.5, 1]:
        for data_aug in ['random_all', 'train']:
            for loss_fn in ['cross_entropy','focal_loss']:
                for vpt_type in ['deep','shallow']:
                    for opt in ['sgd','adam']:
                        for lr in [0.05, 0.1, 0.2]:
                            for wd in [0.001, 0.003, 0.005]:
                                if opt == 'adam':
                                    continue
                                if vpt_type == 'shallow':
                                    continue
                                if loss_fn == 'focal_loss':
                                    continue
                                with open(f'./configs/exps8/minghaocil_lr_{lr}_wd_{wd}_opt_{opt}_vt_{vpt_type}_loss_{loss_fn}_da_{data_aug}_alpha_{alpha}_beta_{beta}.json', 'w') as f:
                                    config['weight_decay'] = wd
                                    config['init_lr'] = lr
                                    config['optimizer'] = opt
                                    config["device"] = ["0","1","2","3"]
                                    config["vpt_type"] = vpt_type
                                    config["batch_size"] = int(432/4*len(config["device"]))
                                    config["loss_fn"] = loss_fn
                                    config["prompt_token_num"] = 3
                                    config["data_augmentation"] = data_aug
                                    config["tuned_epoch"] = 20
                                    config["alpha"] = alpha
                                    config["beta"] = beta
                                    json.dump(config, f, indent=4)