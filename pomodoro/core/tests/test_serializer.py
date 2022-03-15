from pomodoro.core.serializers import TaskSerializer


def test_task_serializer():
    task = {
        "uid": "f560489a-bc57-4f55-b236-c30af43b3b01",
        "description": "Task teste",
        "created_at": "2022-03-14T20:55:00"
    }
    serializer = TaskSerializer(data=task)
    assert serializer.initial_data == task
    assert "uid" in set(serializer.fields.keys())
    assert "description" in set(serializer.fields.keys())
    assert "created_at" in set(serializer.fields.keys())
