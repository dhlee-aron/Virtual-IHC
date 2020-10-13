import os
import re
import openslide
import numpy as np
import matplotlib.pyplot as plt
import glob
os.getcwd()

base_path = './data/wsi/'
def Points_Split(temp_points_str):
    temp_points_str = temp_points_str.replace('[', '')
    temp_points_str = temp_points_str.replace(' ]', '')
    temp_points_str = temp_points_str.split('Point: ')[1:]
    return temp_points_str


# anno_path = os.path.join(base_path, 'annotation')

files_list = glob.glob(os.path.join(base_path, 'hotspot_annotation_qpdata/*'))

for i in range(len(files_list)):
    annotation = {}
    files_path = files_list[i]
    file_name = os.path.splitext(os.path.basename(files_path))[0]
    annotation[file_name] = {}
    idx = 0

    with open(os.path.join(files_path), 'r') as f:
        file_path = f.readline().replace("\n", '')
        annotation[file_name]['path'] = file_path
        for line1, line2 in zip(f, f):
            #            break
            line_name = line1.replace("\n", '')
            line_coord = line2.replace("\n", '')
            annotation[file_name][str(idx)] = {}
            annotation[file_name][str(idx)]['class'] = line_name

            coord_x = [int(float(i)) for idx, i in
                       enumerate(re.findall('\d*\.\d*', line_coord)) if
                       idx % 2 == 0]
            coord_y = [int(float(i)) for idx, i in
                       enumerate(re.findall('\d*\.\d*', line_coord)) if
                       idx % 2 == 1]

            annotation[file_name][str(idx)]['coord'] = [min(coord_x),
                                                        min(coord_y),
                                                        max(coord_x),
                                                        max(coord_y)]
            idx += 1

    np.save(os.path.join(base_path,
                         'hotspot_annotation',
                         '{}.npy'.format(file_name)),
            annotation)


