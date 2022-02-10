from django.test import TestCase
from django.urls import reverse


class OcLittingsSiteIndexPageTest(TestCase):
    """Test that index page returns 200"""
    def test_index_page(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)

    # test that in content html the title is correct
    def test_title_profile_index_page_is_correct(self):
        response = self.client.get(reverse('index'))
        self.assertContains(response, "Holiday Homes", status_code=200)
