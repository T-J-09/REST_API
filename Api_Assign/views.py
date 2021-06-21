from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from Api_Assign.models import Movie
from Api_Assign.seralizers import MoviesSeralizer
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET','PUT','DELETE'])
def details(request, pk):
    try:
        api = Movie.objects.get(pk=pk)
    except Movie.DoesNotExist:
        return JsonResponse({'message':'Content not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        slizer = MoviesSeralizer(api)
        return JsonResponse(slizer.data)

    elif request.method == 'PUT':
        adata = JSONParser().parse(request)
        slizer = MoviesSeralizer(api, data=adata)
        if slizer.is_valid():
            slizer.save()
            return JsonResponse(slizer.data)
        return JsonResponse(slizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':  #1 record deletions
        api.delete()
        return JsonResponse({'message': 'Record is deleted successfully!!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST','DELETE'])
def summary(request):
    if request.method == 'GET': #to find all data by title
        api = Movie.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            api = api.filter(title__icontain=title)

        slizer = MoviesSeralizer(api, many=True)
        return JsonResponse(slizer.data, safe=False)

    elif request.method == 'POST':
        a_data = JSONParser().parse(request)
        slizer = MoviesSeralizer(data=a_data)
        if slizer.is_valid():
            slizer.save()
            return JsonResponse(slizer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(slizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Movie.objects.all().delete()
        return JsonResponse({'message': '{} records are deleted successfully!'.format(count[0])},
                            status=status.HTTP_204_NO_CONTENT)


