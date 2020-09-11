from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from .models import Blog


@registry.register_document
class blogDocument(Document):
    class Index:
        # Name of the Elasticsearch index
        name = 'blogs'
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0}

    class Django:
        model = Blog # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'Bid',
            'Author_name',
            'Blog_title',
            'Blog_slug',
            'Blog_category',
            'Blog_content',
            'Blog_time',
            'Blog_image',
        ]