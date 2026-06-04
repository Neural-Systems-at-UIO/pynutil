from pathlib import Path

import PyNutil as pnt

# PyNutil is a toolkit for quantifying neuroscientific data using brain atlases.
# This example uses a custom atlas (not BrainGlobe API).

repo_root = Path(__file__).resolve().parents[1]

# Load custom atlas
atlas = pnt.load_custom_atlas(
    atlas_path=(
        repo_root
        / "tests/test_data/allen_mouse_2017_atlas/annotation_25_reoriented_2017.nrrd"
    ),
    hemi_path=None,
    label_path=repo_root / "tests/test_data/allen_mouse_2017_atlas/allen2017_colours.csv",
)

# Load alignment
alignment = pnt.read_alignment(
    repo_root / "tests/test_data/nonlinear_allen_mouse/alignment.json"
)

# Extract coordinates
segmentations = pnt.read_segmentation_dir(
    repo_root / "tests/test_data/nonlinear_allen_mouse/segmentations",
    pixel_id=[0, 0, 0],
)
coords = pnt.seg_to_coords(segmentations, alignment, atlas, object_cutoff=0)

# Quantify and save
label_df = pnt.quantify_coords(coords, atlas)
pnt.save_analysis(
    repo_root / "test_result/2custom_atlas_hemi_test_24_03_2025",
    coords,
    atlas,
    label_df=label_df,
)
