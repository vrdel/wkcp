import os
import unittest

from wkcp.utils import extract_imgpaths


class ImagePathExtract(unittest.TestCase):
    def test_extracts_dash_image_label(self):
        self.assertEqual(
            extract_imgpaths(["- image: image.jpg"], path=False),
            "image.jpg",
        )

    def test_extracts_dash_image(self):
        self.assertEqual(
            extract_imgpaths(["- image.jpg"], path=False),
            "image.jpg",
        )

    def test_extracts_plain_image(self):
        self.assertEqual(
            extract_imgpaths(["image.jpg"], path=False),
            "image.jpg",
        )

    def test_extracts_quoted_image_label(self):
        self.assertEqual(
            extract_imgpaths(['"- image: image.jpg"'], path=False),
            "image.jpg",
        )

    def test_preserves_existing_markdown_image_support(self):
        self.assertEqual(
            extract_imgpaths(["![alt](image.jpg)"], path=False),
            "image.jpg",
        )

    def test_prepends_current_directory_for_relative_paths(self):
        self.assertEqual(
            extract_imgpaths(["image.jpg"]),
            f"{os.getcwd()}/image.jpg",
        )

if __name__ == '__main__':
    unittest.main()
