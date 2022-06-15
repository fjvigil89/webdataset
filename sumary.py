from tqdm.notebook import tqdm

import torchvision.transforms as T

import webdataset as wds
from itertools import islice
from pathlib import Path
import braceexpand

shards = "webdataset.tar"  # defined using braceexpand format as used by webdataset
encoded_output = Path("encoded_data")  # where we will save our encoded data

VQGAN_REPO, VQGAN_COMMIT_ID = (
    "dalle-mini/vqgan_imagenet_f16_16384",
    "85eb5d3b51a1c62a0cc8f4ccdee9882c0d0bd384",
)

# # good defaults for a TPU v3-8
# batch_size = 128  # Per device
# num_workers = 8  # For parallel processing
# total_bs = batch_size * jax.device_count()  # You can use a smaller size while testing
# save_frequency = 128  # Number of batches to create a new file (180MB for f16 and 720MB for f8 per file)

shards = list(
    braceexpand.braceexpand(shards)
)

ds = (
    wds.WebDataset(shards, handler=wds.warn_and_continue)
    .decode("rgb", handler=wds.warn_and_continue)
    .to_tuple("png", "json")  # assumes image is in `jpg` and caption in `txt`
    #.batched(total_bs)  # load in batch per worker (faster)
)