import unittest

from unittest import mock

from wkcp.download import DownloadHandle


class ImageLinksExtract(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.patcher1 = mock.patch('wkcp.download.DownloadHandle._download')
        _ = self.patcher1.start()
        self.patcher2 = mock.patch('wkcp.download.DownloadHandle._replace_with_local_links')
        _ = self.patcher2.start()
        args = mock.Mock()
        args.file = ["tests/251226-the-state-of-python-2025-trends-and-survey-insights--the-py-charm-blog.md"]
        self.dh = DownloadHandle(args)

    def test(self):
        self.assertEqual(self.dh.image_links, [
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
        self.assertEqual(len(self.dh.image_links), 18)
        self.assertEqual(self.dh.lines_with_images, [16, 30, 44, 54, 76, 116,
                                                     122, 138, 165, 177, 189,
                                                     276, 284, 288, 290, 294,
                                                     298, 302])

    def tearDown(self):
        self.patcher1.stop()
        self.patcher2.stop()


class mockHttpGet(mock.AsyncMock):
    async def __aenter__(self, *args, **kwargs):
        mock_obj = mock.AsyncMock()

        mock_obj.content = mock.AsyncMock()
        mock_obj.content.read.return_value = "image_content"

        return mock_obj

    async def __aexit__(self, *args, **kwargs):
        pass


class ReplaceImageLinksWithLocalImages(unittest.IsolatedAsyncioTestCase):
    def setUp(self):
        self.patcher1 = mock.patch('wkcp.download.build_image_filename')
        mock_imagefilename = self.patcher1.start()
        mock_imagefilename.side_effect = [f"image{i}.png" for i in range(1, 19)]

        self.patcher2 = mock.patch('wkcp.download.DownloadHandle._write_content_file')
        self.mock_writecontentfile = self.patcher2.start()

        self.patcher3 = mock.patch('wkcp.download.DownloadHandle._replace_with_local_links')
        self.mock_replacewithlocallinks = self.patcher3.start()

        self.patcher4 = mock.patch('wkcp.download.aiohttp.ClientSession.get')
        self.mock_httpclient = self.patcher4.start()
        self.mock_httpclient.side_effect = mockHttpGet

        args = mock.Mock()
        args.file = ["tests/251226-the-state-of-python-2025-trends-and-survey-insights--the-py-charm-blog.md"]
        _ = DownloadHandle(args)

    def test(self):
        self.assertTrue(self.mock_writecontentfile.called)
        self.assertEqual(self.mock_writecontentfile.call_args[0][0], 'image_content')
        self.assertEqual(self.mock_writecontentfile.call_args_list[17], mock.call('image_content', 'tests/image18.png'))
        self.assertEqual(self.mock_replacewithlocallinks.call_args[0][0]['https://blog.jetbrains.com/wp-content/uploads/2025/08/image-23.png'], 'image11.png')

    def tearDown(self):
        self.patcher1.stop()
        self.patcher2.stop()
        self.patcher3.stop()
        self.patcher4.stop()


if __name__ == '__main__':
    unittest.main()
