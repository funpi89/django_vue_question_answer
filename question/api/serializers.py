from rest_framework import serializers
from question.models import Question, Answer

class AnswerSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    user_has_voted = serializers.SerializerMethodField()
    question_slug = serializers.SerializerMethodField()

    class Meta:
        model = Answer
        exclude = ['question', 'voters', 'updated_at']

    def get_created_at(self, instance):
        return instance.created_at.strftime('%B %d, %Y')

    def get_likes_count(self, instance):
        return instance.voters.count()

    def get_user_has_voted(self, instance):
        request = self.context.get('request')
        return instance.voters.filter(pk=request.user.pk).exists()

    def get_question_slug(self, instance):
        return instance.question.slug

class QuestionSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    created_at = serializers.SerializerMethodField()
    slug = serializers.SlugField(read_only=True)
    answer_count = serializers.SerializerMethodField()
    user_has_answerd = serializers.SerializerMethodField()

    class Meta:
        model = Question
        exclude = ['updated_at']

    def get_created_at(self, instance):
        return instance.created_at.strftime('%B %d, %Y')

    def get_answer_count(self, instance):
        return instance.answers.count()

    def get_user_has_answerd(self, instance):
        request = self.context.get('request')
        return instance.answers.filter(author=request.user).exists()





