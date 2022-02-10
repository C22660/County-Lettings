from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from faker import Faker

from profiles.models import Profile


class ProfileIndexPageTest(TestCase):
    """Test that index page returns 200"""
    def test_index_page(self):
        response = self.client.get(reverse('profiles:index'))
        self.assertEqual(response.status_code, 200)

    # test that in content html the title is correct
    def test_title_profile_index_page_is_correct(self):
        response = self.client.get(reverse('profiles:index'))
        self.assertContains(response, "Profiles", status_code=200)


class ProfileListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Create fafe data for Address
        cls.fake = Faker()
        cls.user = User.objects.create(
            username=cls.fake.user_name(),
            first_name=cls.fake.first_name(),
            last_name=cls.fake.last_name(),
            email=cls.fake.email(),
        )
        cls.profile = Profile.objects.create(
            favorite_city=cls.fake.city(),
            user=cls.user
        )

    def test_profile_creation(self):
        profile = Profile.objects.get(id=self.profile.id)
        self.assertEqual(self.profile.favorite_city, profile.favorite_city)

    # test that detail page returns a 200 if the item exists
    def test_detail_page_returns_200(self):
        username = self.profile.user.username
        response = self.client.get(reverse('profiles:profile', args=(username,)))
        self.assertEqual(response.status_code, 200)

    # test that detail page returns a 404 if the item does not exist
    def test_detail_page_returns_404(self):
        fake_username = "JohnDoe"
        response = self.client.get(reverse('profiles:profile', args=(fake_username,)))
        self.assertEqual(response.status_code, 404)

    # test that in content html the title is correct
    def test_title_profile_page_is_correct(self):
        username = self.profile.user.username
        response = self.client.get(reverse('profiles:profile', args=(username,)))
        self.assertContains(response, username, status_code=200)
