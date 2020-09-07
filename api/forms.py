from django import forms

from api.models import Scraper


class CreateScrapper(forms.ModelForm):
    """Create endpoint."""

    class Meta:
        # write the name of models for which the form is made
        model = Scraper

        # Custom fields
        fields = ["currency", "frequency"]

    currency = forms.CharField(min_length=1, max_length=50, required=True)
    frequency = forms.IntegerField(required=True)
    value = forms.IntegerField(required=False)

    def clean_currency(self):
        currency = self.cleaned_data['currency']
        scraper_exists = Scraper.objects.filter(currency=currency).exists()
        if scraper_exists:
            raise forms.ValidationError('The scraper already exists.')
        return currency

    def save(self):
        """Create Scraper from data."""
        scraper = Scraper(currency=self.cleaned_data['currency'], frequency=self.cleaned_data['frequency'])
        if self.cleaned_data['value']:
            scraper.value = self.cleaned_data['value']
        scraper.save()
        return scraper


class UpdateScrapper(forms.ModelForm):
    """Update endpoint."""

    class Meta:
        # write the name of models for which the form is made
        model = Scraper

        # Custom fields
        fields = ["id", "frequency"]

    id = forms.IntegerField(required=True)
    frequency = forms.IntegerField(required=True)
    value = forms.IntegerField(required=False)

    def clean_id(self):
        id_exists = Scraper.objects.filter(id=self.cleaned_data['id']).exists()
        if not id_exists:
            raise forms.ValidationError('The Id is not found.')
        return self.cleaned_data['id']

    def save(self):
        """Updated Scraper from data."""
        scraper = Scraper.objects.filter(id=self.cleaned_data['id']).get()
        scraper.frequency = self.cleaned_data['frequency']
        if self.cleaned_data['value']:
            scraper.value = self.cleaned_data['value']
        scraper.save()
        return scraper

class DeleteScrapper(forms.ModelForm):
    """Update endpoint."""

    class Meta:
        # write the name of models for which the form is made
        model = Scraper

        # Custom fields
        fields = ["id"]

    id = forms.IntegerField(required=True)

    def clean_id(self):
        id_exists = Scraper.objects.filter(id=self.cleaned_data['id']).exists()
        if not id_exists:
            raise forms.ValidationError('The scraper was not found.')
        return self.cleaned_data['id']

    def delete(self):
        """Delete Scraper from data."""
        scraper = Scraper.objects.filter(id=self.cleaned_data['id']).get()
        scraper.delete()
        return scraper