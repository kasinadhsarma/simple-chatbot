import pytest
from flask import Flask, json
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"Friendly Chat Bot" in response.data

def test_chat_hi(client):
    response = client.post('/chat', json={'message': 'hi'})
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['response'] == "Hello! How can I help you today?"

def test_chat_how_are_you(client):
    response = client.post('/chat', json={'message': 'how are you'})
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['response'] == "I'm doing great, thank you for asking! How about you?"

def test_chat_bye(client):
    response = client.post('/chat', json={'message': 'bye'})
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['response'] == "Goodbye! Have a great day!"

def test_chat_default(client):
    response = client.post('/chat', json={'message': 'random message'})
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['response'] == "I'm here to chat and help! Feel free to ask me anything."
