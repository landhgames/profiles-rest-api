from rest_framework import serializers


from  . import models

class HelloSerializer(serializers.Serializer):

    name = serializers.CharField(max_length=10)


class UserProfileSerializer(serializers.ModelSerializer):
    """Profile serializer"""
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validate_data):
        """Create and return new user"""
        user = models.UserProfile(
            email= validate_data['email'],
            name= validate_data['name'],
        )

        user.set_password(validate_data['password'])
        user.save()

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializer for profile feed items"""
   
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}

    # def create(self, validate_data):
    #     """Create new profile"""
    #     profile = models.ProfileFeedItem(
    #         user_profile = validate_data["user_profile"]
    #         # status_text = validate_data["status_text"]                        
    #     )

    #     profile.save()