"""Image series and section data containers.

These classes represent a series of sections (images or segmentations) to be
processed through the pynutil pipeline.  Users with custom segmentation types
can construct :class:`Section` and :class:`ImageSeries` objects directly,
providing their own ``numpy`` arrays instead of reading from disk.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional

import numpy as np


@dataclass
class Section:
    """A single section, identified by number and backed by an image.

    Either *image* or *path* must be provided.  When only *path* is given the
    image is loaded lazily the first time it is needed by the pipeline.

    Parameters
    ----------
    section_number:
        Numeric identifier that must match a section in the alignment JSON.
    filename:
        Display name used in :attr:`~pynutil.ExtractionResult.section_filenames`.
        Defaults to *path* when not set explicitly.
    image:
        Pre-loaded image array (2-D or 3-D ``numpy`` array).  Provide this
        when you have already loaded or generated the image data yourself.
    path:
        Path to the image file on disk.  The image is loaded on demand by the
        configured segmentation adapter when the section is processed.
    """

    section_number: int
    filename: str = ""
    image: Optional[np.ndarray] = field(default=None, repr=False)
    path: Optional[str] = None

    def get_image(self, adapter) -> np.ndarray:
        """Return the image array, loading from *path* if not pre-loaded.

        Parameters
        ----------
        adapter:
            A :class:`~pynutil.processing.adapters.segmentation.SegmentationAdapter`
            used to load the file when *image* is ``None``.
        """
        if self.image is not None:
            return self.image
        if self.path is not None:
            return adapter.load(self.path)
        raise ValueError(
            f"Section {self.section_number} has neither image data nor a file path."
        )


@dataclass
class ImageSeries:
    """An ordered collection of :class:`Section` objects.

    Construct this directly when you want to supply custom image data, or use
    :func:`~pynutil.read_segmentation_dir` / :func:`~pynutil.read_image_dir`
    to build one from a folder of image files.

    Parameters
    ----------
    sections:
        Dictionary mapping ``section_number`` to :class:`Section` objects.
    pixel_id:
        RGB value (or label) identifying the segmented class of interest.
        Set by :func:`~pynutil.read_segmentation_dir` and consumed by
        :func:`~pynutil.seg_to_coords`.
    segmentation_format:
        Name of the segmentation adapter to use (e.g. ``"binary"`` or
        ``"cellpose"``).  Set by :func:`~pynutil.read_segmentation_dir` and
        consumed by :func:`~pynutil.seg_to_coords`.
    """

    sections: Dict[int, Section] = field(default_factory=dict)
    pixel_id: object = field(default_factory=lambda: [0, 0, 0])
    segmentation_format: str = "binary"

    @property
    def filenames(self) -> List[str]:
        """Display filenames for all sections."""
        return [s.filename for s in self.sections.values()]
