from django.db import models


class OrderedDateTimeModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    order = models.IntegerField(default=0)

    class Meta:
        abstract = True


class CourseObject(OrderedDateTimeModel):

    NON_EDITABLE = 0
    EDITABLE = 1

    OBJECT_TYPE_CHOICES = (
        (NON_EDITABLE, 'Non editable'),
        (EDITABLE, 'Editable'),
    )

    heading = models.CharField(max_length=255)
    body = models.TextField()
    marked = models.BooleanField(default=False)
    obj_type = models.IntegerField(choices=OBJECT_TYPE_CHOICES, default=EDITABLE)
    section = models.ForeignKey('Section')

    class Meta:
        abstract = True
        ordering = ['order', ]

    def get_body(self):
        return self.body[:255]

    def get_edit_icon(self):
        if self.obj_type == self.NON_EDITABLE:
            return 'book'
        else:
            return 'pencil'

    def get_duplicate_icon(self):
        if self.obj_type == self.NON_EDITABLE:
            return 'list-alt'
        else:
            return 'duplicate'

    def get_mark(self):
        icon_class = 'margin-top-5 icon wb-clipboard bg-blue-600 white-color'
        if self.obj_type == self.EDITABLE:
            icon_class = icon_class + ' icon-circle glyphicon glyphicon-ok'
        if self.marked:
            icon_class = icon_class.replace('blue', 'green')
        return icon_class

    def __str__(self):
        return "%s" % self.heading


class Section(OrderedDateTimeModel):
    topic_title = models.CharField(max_length=255)

    def __str__(self):
        return "%s" % self.topic_title


class Reading(CourseObject):
    pass


class Question(CourseObject):
    pass

