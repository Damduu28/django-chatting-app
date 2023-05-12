from typing import Any
from django.forms import model_to_dict
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import Model
from .models import User

class LazyEncode(DjangoJSONEncoder):
    def default(self, o):
        if isinstance(o, User):
            return model_to_dict(o)
        return super().default(o)