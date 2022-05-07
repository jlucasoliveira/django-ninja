from rest_framework import serializers
import serpy
from polls import models


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Question
        fields = ["id", "question_text", "pub_date"]


class QuestionListSerializer(serpy.Serializer):
    id = serpy.IntField()
    question_text = serpy.StrField()
    pub_date = serpy.Field()
