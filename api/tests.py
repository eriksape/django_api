import json
from time import sleep

from django.test import TestCase
from django.urls import reverse

from api.forms import CreateScrapper, UpdateScrapper, DeleteScrapper
from api.models import Scraper


class ScraperModelTests(TestCase):
    """Model tests for Scraper"""

    def setUp(self):
        """Test case setup."""
        self.scraper = Scraper.objects.create(
            currency="Ethereum_check",
            frequency=1000
        )
        self.time_format = '%Y-%m-%d %H:%M:%s'

    def test_string_representation(self):
        """Inserts fields in the model."""
        scraper = Scraper(currency="Bitcoin_new", frequency=1000)
        self.assertEqual(scraper.__str__(), scraper.currency)

    def test_not_modify_value_updated_at_field(self):
        """Check if value_updated_at is not modified"""
        self.scraper.frequency = 100
        self.scraper.save()
        self.assertEqual(
            self.scraper.created_at.strftime(self.time_format), self.scraper.value_updated_at.strftime(self.time_format)
        )

    def test_modify_value_updated_at_field(self):
        """Check if value_updated_at is modified"""
        sleep(1)
        self.scraper.value = 100
        self.scraper.save()
        self.assertNotEqual(
            self.scraper.created_at.strftime(self.time_format), self.scraper.value_updated_at.strftime(self.time_format)
        )


class ScraperFormTests(TestCase):
    """Form tests for Scraper"""

    def setUp(self):
        """Test case setup."""
        self.scraper = Scraper.objects.create(
            currency="Ethereum_check",
            frequency=1000
        )

    def test_not_valid_data_for_new_instance(self):
        """Check if the form is invalid to storage in database"""
        form = CreateScrapper()
        self.assertFalse(form.is_valid())

    def test_valid_data_for_new_instance(self):
        """Check if the form is valid to storage in database"""
        form = CreateScrapper({'frequency': 1, 'currency': 'Bitcoin_new'})
        self.assertTrue(form.is_valid())

    def test_data_already_exists_for_new_instance(self):
        """Check if the form can't save with stored currency value"""
        form = CreateScrapper({'frequency': 1, 'currency': 'Ethereum_check'})
        self.assertFalse(form.is_valid())

    def test_not_valid_data_for_update_instance(self):
        """Check if the form is invalid to update in database"""
        form = UpdateScrapper()
        self.assertFalse(form.is_valid())

    def test_valid_data_for_update_instance(self):
        """Check if the form is valid to update in database"""
        form = UpdateScrapper({'id': self.scraper.id, 'frequency': 100})
        self.assertTrue(form.is_valid())

    def test_not_exists_id_for_update_instance(self):
        """Check if the id exists to update in database"""
        form = UpdateScrapper({'id': 2, 'frequency': 100})
        self.assertFalse(form.is_valid())

    def test_not_exists_id_for_delete_instance(self):
        """Check if cant delete in database"""
        form = DeleteScrapper({'id': 2})
        self.assertFalse(form.is_valid())

    def test_exists_id_for_delete_instance(self):
        """Check if can delete in database"""
        form = DeleteScrapper({'id': self.scraper.id})
        self.assertTrue(form.is_valid())


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
