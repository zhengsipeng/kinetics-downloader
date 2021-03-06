import os
import sys
import json
from tqdm import tqdm

    
def main(is_mini, vpath):
    if not os.path.exists('kinetics_mini'):
        os.makedirs('kinetics_mini')
    if not os.path.exists('kinetics_400'):
        os.makedirs('kinetics_400')

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


def gen_miss_json(split):
    with open('resources/origin/kinetics_%s.json'%split, 'r') as f:
        annos = json.load(f)
    with open('resources/mini_miss_val.list', 'r') as f:
        misslist = [l.split('/')[-1][:11] for l in f.readlines()]
    with open('resources/mini_miss_test.list', 'r') as f:
        misslist += [l.split('/')[-1][:11] for l in f.readlines()]
    with open('resources/mini_miss_train.list', 'r') as f:
        misslist += [l.split('/')[-1][:11] for l in f.readlines()]
    print(len(misslist))
    new_anno = dict()
    for vid in tqdm(annos):
        if vid in misslist:
            new_anno[vid] = annos[vid]
    print(len(new_anno.keys()))
    with open('resources/kinetics_%s.json'%split, 'w') as f:
        json.dump(new_anno, f)


if __name__ == '__main__':
    #is_mini = sys.argv[1]
    #vpath = sys.argv[2]
    #main(is_mini, vpath)
    gen_miss_json('train')