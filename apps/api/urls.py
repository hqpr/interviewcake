from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from .views import ReadingViewSet, UpdateReadingCourseView, UpdateQuestionCourseView

urlpatterns = [
    url(r'^courses/readings/$', ReadingViewSet.as_view({'get': 'list'}), name='courses'),
    url(r'^courses/r/(?P<pk>[-\w]+)/$', csrf_exempt(UpdateReadingCourseView.as_view()), name='update_reading'),
    url(r'^courses/q/(?P<pk>[-\w]+)/$', csrf_exempt(UpdateQuestionCourseView.as_view()), name='update_question'),
]
