import json
import argparse
from trainer import train

def main():
    args = setup_parser().parse_args()
    tag = args.config.split('/')[-1].split('.json')[0]
    mode = args.mode
    param = load_json(args.config)
    
    # rewrite parameters
    if args.device!=None:
        print('new setting [device]:', args.device)
        param['device'] = [str(args.device)]
    if args.tuned_epoch!=None:
        print('new setting [tuned_epoch]:', args.tuned_epoch)
        param['tuned_epoch'] = args.tuned_epoch
        
    args_dict = vars(args)  # Converting argparse Namespace to a dict.
    args_dict.update(param)  # Add parameters from json
    train(args_dict, tag, mode)

def load_json(settings_path):
    with open(settings_path) as data_file:
        param = json.load(data_file)
    return param

def setup_parser():
    parser = argparse.ArgumentParser(description='Reproduce of multiple continual learning algorthms.')
    parser.add_argument('--config', type=str, default='./exps/finetune.json',
                        help='Json file of settings.')
    parser.add_argument('--mode', type=str, default='train-eval')
    parser.add_argument('--device', type=int)
    parser.add_argument('--tuned_epoch', type=int)
    return parser

if __name__ == '__main__':
    main()