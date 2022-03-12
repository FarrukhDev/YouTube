from rest_framework.serializers import ModelSerializer
from video.models import Video, Playlist, Comment

class VideoSerializer(ModelSerializer):
    class Meta:
        model = Video
        fields = ['title','description','photo','video','comments']
class PlaylistSerializer(ModelSerializer):
    class Meta:
        model = Playlist
        fields = ['name','video']
class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = ['text','user']