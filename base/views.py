from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

ar=[{"name":"waga"},{"name":"baga"}]

@api_view(['GET'])
def index(req):
    return Response({'msg':'hello'})


@api_view(['GET'])
def test_data(req):
    return Response(ar)