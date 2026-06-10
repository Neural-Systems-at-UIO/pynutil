from pathlib import Path

import cv2

segmentations = (
    Path(__file__).resolve().parents[1]
    / "tests"
    / "test_data"
    / "blank_test"
    / "segmentations"
)
for image in segmentations.glob("*"):
    im = cv2.imread(str(image))
    im[:] = 255
    cv2.imwrite(str(image), im)
