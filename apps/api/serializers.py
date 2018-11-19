from rest_framework import serializers

from apps.course.models import Reading, Question, Section


# class SectionSerializer()


class ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reading
        fields = ('heading', 'body', 'marked', 'obj_type', 'section', 'id')


class ReadingUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reading
        fields = ('marked', )


class QuestionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('marked',)


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('heading', 'body', 'marked', 'obj_type', 'section')
