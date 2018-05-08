from django.core import serializers
import json

def serialize_for_json(obj):
    serialized_data = serializers.serialize('json', [obj])
    struct = json.loads(serialized_data)
    return json.dumps(struct[0])
