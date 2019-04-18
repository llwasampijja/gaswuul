from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, CurrentUserDefault
from accounts.serializers import UserSerializer
from redflag.models import Redflag


class RedflagSerializer(ModelSerializer):
    class Meta:
        model = Redflag
        fields = ('title', 'comment', 'date', 'status',
                  'image', 'video', 'createdby', 'location')
