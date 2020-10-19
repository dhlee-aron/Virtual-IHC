import sys
sys.path.append('./')
from src.A1_MakeTrainDataset import makedataset
import argparse
import time

COPYRIGHT_HOLDER = 'Arontier Inc.'

parser = argparse.ArgumentParser(
    description="""
    Make Train Dataset by sampling Regstrationed patch images. 
    """,
    epilog='Copyright {} {} All rights reserved.'.format(
        time.strftime("%Y"),
        COPYRIGHT_HOLDER),
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

# Required arguments
parser.add_argument('-o', metavar='output-path',
                    type=str, dest='output_path', default='output-path',
                    help='designate a directory save output path')

# Optional arguments
parser.add_argument('-b', metavar='threshold-bgratio',
                    type=float, dest='threshold_bgratio', default=0.9,
                    help='threshold of back ground ratio')
parser.add_argument('-t', metavar='threshold-tsr',
                    type=int, dest='threshold_tsr', default=0.05,
                    help='threshold of tumor stroma ratio')
parser.add_argument('-p', metavar='threshold-prob',
                    type=list, dest='threshold_prob', default=[1, 0.1, 0.01],
                    help='threshold of probability')
args = parser.parse_args()

if args.output_path is None:
    parser.print_help()
    exit(1)

makedataset(save_dir=args.output_path,
            threshold_bgratio=args.threshold_bgratio,
            threshold_tsr=args.threshold_tsr,
            threshold_prob=args.threshold_prob)
