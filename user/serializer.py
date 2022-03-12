from rest_framework.serializers import ModelSerializer
from user.models import Account


class UserSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = ['name','surname','user','birth_date','gender','bio','playlists']