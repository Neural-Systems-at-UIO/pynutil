import unittest

import numpy as np

from PyNutil import VolumeResult, save_volumes


class TestSaveVolumes(unittest.TestCase):
    def test_save_volumes_rejects_missing_volume(self):
        volumes = VolumeResult(
            value=np.zeros((1, 1, 1), dtype=np.float32),
            frequency=None,
            damage=np.zeros((1, 1, 1), dtype=np.uint8),
        )

        with self.assertRaisesRegex(ValueError, "got None for frequency"):
            save_volumes(output_folder="/tmp/unused", volumes=volumes, atlas=None)


if __name__ == "__main__":
    unittest.main()
