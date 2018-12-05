import os
import re
import json

from typing import Sequence, GenericMeta
from datetime import datetime, date
import dateutil.parser

import inflection

from stevesie import resources
from stevesie.utils import api

DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S.%fZ'

class RemoteResource(object):

    _is_hydrated = False

    def set_hydrated(self):
        self._is_hydrated = True

    def hydrate(self, obj, fetch_remote=True):
        hydrate_args = {}
        for field_name in self._fields:
            field_type = self._field_types[field_name]
            api_field_name = inflection.camelize(field_name, uppercase_first_letter=False)
            field_value = obj.get(api_field_name, obj.get(field_name))

            if field_value is not None:
                if field_type == datetime:
                    field_value = dateutil.parser.parse(field_value)
                elif issubclass(field_type, RemoteResource):
                    field_value = field_type().hydrate(field_value, fetch_remote=fetch_remote)
                elif issubclass(field_type, Sequence) \
                    and issubclass(field_type.__class__, GenericMeta):
                    # TODO - serious debt, can't otherwise figure out the type of a typing.Sequence
                    sequence_class_string = str(field_type)

                    match = re.search(r'\[(.*)\]', sequence_class_string)
                    module_parts = match.group(1).split('.')

                    if len(module_parts) == 1: # referring to self using string type hack
                        class_name_match = re.search(r'\(\'(.*)\'\)', module_parts[0])
                        class_name = class_name_match.group(1)
                        module_name = inflection.underscore(class_name)
                    else:
                        module_name = module_parts[2]
                        class_name = module_parts[3]

                    mod = getattr(resources, module_name)
                    cls = getattr(mod, class_name)

                    field_value = [cls().hydrate(item, fetch_remote=fetch_remote) \
                        for item in field_value]

            hydrate_args[field_name] = field_value

        hydrated = self._replace(**hydrate_args)
        hydrated.set_hydrated()
        return hydrated

    def fetch(self):
        api_json = api.get(self.resource_url)
        obj = self.parse_api_response(api_json)
        return self.hydrate(obj)

    def destroy(self):
        api.delete(self.resource_url)

    def to_json(self, obj=None):
        if obj is None:
            obj = self

        def inner_json(inner_obj):
            if isinstance(inner_obj, list):
                return [self.to_json(o) for o in inner_obj]
            if isinstance(inner_obj, RemoteResource):
                return self.to_json(inner_obj)
            return inner_obj

        if hasattr(obj, 'collection_type') and obj.collection_type is not None:
            # little hack for implicit remote resource collection
            return [inner_json(value) for value in obj.items()]

        return {key: inner_json(value) for key, value in obj._asdict().items()}

    def save_to_file(self, local_filename):

        def serialize(obj):
            if isinstance(obj, (datetime, date)):
                return obj.strftime(DATETIME_FORMAT)
            raise TypeError('Cannot serialize %s' % type(obj))

        with open(os.path.expanduser(local_filename), 'w') as file:
            json.dump(self.to_json(), file, default=serialize)

    def load_from_file(self, local_filename):
        with open(os.path.expanduser(local_filename)) as file:
            obj = json.load(file)
        return self.hydrate(obj)

    def parse_api_response(self, api_json):
        return api_json['item']

    @property
    def resource_params(self):
        return {}

    @property
    def is_hydrated(self):
        return self._is_hydrated

    @property
    def resource_path(self):
        pass

    @property
    def resource_url(self):
        return api.BASE_URL_PATH + self.resource_path
