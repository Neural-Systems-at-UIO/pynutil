from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Tuple

import numpy as np
import pandas as pd


@dataclass
class AtlasData:
    """Bundle of atlas volume, hemisphere map, and region labels."""

    volume: np.ndarray
    hemi_map: Optional[np.ndarray]
    labels: pd.DataFrame
    resolution: Optional[Tuple[float, ...]] = None
