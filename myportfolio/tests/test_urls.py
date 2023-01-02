from django.test import SimpleTestCase
from django.urls import reverse,resolve
from myportfolio.views import index,download_file,readmore
class TestUrls(SimpleTestCase):
    def test_list_url_is_resolved(self):
        url = reverse('download')
        self.assertEquals(resolve(url).func, download_file)