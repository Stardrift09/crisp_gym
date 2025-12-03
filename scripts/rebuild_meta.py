import json
from pathlib import Path
import pandas as pd
# Path to your local dataset parquet folder
parquet_folder = Path("/home/shaotongchen/.cache/huggingface/lerobot/EfreetSultan/real_world_2/data/chunk-000")
output_file = Path("/home/shaotongchen/.cache/huggingface/lerobot/EfreetSultan/real_world_2/meta/episodes.jsonl")

# Default task name if you don’t have one per episode
default_task = "SCENE2_pick_up_the_book_and_place_it_in_the_back_compartment_of_the_caddy_safe"

# Collect all parquet files
parquet_files = sorted(parquet_folder.glob("episode_*.parquet"))

with open(output_file, "w") as f:
    for pf in parquet_files:
        # Read parquet
        df = pd.read_parquet(pf)
        # Episode index from filename
        ep_index = int(pf.stem.split("_")[1])
        # Length = number of rows
        length = len(df)
        # Build json entry
        entry = {
            "episode_index": ep_index,
            "tasks": [default_task],
            "length": length
        }
        # Write as json line
        f.write(json.dumps(entry) + "\n")

print(f"Regenerated episodes.jsonl with {len(parquet_files)} episodes at {output_file}")
