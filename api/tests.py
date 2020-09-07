import json
from django.test import TestCase
from django.urls import reverse
class ScraperViewTests(TestCase):
    """View tests for Scraper"""

    def setUp(self):
        """Test case setup."""
        self.scraper = Scraper.objects.create(
            currency="Ethereum_check",
            frequency=1000
        )

    def test_200_in_get_scrapers(self):
        """Check for 200 status code to get Scrapers"""
        url = reverse('scrapers')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_200_in_post_scraper(self):
        """Check for 200 status code to post Scraper"""
        json_data = json.dumps({'currency': 'Bitcoin_new', 'frequency': 100})
        url = reverse('scrapers')
        response = self.client.post(url, json_data, 'json')
        self.assertEqual(response.status_code, 200)

    def test_200_put_scraper(self):
        """Check for 200 status code to post Scraper"""
        json_data = json.dumps({'currency': 'Bitcoin_new', 'frequency': 10, 'id': self.scraper.id})
        url = reverse('scrapers')
        response = self.client.put(url, json_data, 'json')
        self.assertEqual(response.status_code, 200)

    def test_200_in_delete_scraper(self):
        """Check for 200 status code to post Scraper"""
        json_data = json.dumps({'currency': 'Bitcoin_new', 'frequency': 10, 'id': self.scraper.id})
        url = reverse('scrapers')
        response = self.client.delete(url, json_data, 'json')
        self.assertEqual(response.status_code, 200)

    def test_400_in_post_scraper(self):
        """Check for 400 status code to post Scraper"""
        json_data = json.dumps({'currency': 'Bitcoin_new'})
        url = reverse('scrapers')
        response = self.client.post(url, json_data, 'json')
        self.assertEqual(response.status_code, 400)

    def test_400_put_scraper(self):
        """Check for 400 status code to post Scraper"""
        json_data = json.dumps({'currency': 'Bitcoin_new', 'frequency': 10})
        url = reverse('scrapers')
        response = self.client.put(url, json_data, 'json')
        self.assertEqual(response.status_code, 400)

    def test_400_in_delete_scraper(self):
        """Check for 400 status code to post Scraper"""
        json_data = json.dumps({'currency': 'Bitcoin_new', 'frequency': 10})
        url = reverse('scrapers')
        response = self.client.delete(url, json_data, 'json')
        self.assertEqual(response.status_code, 400)
