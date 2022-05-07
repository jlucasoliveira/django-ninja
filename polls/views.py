from typing import List
from ninja import Router
from rest_framework import mixins, routers, viewsets
from django.shortcuts import get_object_or_404, get_list_or_404
from polls import serializers
from polls.models import Choice, Question
from polls.schemas import QuestionList, ChoiceSchema


router = Router(tags=["Polls"])


@router.get("/", response=List[QuestionList])
def list_questions(request):
    qs = Question.objects.all()
    return qs

_router = routers.SimpleRouter()
class ListQuestions(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Question.objects.all()
    serializer_class = serializers.QuestionListSerializer
_router.register("list-test", ListQuestions)

@router.get("/{question_id}", response=QuestionList)
def retrieve_question(request, question_id: int):
    question = get_object_or_404(Question, id=question_id)
    return question


@router.get("/{question_id}/choices", response=List[ChoiceSchema])
def list_choices(request, question_id: int):
    choices = get_list_or_404(Choice, question_id=question_id)
    return choices


@router.get("/{question_id}/choices/{choice_id}", response=ChoiceSchema)
def retrieve_choice(request, question_id: int, choice_id: int):
    choice = get_object_or_404(Choice, id=choice_id, question_id=question_id)
    return choice
