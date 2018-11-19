from django.conf.urls import url

from .views import ReadingViewSet, UpdateReadingCourseView, UpdateQuestionCourseView

urlpatterns = [
    url(regex=r'^courses/readings/$', view=ReadingViewSet.as_view({'get': 'list'}), name='courses'),
    url(regex=r'^courses/r/(?P<pk>[-\w]+)/$', view=UpdateReadingCourseView.as_view(), name='update_reading'),
    url(regex=r'^courses/q/(?P<pk>[-\w]+)/$', view=UpdateQuestionCourseView.as_view(), name='update_question'),
]
