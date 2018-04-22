import re

from abc import ABC, abstractmethod

from typing import Sequence, GenericMeta

import inflection
from datetime import datetime

import stevesie
from stevesie.utils import api

DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'

class RemoteResource(ABC):

    def __init__(self, id):
        self._id = id
        self._is_hydrated = False
        super(RemoteResource, self).__init__()

    def hydrate(self, obj=None):
        if obj is None:
            api_json = api.get(self.resource_url)
            obj = api_json['item']
        
        hydrate_args = {'id': self.id}

        for field_name in self._fields:
            field_type = self._field_types[field_name]
            api_field_name = inflection.camelize(field_name, uppercase_first_letter=False)
            field_value = obj.get(api_field_name)
            
            if field_value is not None:
                if field_type == datetime:
                    field_value = datetime.strptime(field_value, DATETIME_FORMAT)
                elif issubclass(field_type, RemoteResource):
                    field_value = field_type(field_value['id']).hydrate(field_value)
                elif issubclass(field_type, Sequence) and issubclass(field_type.__class__, GenericMeta):
                    # TODO - serious debt, can't otherwise figure out the type of a typing.Sequence
                    sequence_class_string = str(field_type)
                    
                    m = re.search('\[(.*)\]', sequence_class_string)
                    module_parts = m.group(1).split('.')
                    module_name = module_parts[1]
                    class_name = module_parts[2]

                    mod = getattr(stevesie, module_name)
                    cls = getattr(mod, class_name)

                    field_value = [cls(item['id']).hydrate(item) for item in field_value]

            hydrate_args[field_name] = field_value

        return self._replace(**hydrate_args)

    @property
    def id(self):
        return self._id

    @property
    def is_hydrated(self):
        return self._is_hydrated

    @property
    @abstractmethod
    def resource_path(self):
        pass

    @property
    def resource_url(self):
        return api.BASE_URL + self.resource_path
