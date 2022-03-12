from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from video.models import Video, Comment, Playlist
from video.serializer import VideoSerializer, CommentSerializer, PlaylistSerializer
from rest_framework.filters import SearchFilter



class VideoListCreateAPIView(ListCreateAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends = [SearchFilter]
    search_fields = ['__all__']

class CommentListCreateAPIView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class PlaylistListCreateAPIView(ListCreateAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    filter_backends = [SearchFilter]
    search_fields = ['__all__']

class VideoRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title','id']

class CommentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title','id']

class PlaylistRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title','id']