import pandas as pd
import seaborn as sns
import os
import argparse

def parse_args():

    parser = argparse.ArgumentParser()

    parser.add_argument('--trials_dir_path',
                        type=str,
                        required=True)

    return parser.parse_args()


if __name__ == '__main__':

    args = parse_args()
    progresses = []

    for trial_dir in os.listdir(args.trials_dir_path):
        if trial_dir.startswith('trial'):
            log_file_path = '/'.join([args.trials_dir_path, trial_dir, 'progress.txt'])
            progresses.append(pd.read_csv(log_file_path, sep = "\t"))

    progresses_df = pd.concat(progresses)
    sns.set()
    sns.lineplot(x=progresses_df.Epoch, y=progresses_df.EpisodeDuration, ci='sd', estimator='mean')
    sns.lineplot(x=progresses_df.Epoch, y=progresses_df.MeanEpisodeDuration, ci='sd', estimator='mean')
    print('')