from django.contrib import admin
from addcourse.models import Course
from django.utils.html import format_html

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 50px;" />'.format(object.content.url))

    thumbnail.short_description = 'About content'
    list_display = ('course_id','thumbnail','subject')
    list_display_links = ('course_id','thumbnail','subject')

admin.site.register(Course, CourseAdmin)