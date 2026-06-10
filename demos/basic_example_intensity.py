"""Sometimes you may want to measure the intensity of input images.
To do this we use image_to_coords instead of seg_to_coords.
"""
from pathlib import Path

from brainglobe_atlasapi import BrainGlobeAtlas
import pynutil as pnt

# Configuration
repo_root = Path(__file__).resolve().parents[1]
image_folder = repo_root / "tests/test_data/image_intensity/images"
alignment_json = repo_root / "tests/test_data/image_intensity/alignment.json"
output_folder = repo_root / "test_result/intensity_measurement"

# Load atlas and alignment
atlas = BrainGlobeAtlas("allen_mouse_25um")
alignment = pnt.read_alignment(alignment_json)

# Extract intensity data
images = pnt.read_image_dir(image_folder)
coords = pnt.image_to_coords(images, alignment, atlas)

# Quantify by atlas region
label_df = pnt.quantify_coords(coords, atlas)

# Save results
pnt.save_analysis(
    output_folder,
    coords,
    atlas,
    label_df=label_df,
)
