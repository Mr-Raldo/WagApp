from rest_framework.serializers import ModelSerializer
from . models import QuestionnairePage


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = QuestionnairePage
        fields ='__all__'