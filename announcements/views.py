from rest_framework.generics import *
from .models import Announcement, WorkRequest
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from .permissions import IsCaptain, IsProjectManager
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.db.models import Q

class AnnouncementListView(ListCreateAPIView):
    serializer_class = AnnouncementSerializer
    permission_classes = []

    def get_queryset(self):
        user = self.request.user
        if user.role == 'captain':
            return Announcement.objects.filter(Q(deleted_at__isnull=True) & Q(assigned_to=user) | Q(assigned_to__isnull=True))
        elif user.role == 'project_manager':
            return Announcement.objects.filter(deleted_at__isnull=True)

class AnnouncementDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer
    permission_classes = []





class WorkRequestListViewManager(ListCreateAPIView):
    permission_classes = [IsProjectManager]
    serializer_class = WorkRequestSerializer
    def get_queryset(self):
        return WorkRequest.objects.filter(deleted_at__isnull=True)


class WorkRequestListView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WorkRequestSerializerWithOutAnn
    def get_queryset(self):
        return WorkRequest.objects.filter(deleted_at__isnull=True)


class DeletedWorkRequestListView(ListAPIView):
    serializer_class = WorkRequestSerializer
    #permission_classes = [IsAuthenticated, IsAdmin]

    def get_queryset(self):
        return WorkRequest.objects.filter(deleted_at__isnull=False)


class MyWorkRequestListView(ListCreateAPIView):
    serializer_class = WorkRequestSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs['pk']
        return WorkRequest.objects.filter(requester=user_id, deleted_at__isnull=True)

class WorkRequestDetailView(RetrieveUpdateDestroyAPIView):
    queryset = WorkRequest.objects.all()
    serializer_class = WorkRequestSerializer
    #permission_classes = [IsAuthenticated, IsAdmin]

