from django.test import TestCase
from django.urls import reverse

from faker import Faker

from lettings.models import Letting, Address


class LettingIndexPageTest(TestCase):
    """Test that index page returns 200"""
    def test_index_page(self):
        response = self.client.get(reverse('lettings:index'))
        self.assertEqual(response.status_code, 200)

    # test that in content html the title is correct
    def test_title_letting_index_page_is_correct(self):
        response = self.client.get(reverse('lettings:index'))
        self.assertContains(response, "Lettings", status_code=200)


class LettingListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create fafe data for Address
        cls.fake = Faker()
        cls.address = Address.objects.create(
            number=cls.fake.building_number(),
            street=cls.fake.street_name(),
            city=cls.fake.city(),
            state=cls.fake.name(),
            zip_code=cls.fake.postcode(),
        )
        cls.letting = Letting.objects.create(
            title=cls.fake.name(),
            address=cls.address
        )

    def test_letting_creation(self):
        letting = Letting.objects.get(id=self.letting.id)
        self.assertEqual(self.letting.title, letting.title)

    # test that detail page returns a 200 if the item exists
    def test_detail_page_returns_200(self):
        letting_id = self.letting.id
        response = self.client.get(reverse('lettings:letting', args=(letting_id,)))
        self.assertEqual(response.status_code, 200)

    # test that detail page returns a 404 if the item does not exist
    def test_detail_page_returns_404(self):
        letting_id = self.letting.id + 1
        response = self.client.get(reverse('lettings:letting', args=(letting_id,)))
        self.assertEqual(response.status_code, 404)

    # test that in content html the title is correct
    def test_title_profile_page_is_correct(self):
        letting_id = self.letting.id
        title = self.letting.title
        response = self.client.get(reverse('lettings:letting', args=(letting_id,)))
        self.assertContains(response, title, status_code=200)