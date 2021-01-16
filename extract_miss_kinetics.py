import os
import sys
from tqdm import tqdm


if not os.path.exists('kinetics_mini'):
    os.makedirs('kinetics_mini')
if not os.path.exists('kinetics_400'):
    os.makedirs('kinetics_400')
    
def main(is_mini, vpath):
    vids = [l.split('.')[0] for l in os.listdir(vpath)]
    for split in ['train', 'val', 'test']:
        if int(is_mini) == 0:
            miss_file = 'miss_%s.list'%split
            target = 'kinetics_400'
        else:
            miss_file = 'mini_miss_%s.list'%split
            target = 'kinetics_mini'
        with open('resources/'+miss_file, 'r') as f:
            vlist = [l.strip() for l in f.readlines()]
        for vname in vlist:
            vid = vname.split('/')[-1]
            print('cp %s.mp4 %s'%(os.path.join(vpath, vid), target))
            if vid in vids:
                command = 'cp %s.mp4 %s'%(os.path.join(vpath, vid), target)
                os.system(command)


if __name__ == '__main__':
    is_mini = sys.argv[1]
    vpath = sys.argv[2]
    main(is_mini, vpath)