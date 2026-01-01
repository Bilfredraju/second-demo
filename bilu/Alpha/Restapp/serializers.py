from rest_framework.serializers import ModelSerializer
from.models import userpro

class userserializers(ModelSerializer):
    class Meta:
        model = userpro
        fields = '__all__'

    
