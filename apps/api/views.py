from rest_framework import viewsets
from rest_framework.generics import UpdateAPIView

from apps.course.models import Reading, Question
from .serializers import ReadingSerializer, ReadingUpdateSerializer, QuestionUpdateSerializer


class ReadingViewSet(viewsets.ModelViewSet):
    queryset = Reading.objects.all().order_by('-order')
    serializer_class = ReadingSerializer


class UpdateReadingCourseView(UpdateAPIView):
    queryset = Reading.objects.all()
    serializer_class = ReadingUpdateSerializer

    def put(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.marked:
            obj.marked = False
        else:
            obj.marked = True
        obj.save()
        return self.update(request, *args, **kwargs)


class UpdateQuestionCourseView(UpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionUpdateSerializer

    def put(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.marked:
            obj.marked = False
        else:
            obj.marked = True
        obj.save()
        return self.update(request, *args, **kwargs)
