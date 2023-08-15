import os
import shutil
import argparse
import random

def split_train_test(input_dir, train_dir, test_dir, split_ratio=0.7):
    # List all video files
    files = [f for f in os.listdir(input_dir) if f.endswith('.mp4')]  # assuming videos are in .mp4 format
    random.shuffle(files)  # shuffle for randomness

    # Calculate split indexes
    train_count = int(split_ratio * len(files))
    train_files = files[:train_count]
    test_files = files[train_count:]

    # Ensure train and test directories exist
    if not os.path.exists(train_dir):
        os.mkdir(train_dir)
    if not os.path.exists(test_dir):
        os.mkdir(test_dir)

    # Move videos to train and test directories
    for f in train_files:
        shutil.move(os.path.join(input_dir, f), os.path.join(train_dir, f))
    for f in test_files:
        shutil.move(os.path.join(input_dir, f), os.path.join(test_dir, f))

    print(f"Moved {len(train_files)} files to {train_dir} and {len(test_files)} files to {test_dir}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Separate videos into train and test sets.')
    parser.add_argument('--input_dir', required=True, help='Input directory containing all videos')
    parser.add_argument('--train_dir', default='train', help='Directory to store training videos')
    parser.add_argument('--test_dir', default='test', help='Directory to store test videos')
    args = parser.parse_args()

    split_train_test(args.input_dir, args.train_dir, args.test_dir)

