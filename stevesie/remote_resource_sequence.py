from stevesie.remote_resource import RemoteResource
from stevesie.utils import api

PAGE_SIZE = 1000

class RemoteResourceSequence(RemoteResource):

    def __init__(self, *args, **kwargs):
        self._items = None
        super(RemoteResourceSequence, self).__init__(*args, **kwargs)

    def items(self):
        return self._items

    @property
    def collection_type(self):
        return None

    @property
    def collection_field(self):
        return None

    def fetch(self, limit=None):
        page_limit = min(limit, PAGE_SIZE) if limit is not None else PAGE_SIZE
        api_json = api.get(self.resource_url, {'limit': page_limit})
        obj = self.parse_api_response(api_json)
        initial_hydration = self.hydrate(obj, limit=limit)
        return initial_hydration

    def hydrate(self, obj, fetch_remote=True, limit=None):
        if self.collection_type:
            cls = self.collection_type
            self._items = [cls().hydrate(o, fetch_remote=fetch_remote) for o in obj]
            return self

        initial_hydration = super(RemoteResourceSequence, self).hydrate(obj)
        item_limit = min(limit, initial_hydration.total) if limit is not None else initial_hydration.total

        offset = 0
        while fetch_remote and self.collection_field and offset < item_limit - PAGE_SIZE:
            offset = offset + PAGE_SIZE

            params = initial_hydration.resource_params
            params['offset'] = offset

            pagination_json = api.get(initial_hydration.resource_url, params)
            pagination_obj = self.parse_api_response(pagination_json)

            new_hydration = super(RemoteResourceSequence, self).hydrate(pagination_obj)

            merged_collection = getattr(initial_hydration, self.collection_field) \
                + getattr(new_hydration, self.collection_field)

            merged_args = {}
            merged_args[self.collection_field] = merged_collection

            initial_hydration = initial_hydration._replace(**merged_args)

        return initial_hydration

    def parse_api_response(self, api_json):
        if self.collection_type:
            return api_json['items']
        return super(RemoteResourceSequence, self).parse_api_response(api_json)
