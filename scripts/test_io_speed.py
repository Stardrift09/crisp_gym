import numpy as np
import time
from pathlib import Path

output_dir = Path("/tmp/test_io")
output_dir.mkdir(exist_ok=True)
num_files = 100
img_size = (1024, 1024, 3)  # 1MP image
images = [np.random.randint(0, 255, img_size, dtype=np.uint8) for _ in range(num_files)]

start = time.time()
for i, img in enumerate(images):
    np.save(output_dir / f"img_{i}.npy", img)  # writing as raw binary .npy
end = time.time()

total_bytes = num_files * np.prod(img_size)
total_mb = total_bytes / (1024**2)
speed = total_mb / (end - start)
print(f"Write speed: {speed:.2f} MB/s")