import unittest

from unittest import mock

from wkcp.download import handle as download_handle
from wkcp.download import extract_image_links


class TestDownload(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.args = mock.Mock()
        self.args.file = ["tests/251226-the-state-of-python-2025-trends-and-survey-insights--the-py-charm-blog.md"]
        with open(self.args.file[0], 'r') as fp:
            self.filelines = fp.readlines()

    def test_image_links(self):
        ret1, ret2 = extract_image_links(self.filelines)
        self.assertEqual(ret1, [
            'https://blog.jetbrains.com/wp-content/uploads/2025/08/Blog-Featured-1280x720-1-2.png',
            'https://blog.jetbrains.com/wp-content/uploads/2025/08/image-14.png',
            'https://blog.jetbrains.com/wp-content/uploads/2025/08/image-15.png',
            'https://blog.jetbrains.com/wp-content/uploads/2025/08/image-16.png',
            'https://blog.jetbrains.com/wp-content/uploads/2025/08/image-17.png',
            'https://blog.jetbrains.com/wp-content/uploads/2025/08/image-18.png',
            'https://blog.jetbrains.com/wp-content/uploads/2025/08/image-19.png',
            'https://blog.jetbrains.com/wp-content/uploads/2025/08/image-20.png',
            'https://blog.jetbrains.com/wp-content/uploads/2025/08/image-21.png',
            'https://blog.jetbrains.com/wp-content/uploads/2025/08/image-22.png',
            'https://blog.jetbrains.com/wp-content/uploads/2025/08/image-23.png',
            'https://blog.jetbrains.com/wp-content/uploads/2024/11/michael-kennedy.jpg',
            'https://admin.blog.jetbrains.com/wp-content/uploads/2023/12/PyCharm_Python-IDE-for-data-and-web_970x250-2x.png',
            'https://blog.jetbrains.com/wp-content/themes/jetbrains/assets/img/img-form.svg',
            'https://blog.jetbrains.com/wp-content/uploads/2025/10/PC-social-BlogFeatured-1280x720-1-20.png',
            'https://blog.jetbrains.com/wp-content/uploads/2025/10/Blog_1280x720-1.png',
            'https://blog.jetbrains.com/wp-content/uploads/2025/10/PC-social-BlogFeatured-1280x720-1-8.png',
            'https://blog.jetbrains.com/wp-content/uploads/2025/09/PC-social-BlogFeatured-1280x720-2x-8.png'
        ])
        self.assertEqual(ret2, [16, 30, 44, 54, 76, 116, 122, 138, 165, 177,
                                189, 276, 284, 288, 290, 294, 298, 302])


if __name__ == '__main__':
    unittest.main()
