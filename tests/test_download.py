import unittest

from unittest import mock

from wkcp.download import DownloadHandle


class ImageLinksExtract(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.patcher1 = mock.patch('wkcp.download.DownloadHandle._download')
        _ = self.patcher1.start()
        self.patcher2 = mock.patch('wkcp.download.DownloadHandle._replace_with_local_links')
        _ = self.patcher2.start()

    def test(self):
        args = mock.Mock()
        args.file = ["tests/251226-the-state-of-python-2025-trends-and-survey-insights--the-py-charm-blog.md"]
        dh = DownloadHandle(args)

        self.assertEqual(dh.image_links, [
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
        self.assertEqual(dh.lines_with_images, [16, 30, 44, 54, 76, 116, 122,
                                                138, 165, 177, 189, 276, 284,
                                                288, 290, 294, 298, 302])

    def tearDown(self):
        self.patcher1.stop()
        self.patcher2.stop()


if __name__ == '__main__':
    unittest.main()
