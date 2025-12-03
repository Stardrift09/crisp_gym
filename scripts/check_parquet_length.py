import pandas as pd
import glob
# adjust path to your dataset
parquet_files = sorted(glob.glob("/home/shaotongchen/.cache/huggingface/lerobot/EfreetSultan/real_world_2/data/chunk-*/episode_*.parquet"))
fps = 20  # your FPS
durations = []

for pf in parquet_files:
    df = pd.read_parquet(pf)
    n_frames = len(df)
    duration_sec = n_frames / fps
    durations.append((pf, n_frames, duration_sec))

# Print results
for pf, n_frames, duration_sec in durations:
    print(f"{pf}: {n_frames} frames, {duration_sec:.2f} seconds")



