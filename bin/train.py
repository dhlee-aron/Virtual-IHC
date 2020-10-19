import sys

sys.path.append('./')
from src.B0_Train import train
import argparse
import time

COPYRIGHT_HOLDER = 'Arontier Inc.'

parser = argparse.ArgumentParser(
    description="""
    Train He-IHC pix2pix model  
    """,
    epilog='Copyright {} {} All rights reserved.'.format(
        time.strftime("%Y"),
        COPYRIGHT_HOLDER),
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

# Required arguments
parser.add_argument('-i', metavar='input-path',
                    type=str, dest='input_path', default='input-path',
                    help='designate a directory save output path')

# Optional arguments
parser.add_argument('-model', choices=['unet'], dest='model', default='unet',
                    help='model type in the generator architecture')
parser.add_argument('-info', metavar='run-info',
                    type=str, dest='run_info', default='model',
                    help='run-info of model')
parser.add_argument('-img-per-epoch', metavar='img-per-epoch',
                    type=int, dest='img_per_epoch', default=10000,
                    help='number of training image in an epoch')
parser.add_argument('-l1-lambda', metavar='l1-lambda',
                    type=float, dest='l1_lambda', default=10,
                    help='lambda of l1 loss')
parser.add_argument('-hed-lambda', metavar='hed-lambda',
                    type=float, dest='hed_lambda', default=0.9,
                    help='lambda of hed l1 loss')
parser.add_argument('-hed-normalize', metavar='hed-normalize',
                    type=bool, dest='hed_normalize', default=False,
                    help='hed channel normalize')
parser.add_argument('-threads', metavar='threads',
                    type=int, dest='threads', default=4,
                    help='indicate number of using threads while training')
parser.add_argument('-cuda', metavar='cuda',
                    type=bool, dest='cuda', default=True,
                    help='using cuda')
args = parser.parse_args()

if args.input_path is None:
    parser.print_help()
    exit(1)

#data_path = '/media/dong/94a07df8-6863-42d6-86f3-c96e626447dd/HE_IHC_KKM/HE_IHC_Slides/data/patch_select_0708_size25k_stratio005_ratio201_Train'
train(run_info=args.run_info, dataset_path=args.input_path,
      img_per_epoch=args.img_per_epoch,
      batch_size=1, model=args.model, input_nc=3, output_nc=3, ngf=64, ndf=64,
      epoch_count=1, niter=100, niter_decay=100, lr=0.0002,
      lr_policy='lambda', lr_decay_iters=50, beta1=0.5, cuda=args.cuda,
      threads=args.threads, seed=123, lamb=args.l1_lambda,
      lamb_hed=args.hed_lambda, hed_normalize=args.hed_normalize)
