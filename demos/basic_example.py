from pathlib import Path

from brainglobe_atlasapi import BrainGlobeAtlas
import pynutil as pnt

# Configuration
repo_root = Path(__file__).resolve().parents[1]
segmentation_folder = repo_root / "tests/test_data/nonlinear_allen_mouse/segmentations"
alignment_json = repo_root / "tests/test_data/nonlinear_allen_mouse/alignment.json"
colour = [0, 0, 0]
output_folder = repo_root / "test_result/hemi_test_bg6_damage_18_03_2026"

# Load atlas (BrainGlobe) and alignment
atlas = BrainGlobeAtlas("allen_mouse_25um")
alignment = pnt.read_alignment(alignment_json)

# Extract coordinates from segmentations
segmentations = pnt.read_segmentation_dir(
    segmentation_folder, pixel_id=colour, segmentation_format="binary"
)
coords = pnt.seg_to_coords(segmentations, alignment, atlas, object_cutoff=0)

# Quantify by atlas region
label_df = pnt.quantify_coords(coords, atlas)
# Optionally generate a 3D heatmap
pnt.interpolate_volume(image_series=segmentations, registration=alignment, atlas=atlas)
# Save results
pnt.save_analysis(
    output_folder,
    coords,
    atlas,
    label_df=label_df,
)
