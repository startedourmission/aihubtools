#class for aihub dataset handling
# '/Users/cha/DATASET/168.한국 전통 수묵화 화풍별 제작 데이터'
import zipfile
import os
import glob
import json
import shutil
from tqdm import tqdm

import mapper


class aihubdata:
    def __init__(self, path=None, datakey=None):
        self.datakey = datakey
        self.path = path
        
    def treeview(self, path=None, n=0, sorted_view=True):
        if not path:
            path = self.path

        with os.scandir(path) as it:  
            for entry in sorted(it, key=lambda e: e.name) if sorted else it:
                if entry.is_dir():
                    print('\t' * n, entry.name, ':', len(os.listdir(entry.path)))
                    self.treeview(entry.path, n + 1)
                else:
                    print('\t' * n, entry.name)
  
    def unzip(self): 
        zip_list = os.listdir(self.path)
        for i in tqdm(zip_list):

            zip_file = zipfile.ZipFile(PATH + file_name)
            zip_file.extractall(path=OUTPUT_PATH + i + '/images/')

        print('complete')

class objectDetection(aihubdata):

    def hub2yolo(self):
        pass            

    def xyxy2yolo(self, classid, bbox, width, height):
        x_center = (bbox[0] + bbox[2]) / 2 / width
        y_center = (bbox[1] + bbox[3]) / 2 / height
        bbox_width = (bbox[2] - bbox[0]) / width
        bbox_height = (bbox[3] - bbox[1]) / height

        return f"{classid} {x_center} {y_center} {bbox_width} {bbox_height}\n"    
        

if __name__ == '__main__':

    # Paths
    SOURCE_DIR_PATH = '/scratch/e1430a12/workspace/ODLE/71377/'
    OUTPUT_DIR_PATH = '/scratch/e1430a12/workspace/ODLE/71377_val_yolo2'
    print(SOURCE_DIR_PATH)
    print(OUTPUT_DIR_PATH)

    for i in tqdm(glob.glob(os.path.join(SOURCE_DIR_PATH,'L*', 'labels'))):
        result_path = os.path.join(OUTPUT_DIR_PATH, 'labels')
        os.makedirs(result_path, exist_ok=True)
        convert(i, result_path)

