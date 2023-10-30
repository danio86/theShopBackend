from django.contrib.auth.models import User
from .models import Property
from rest_framework import status
from rest_framework.test import APITestCase


class PropertyListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='dani', password='dani')

    def test_can_list_properties(self):
        dani = User.objects.get(username='dani')
        Property.objects.create(owner=dani, title='the loft', price=100000, size=127, num_rooms=4)
        response = self.client.get('/properties/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))


    def test_user_not_logged_in_cant_create_property(self):
        response = self.client.post('/properties/', {'title': 'a title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PropertyDetailViewTests(APITestCase):
    def setUp(self):
        adam = User.objects.create_user(username='dani', password='dani')
        brian = User.objects.create_user(username='brian', password='pass')
        Property.objects.create(
            owner=adam, title='the loft', price=100000, size=127, num_rooms=4
        )
        Property.objects.create(
            owner=brian, title='the house', price=100000, size=127, num_rooms=4
        )

    def test_can_retrieve_post_using_valid_id(self):
        response = self.client.get('/properties/1/')
        self.assertEqual(response.data['title'], 'the loft')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_post_using_invalid_id(self):
        response = self.client.get('/properties/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_user_can_update_own_property(self):
        self.client.login(username='dani', password='dani')
        response = self.client.put('/properties/1/', {'title': 'newTitle'})
        property = Property.objects.filter(pk=1).first()
        self.assertEqual(property.title, 'newTitle')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_user_cant_update_another_users_property(self):
        self.client.login(username='adam', password='pass')
        response = self.client.put('/properties/2/', {'title': 'a new title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)