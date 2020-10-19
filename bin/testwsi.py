import os
import sys

sys.path.append('./')
from src.C1_WSI_test import predict_wsi
import argparse
import time

COPYRIGHT_HOLDER = 'Arontier Inc.'

parser = argparse.ArgumentParser(
    description="""
    Test H&E WSI  
    """,
    epilog='Copyright {} {} All rights reserved.'.format(
        time.strftime("%Y"),
        COPYRIGHT_HOLDER),
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

# Required arguments
parser.add_argument('-f', metavar='filename',
                    type=str, dest='filename', default='filename',
                    help='designate a directory save output path')

# Optional arguments
parser.add_argument('-model-name', metavar='model-name',
                    type=str, dest='model_name', default='model_20200708',
                    help='designate a directory model checkpoint path')
parser.add_argument('-model-path', metavar='model-path',
                    type=str, dest='model_path', default='./data/checkpoints',
                    help='designate a directory model checkpoint path')
parser.add_argument('-input-path', metavar='wsi-input-path',
                    type=str, dest='input_path', default='./data/wsi/test_slide',
                    help='designate a directory input path')
parser.add_argument('-output-path', metavar='output-path',
                    type=str, dest='output_path', default='./data/result/wsi',
                    help='designate a directory output path')
args = parser.parse_args()

if args.filename is None:
    parser.print_help()
    exit(1)

if not os.path.exists(args.output_path):
    os.makedirs(args.output_path, exist_ok=True)

# Testing settings
input_file_path = os.path.join(args.input_path, '{}.svs'.format(args.filename))
model_file_path = os.path.join(args.model_path,'{}.pth'.format(args.model_name))
predict_wsi(input_file_path, args.output_path, model_file_path)
