
import sys
sys.path.append('./')
from src.A1_ImageRegistration import GetRegistrationCoordinate, MakePatchImage
import argparse
import time

COPYRIGHT_HOLDER = 'Arontier Inc.'

parser = argparse.ArgumentParser(
    description="""
    Global and Local Registration Between paired H&E , CK WSI 
    """,
    epilog='Copyright {} {} All rights reserved.'.format(
        time.strftime("%Y"),
        COPYRIGHT_HOLDER),
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

# Required arguments
parser.add_argument('-p', metavar='patient-id',
                    type=str, dest='patient_id', default='patient-id',
                    help='patient-id of WSI. it contains HE, CK, C4D, etc. stainings')

# Optional arguments
parser.add_argument('-i', metavar='wsi-path',
                    type=str, dest='wsi_path', default='wsi-path',
                    help='designate a directory containing input wsi')
parser.add_argument('-down', metavar='downsample',
                    type=int, dest='downsample', default=32,
                    help='Downsample WSI for making faster registation result')
parser.add_argument('-workers', metavar='workers',
                    type=int, dest='n_worker', default=4,
                    help='number of multiprocess workers')
args = parser.parse_args()

if args.patient_id is None:
    parser.print_help()
    exit(1)
if args.wsi_path is None:
    parser.print_help()
    exit(1)

GetRegistrationCoordinate(patient_id=args.patient_id,
                          wsi_path=args.wsi_path,
                          Downsample_Times=args.downsample,
                          n_workers=args.n_worker)

MakePatchImage(patient_id=args.patient_id,
               wsi_path=args.wsi_path,
               Downsample_Times=args.downsample,
               patch_name='patch_512')
