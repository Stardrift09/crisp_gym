import pandas as pd
import json

dfs = []

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
# Loop from 0 to 10 (inclusive)
for i in range(209,210):
    # Construct the filename with zero-padded episode number
    filename = f"/home/shaotongchen/.cache/huggingface/LSY-lab/real_world_4/second_tset/data/chunk-000/episode_{i:06d}.parquet"


    # Read the Parquet file
    df = pd.read_parquet(filename)
    
    # Append to list
    dfs.append(df)

# Concatenate all DataFrames
df = pd.concat(dfs, ignore_index=True)

# Inspect columns
print(df.columns)

# tasks = {}
# with open("/home/shaotongchen/.cache/huggingface/lerobot/EfreetSultan/real_world_02/meta/tasks.jsonl") as f:
#     for line in f:
#         item = json.loads(line)
#         tasks[item['task_index']] = item['task']


# # Map task_index to task description
# df['task'] = df['task_index'].map(tasks)

# Check
print(df[['episode_index', 'timestamp', 'observation.state.joints']])