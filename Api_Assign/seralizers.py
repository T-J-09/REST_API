from rest_framework import serializers
from Api_Assign.models import Movie

class MoviesSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'id',
            'title',
            'url',
            'descrip')