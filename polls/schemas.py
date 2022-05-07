from ninja import ModelSchema
from polls import models


class QuestionList(ModelSchema):
    class Config:
        model = models.Question
        model_fields = ["id", "question_text", "pub_date"]


class ChoiceSchema(ModelSchema):
    class Config:
        model = models.Choice
        model_fields = ["id", "question", "choice_text", "votes"]
