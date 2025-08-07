from rest_framework import serializers
from .models import Autor

class AutorSerializers(serializers.ModelSerializer):
    class meta:
    model = Autorfield()