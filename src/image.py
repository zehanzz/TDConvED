import argparse
import os
from multiprocessing import Pool
import ffmpeg
from itertools import repeat
import shutil

g_sample = 25

def sample_videos(args):
    video_directory = args.video_directory
    output_dir = args.output_dir

    videos = [f for f in os.listdir(video_directory) if f.endswith('.mp4')]

    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    p = Pool(10)
    p.starmap(__sample, zip(videos, repeat(output_dir), repeat(video_directory)))
    
    p.close()
    p.join()

    # Delete directory that doesn't have g_sample images.    
    directories = [d for d in os.listdir(output_dir) if os.path.isdir(os.path.join(output_dir, d))]
    for d in directories:
        if len(os.listdir(os.path.join(output_dir, d))) != g_sample:
            shutil.rmtree(os.path.join(output_dir, d))

def __sample(video_file, output_dir, video_directory):
    video_path = os.path.join(video_directory, video_file)
    sample_image(video_path, os.path.splitext(video_file)[0], output_dir)
    os.remove(video_path)

def sample_image(video_path, video_id, output_dir):
    output_abs_dir = os.path.join(output_dir, video_id)
    if not os.path.exists(output_abs_dir):
        os.mkdir(output_abs_dir)

    probe = ffmpeg.probe(video_path)
    video_stream = next((stream for stream in probe['streams'] if stream['codec_type'] == 'video'), None)
    if video_stream is None:
        print(video_id, "error")
        return

    duration = float(video_stream['duration'])
    start = float(video_stream.get('start_time', 0))
    end = duration

    for i in range(0, g_sample):
        time = start + (end - start) * i / g_sample
        (
            ffmpeg
            .input(video_path, ss=time)
            .filter('scale', 256, 256)
            .output(os.path.join(output_abs_dir, video_id + f"_{i}.jpg"), vframes=1)
            .global_args('-loglevel', 'error')
            .global_args('-y')
            .run()
        )

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Sample images from already downloaded videos')
    parser.add_argument('--video_directory', required=True, help='directory of the downloaded videos')
    parser.add_argument('--output_dir', default='../data/msr_vtt/train', help='output directory for sampled images')
    args = parser.parse_args()
    assert os.path.exists(args.video_directory), "--video_directory doesn't exist."
    sample_videos(args)

