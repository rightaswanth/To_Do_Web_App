from rest_framework import serializers
from task.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id','title','description','start_date','end_date',
                  'current_status','priority','due_date','completion_date']
        read_only_fields = ['id', 'user_id', 'created_at', 'modified_at']

    def create(self, validated_data):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            validated_data['user_id'] = request.user
        if 'due_date' not in validated_data:
            validated_data['due_date'] = validated_data.get('end_date')
        return super().create(validated_data)