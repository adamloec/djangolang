from django.shortcuts import render

from rest_framework import APIView
from rest_framework.response import Response

from hf.llm import LLM

# Create your views here.

class ModelView(APIView):
    
    def post(self, request):
