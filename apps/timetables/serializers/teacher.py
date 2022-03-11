from rest_framework import serializers

from apps.timetables.models.teacher import Teacher


class TeacherSerializer(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = "__all__"
