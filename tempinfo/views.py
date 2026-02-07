from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import TempInfoCollect
from .serializers import TempInfoCollectSerializer
from skincare.response import success_response
from account.permissions import IsAdminRole
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination


# Create your views here.

class TempInfoListCreateAPIView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAdminRole()]
        return [AllowAny()] 

    @swagger_auto_schema(
        operation_description="List all TempInfo entries or create a new one",
        manual_parameters=[
            openapi.Parameter(
                'page',
                openapi.IN_QUERY,
                description="Page number",
                type=openapi.TYPE_INTEGER
            ),
            openapi.Parameter(
                'lean',
                openapi.IN_QUERY,
                description="Language code (default EN)",
                type=openapi.TYPE_STRING,
                default='EN'
            ),
        ],
        responses={
            200: TempInfoCollectSerializer(many=True),
            201: TempInfoCollectSerializer,
            400: "Validation Error"
        },
        tags=['Member']
    )
    def get(self, request):
        queryset = TempInfoCollect.objects.all().order_by('-id')

        paginator = PageNumberPagination()
        paginated_queryset = paginator.paginate_queryset(queryset, request)

        serializer = TempInfoCollectSerializer(paginated_queryset, many=True)

        return paginator.get_paginated_response({
            "success": True,
            "message": "TempInfo list retrieved successfully",
            "data": serializer.data
        })

    @swagger_auto_schema(
        operation_description="Create a new TempInfo entry",
        request_body=TempInfoCollectSerializer,
        manual_parameters=[
            openapi.Parameter(
                'lean',
                openapi.IN_QUERY,
                description="Language code for translation (default is 'EN')",
                type=openapi.TYPE_STRING,
                default='EN'
            ),
        ],
        responses={
            201: TempInfoCollectSerializer,
            400: "Validation Error"
        },
        tags=['Member']
    )
    def post(self, request):
        """Create a new TempInfo entry"""
        serializer = TempInfoCollectSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return success_response("TempInfo created successfully", serializer.data, status_code=status.HTTP_201_CREATED)



class TempInfoRetrieveUpdateDeleteAPIView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    def get_permissions(self):
        return [IsAdminRole()]

    def get_object(self, id):
        return get_object_or_404(TempInfoCollect, id=id)

    # ---------------- GET ----------------
    @swagger_auto_schema(
        operation_description="Retrieve a single TempInfo entry (Admin only)",
        responses={200: TempInfoCollectSerializer},
        tags=['Member']
    )
    def get(self, request, id):
        instance = self.get_object(id)
        serializer = TempInfoCollectSerializer(instance)
        return success_response(
            "TempInfo retrieved successfully",
            serializer.data
        )

    # ---------------- PATCH ----------------
    @swagger_auto_schema(
        operation_description="Update a TempInfo entry partially (Admin only)",
        request_body=TempInfoCollectSerializer,
        responses={200: TempInfoCollectSerializer},
        tags=['Member']
    )
    def patch(self, request, id):
        instance = self.get_object(id)
        serializer = TempInfoCollectSerializer(
            instance,
            data=request.data,
            partial=True
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return success_response(
            "TempInfo updated successfully",
            serializer.data
        )

    # ---------------- DELETE ----------------
    @swagger_auto_schema(
        operation_description="Delete a TempInfo entry (Admin only)",
        responses={204: "Deleted successfully"},
        tags=['Member']
    )
    def delete(self, request, id):
        instance = self.get_object(id)
        instance.delete()
        return success_response(
            "TempInfo deleted successfully",
            status_code=status.HTTP_204_NO_CONTENT
        )