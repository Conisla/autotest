from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from api.models import Jeu

class JeuAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.jeu = Jeu.objects.create(id_jeu='1', name='Monopoly')

    def test_get_jeu_list(self):
        url = reverse('Jeu-list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Vérifie si un seul jeu est renvoyé
        self.assertEqual(response.data[0]['id_jeu'], self.jeu.id_jeu)
        self.assertEqual(response.data[0]['name'], self.jeu.name)

    def test_create_jeu(self):
        url = reverse('Jeu-list')
        data = {'id_jeu': '2', 'name': 'Chess'}
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Jeu.objects.count(), 2)

    def test_get_jeu_detail(self):
        url = reverse('Jeu-detail', args=[self.jeu.id_jeu])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['id_jeu'], self.jeu.id_jeu)
        self.assertEqual(response.data['name'], self.jeu.name)

    def test_update_jeu(self):
        # url pour l'update '/api/jeu/<id_jeu>'
        url = reverse('Jeu-detail', args=[self.jeu.id_jeu])
        
        # data à envoyer pour mise a jour 
        data = {'id_jeu': self.jeu.id_jeu ,'name': 'New Name'}
        
        # Envoie de data avec requête HTTP méthode PUT à l'url
        response = self.client.put(url, data, format='json')

        # Test si Status de la requête == HTTP_200
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test si name de jeu<id_jeu> a été update
        self.assertEqual(Jeu.objects.get(id_jeu=self.jeu.id_jeu).name, 'New Name')

    def test_delete_jeu(self):
        url = reverse('Jeu-detail', args=[self.jeu.id_jeu])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Jeu.objects.count(), 0)
