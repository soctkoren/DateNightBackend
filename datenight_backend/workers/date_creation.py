from django.contrib.auth.models import User
from datenight_backend.workers.serializer import serialize_for_json
from datenight_backend.models.image import Image
from datenight_backend.models.date import Date
from datenight_backend.models.user_date import UserDate
from datenight_backend.models.tag import Tag
from datenight_backend.models.date_tag import DateTag
from datenight_backend.models.featured_date import FeaturedDate
from datenight_backend.models.favorite_date import FavoriteDate
from datenight_backend.models.destination_node import DestinationNode
from datenight_backend.models.travel_node import TravelNode
from datenight_backend.models.node import Node
from datenight_backend.models.address import Address
from django.forms.models import model_to_dict
import json

def create_draft(user_id):
    current_user = User.objects.get(pk=user_id)
    draft = Date()
    draft.save()
    user_date = UserDate(user_date=draft, user=current_user)
    user_date.save()
    return draft.id

def get_date(date_id):
    return Date.objects.get(pk=date_id)

def get_user_id_from_date(date_id):
    return UserDate.objects.get(user_date_id=date_id)

# images
def create_date_hero_img(img, user_id, date_id):
    user = User.objects.get(pk=user_id)
    new_img = Image(img_url=img, user=user)
    new_img.save()
    date = Date.objects.get(pk=date_id)
    date.image = new_img
    date.save()
    data = serialize_for_json(new_img)
    payload = {'img': new_img.pk, 'data': data, 'date_id': date.pk}
    return payload

def create_node(date_id, order_number, node_type, is_hidden, address, user_id):
    date = Date.objects.get(pk=date_id)
    new_node = Node(order_number=order_number, is_hidden=is_hidden, date=date)
    new_node.save()
    new_address = Address(address=address, user_id=user_id)
    new_address.save()
    node_content = DestinationNode(description='', node=new_node, destination_address=new_address)
    node_content.save()

    payload = new_node.create_payload()
    payload['destination'] = node_content.create_payload()
    payload['node_type'] = node_type
    return payload
