from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from .models import EventType



valid_payload_data = {
    "event_type": 1,
    "info": [
        {
            "test_info": 2342
        }
    ],
    "timestamp": "2021-03-14T15:26:59Z"
}

invalid_payload_data = {
    "event_type": None,
    "info": [
        {
            "test_info": 2342
        }
    ],
    "timestamp": "2021-03-14T15:26:59Z"
}

invalid_token_key = 'bbb7ed0c7ac8fad790f11acb7456394d5ce17179'


class EventCreationTests(APITestCase):

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user('test', 'test@test.com', 'test123')
        self.event_type = EventType.objects.create(name="New Year")
        self.token = Token.objects.create(user=self.user)

        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    def test_create_event__with_valid_data(self):
        response = self.client.post('/api/v1/events/', data=valid_payload_data, format='json',)
        self.assertEqual(response.status_code, 201)

    def test_create_event_with__invalid_data(self):
        response = self.client.post('/api/v1/events/', data=invalid_payload_data, format='json',)
        self.assertEqual(response.status_code, 400)

    def test_create_event_without_authentication(self):
        self.client.credentials() # unset any existing credentials
        response = self.client.post('/api/v1/events/', data=valid_payload_data, format='json',)
        self.assertEqual(response.status_code, 401)
    
    def test_create_event_with_invalid_token(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + invalid_token_key)
        response = self.client.post('/api/v1/events/', data=valid_payload_data, format='json',)
        self.assertEqual(response.status_code, 401)
