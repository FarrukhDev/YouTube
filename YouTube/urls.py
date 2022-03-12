from django.contrib import admin
from django.urls import path
from user.views import UserListCreateAPIView
from video.views import *
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="YouTube API",
      default_version='v1',
      description="Clone of the most popular video service YouTube",
       terms_of_service="https://www.google.com/policies/terms/",
       contact=openapi.Contact(email="farruxbekergashaliev@gmail.com"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', UserListCreateAPIView.as_view(), name='userslist'),
    path('users/create', UserListCreateAPIView.as_view(), name='userscreate'),
    path('videosget/',VideoListCreateAPIView.as_view(),name = 'all_videos'),
    path('videocreate/',VideoListCreateAPIView.as_view(),name = 'create_videos'),
    path('getvideo/<int:pk>',VideoRetrieveUpdateDestroyAPIView.as_view(), name = 'get_video'),
    path('delvideo/<int:pk>',VideoRetrieveUpdateDestroyAPIView.as_view(), name = 'delete_video'),
    path('upvideo/<int:pk>',VideoRetrieveUpdateDestroyAPIView.as_view(), name = 'update_video'),
    path('playlistsget/',PlaylistListCreateAPIView.as_view(),name = 'all_playlists'),
    path('createplaylist/',PlaylistListCreateAPIView.as_view(),name = 'create_playlists'),
    path('getplaylist/<int:pk>', PlaylistRetrieveUpdateDestroyAPIView.as_view(), name='get_playlist'),
    path('delplaylist/<int:pk>', PlaylistRetrieveUpdateDestroyAPIView.as_view(), name='del_playlist'),
    path('upplaylist/<int:pk>', PlaylistRetrieveUpdateDestroyAPIView.as_view(), name='update_playlist'),
    path('commentsget/', CommentListCreateAPIView.as_view(), name='all_comments'),
    path('createcomment/', CommentListCreateAPIView.as_view(), name='create_comments'),
    path('getcomment/<int:pk>', CommentRetrieveUpdateDestroyAPIView.as_view(), name='get_comment'),
    path('delcomment/<int:pk>', CommentRetrieveUpdateDestroyAPIView.as_view(), name='del_comment'),
    path('upcomment/<int:pk>', CommentRetrieveUpdateDestroyAPIView.as_view(), name='update_comment'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name="swagger_doc"),

]
