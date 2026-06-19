"""Produce a per-section quantification CSV for every section.

The functional API only returns whole-series tables. To get correct
per-section numbers (including region areas / area_fraction, which are summed
away in the combined result), run the pipeline one section at a time. Use
``read_segmentation`` to load a single file into a one-section ImageSeries.
"""
from pathlib import Path

from brainglobe_atlasapi import BrainGlobeAtlas
import PyNutil as pnt

# Configuration
repo_root = Path(__file__).resolve().parents[1]
segmentation_folder = repo_root / "tests/test_data/nonlinear_allen_mouse/segmentations"
alignment_json = repo_root / "tests/test_data/nonlinear_allen_mouse/alignment.json"
colour = [0, 0, 0]
output_folder = repo_root / "test_result/per_section_example"

# Load atlas and alignment once.
atlas = BrainGlobeAtlas("allen_mouse_25um")
alignment = pnt.read_alignment(alignment_json)

# Process one section at a time.
for path in sorted(segmentation_folder.glob("*.png")):
    seg = pnt.read_segmentation(path, pixel_id=colour, segmentation_format="binary")
    coords = pnt.seg_to_coords(seg, alignment, atlas, object_cutoff=0)
    label_df = pnt.quantify_coords(coords, atlas)

    # Save each section to its own folder (save_analysis uses fixed filenames).
    section_number = next(iter(seg.sections))
    pnt.save_analysis(
        output_folder / f"section_{section_number:03d}",
        coords,
        atlas,
        label_df=label_df,
    )
