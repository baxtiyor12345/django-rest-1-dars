from http.client import responses

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializer import *


@api_view(["GET", "POST"])
def movie_api(request):
    if request.method=="GET":
        movies=Movie.objects.all()
        serializer=MovieSerializer(movies, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    if request.method=="POST":
        serializer=MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)



@api_view(["GET", "POST"])
def actor_api(request):
    if request.method=="GET":
        actors=Actors.objects.all()
        serializer=ActorsSerializer(actors, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)
    if request.method=="POST":
        serializer=ActorsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.data, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET", "PUT", "PATCH", "DELETE"])
def movie_detail_view(request,slug):
    response = {"success": True}
    try:
        movie=Movie.objects.get(slug=slug)
    except Movie.DoesNotExist:
        response["error"]="bunday malumot yuq"
        return Response(data=response, status=status.HTTP_417_EXPECTATION_FAILED)
    if request.method=="GET":
        serializer=MovieSerializer(movie)
        response["data"]=serializer.data
        return Response(data=response, status=status.HTTP_200_OK)
    elif request.method=="PUT":
        serializer=MovieSerializer(movie,data=request.data)
        if serializer.is_valid(raise_exception=True):
           serializer.save()
           response["data"]=serializer.data
           return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method=="PATCH":
        serializer = MovieSerializer(movie, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            response["data"] = serializer.data
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == "DELETE":
        id=movie.pk
        movie.delete()
        # response["message"] = "Movie successfully deleted"
        return Response(data={"id":f"{id} o`chirildi"})

@api_view(["POST"])
def ism_api(request):
    ism=request.data["ism"]
    return Response(data={"ism": f"salom {ism}"})





