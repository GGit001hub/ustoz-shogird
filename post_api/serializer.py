from post.models import Post
from rest_framework.serializers import ModelSerializer
from rest_framework.serializers import ModelSerializer
from r_account.models import CustomUser



class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ['drift','name','age','address','technology','jobs','price','application_time','phone','photo','title','author']



class UserSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username','email']



