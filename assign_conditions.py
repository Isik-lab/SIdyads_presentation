#
import os
import shutil
import glob
import time
import argparse

import numpy as np
import pandas as pd

def get_past_runs(SID=77):
    toppath = os.path.join('data', f'subj{str(SID).zfill(3)}')
    if os.path.exists(toppath):
        #If the subject runs have already been made, print the runs that have been completed.
        query = os.path.join(toppath, 'timingfiles', '*.csv')
        files = glob.glob(query)
        if not files:
            print('\nSubject runs assigned, but no runs completed yet. Closing...')
        else:
            print('\nSubject runs already assigned, and the following runs have been completed... ')
            [print(os.path.basename(x)) for x in glob.glob(query)]
    else:
        print('\nSubject directory not yet created. I will make it for you...')
        os.mkdir(toppath)
        os.mkdir(os.path.join('data', f'subj{str(SID).zfill(3)}', 'runfiles'))
        os.mkdir(os.path.join('data', f'subj{str(SID).zfill(3)}','matfiles'))
        os.mkdir(os.path.join('data', f'subj{str(SID).zfill(3)}','timingfiles'))

        print('\nWriting run files...')
        train = pd.read_csv('train.csv')
        test = pd.read_csv('test.csv')
        count = 1
        for i in range(12):
            run = np.array([0, 0, 1, 2, 3, 4])
            np.random.shuffle(run)
            train = train.sample(frac=1, random_state=int(time.time())).reset_index(drop=True)
            for j in range(len(run)):
                if run[j] == 0:
                    curr = test.copy()
                    cond = 'test'
                else:
                    cond = 'train'
                    if run[j] == 1:
                        curr = train[:50].copy()
                    elif run[j] == 2:
                        curr = train[50:100].copy()
                    elif run[j] == 3:
                        curr = train[100:150].copy()
                    elif run[j] == 4:
                        curr = train[150:].copy()
                outname = os.path.join(toppath, 'runfiles', f'run{str(count).zfill(3)}_{cond}.csv')
                curr.to_csv(outname, header=False, index=False, columns=['video_name'])
                count += 1
        print('\nRuns assigned. Closing...')

def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('sid', type=str, help='id of the subject')
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    args = getArgs()
    get_past_runs(args.sid)
