from PyNutil.image_series import ImageSeries, Section


def test_image_series_stores_sections_by_number():
    section = Section(section_number=2, filename="section_2.png")

    image_series = ImageSeries(sections={2: section})

    assert image_series.sections == {2: section}
    assert image_series.filenames == ["section_2.png"]
