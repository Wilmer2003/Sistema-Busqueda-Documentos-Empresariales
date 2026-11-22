from app.config.settings import settings

from elasticsearch import Elasticsearch

es_client = Elasticsearch(settings.elasticsearch_url)