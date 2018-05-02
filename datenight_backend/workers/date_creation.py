from django.contrib.auth.models import User
from datenight_backend.models.image import Image
from datenight_backend.models.date import Date
from datenight_backend.models.user_date import UserDate
from datenight_backend.models.tag import Tag
from datenight_backend.models.date_tag import DateTag
from datenight_backend.models.featured_date import FeaturedDate
from datenight_backend.models.favorite_date import FavoriteDate
from datenight_backend.models.node import Node

def create_draft(user_id):
    current_user = User.objects.get(pk=user_id)
    draft = Date()
    draft.save()
    user_date = UserDate(user_date=draft, user=current_user)
    user_date.save()
    return draft.id

def get_date(date_id):
    date = Date.objects.get(pk=date_id)
    return date
