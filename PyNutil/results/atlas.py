from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Tuple

import numpy as np
import pandas as pd


@dataclass
class AtlasData:
    """Custom-atlas stand-in that mirrors the BrainGlobeAtlas interface."""

    annotation: np.ndarray
    hemispheres: Optional[np.ndarray]
    labels: pd.DataFrame
    resolution: Optional[Tuple[float, ...]] = None
