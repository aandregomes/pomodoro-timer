def test_request_criar_nova_tarefa(client):
    resp = client.post('/api/tasks', {
        "description": "Criando task de teste"
    }, content_type="application/json")
    assert resp.status_code == 201


def test_response_criar_nova_tarefa(client):
    resp = client.post('/api/tasks', {
        "description": "Criando task de teste"
    }, content_type="application/json")
    assert "uid" in resp.data
    assert "created_at" in resp.data
    assert resp.data["description"] == "Criando task de teste"
