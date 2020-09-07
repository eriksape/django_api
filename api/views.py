import json

from django.core import serializers
from django.http import JsonResponse
from django.views.generic import View

from api.forms import CreateScrapper, UpdateScrapper, DeleteScrapper
from api.models import Scraper


class ScraperAPI(View):
    def get(self, *args, **kwargs):
        data = json.loads(serializers.serialize('json', list(Scraper.objects.all())))
        return JsonResponse({
            'scrapers': [{'id': d['pk'], 'currency': d['fields']['currency'], 'frequency': d['fields']['frequency'],
                          'value': d['fields']['value'], 'created_at': d['fields']['created_at'],
                          'value_updated_at': d['fields']['value_updated_at']} for d in data]
        }, safe=False)

    def post(self, request, *args, **kwargs):
        if request.body:
            data = json.loads(request.body)
            form = CreateScrapper(data)
            if form.is_valid():
                scraper = form.save()
                return JsonResponse({
                    'id': scraper.id,
                    'created_at': scraper.created_at,
                    'currency': scraper.currency,
                    'frequency': scraper.frequency
                }, safe=False)

        return JsonResponse({
            'error': json.loads(form.errors.as_json())
        }, status=400, content_type='application/json')

    def put(self, request, *args, **kwargs):
        data = json.loads(request.body)
        form = UpdateScrapper(data)
        if form.is_valid():
            scraper = form.save()
            return JsonResponse({
                'msg': 'Scraper updated'
            }, safe=False)
        else:
            return JsonResponse({
                'error': json.loads(form.errors.as_json())
            }, status=400, content_type='application/json')

    def delete(self, request, *args, **kwargs):
        data = json.loads(request.body)
        form = DeleteScrapper(data)
        if form.is_valid():
            scraper = form.delete()
            return JsonResponse({
                'msg': 'Scraper deleted'
            }, safe=False)
        else:
            return JsonResponse({
                'error': json.loads(form.errors.as_json())
            }, status=400, content_type='application/json')
