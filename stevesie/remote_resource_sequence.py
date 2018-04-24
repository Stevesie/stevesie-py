from abc import ABC, abstractmethod

from stevesie.remote_resource import RemoteResource


class RemoteResourceSequence(RemoteResource):

    @property
    def collection_type(self):
        return None

    def hydrate(self, obj):
        if self.collection_type:
            cls = self.collection_type
            return [cls().hydrate(o) for o in obj]
        else:
            return super(RemoteResourceSequence, self).hydrate(obj)

    def parse_api_response(self, api_json):
        return api_json['items']
