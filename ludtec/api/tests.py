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
        # url pour get la liste de tous les jeux 'api/jeu/'
        url = reverse('Jeu-list')

        # Envoie de la requete HTTP méthode get sur url
        response = self.client.get(url)
        
        #  Test si Status de la requête == HTTP_200_OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
        #  Test si un seul jeu est renvoyé
        self.assertEqual(len(response.data), 1)

        # Test si id_jeu du premier jeu correspond
        self.assertEqual(response.data[0]['id_jeu'], self.jeu.id_jeu)

        # Test si name du premier jeu correspond
        self.assertEqual(response.data[0]['name'], self.jeu.name)

    def test_create_jeu(self):
        # url pour le create 'api/jeu/'
        url = reverse('Jeu-list')
        
        # data à envoyer pour la création 
        data = {'id_jeu': '2', 'name': 'Chess'}

        # Envoie de data avec requête HTTP méthode POST à l'url
        response = self.client.post(url, data, format='json')

        #  Test si Status de la requête == HTTP_201_CREATED
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Test le nombre de jeu a augmenté
        self.assertEqual(Jeu.objects.count(), 2)

    def test_get_jeu_detail(self):
        # url pour get un jeu spécifique avec son id '/api/jeu/<id_jeu>'
        url = reverse('Jeu-detail', args=[self.jeu.id_jeu])

        # Envoie de la requête get sur url
        response = self.client.get(url)

        # Test si Status de la requête == HTTP_200_OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test si id_jeu créé correspond
        self.assertEqual(response.data['id_jeu'], self.jeu.id_jeu)

        # Test si name créé correspond
        self.assertEqual(response.data['name'], self.jeu.name)

    def test_update_jeu(self):
        # url pour l'update '/api/jeu/<id_jeu>'
        url = reverse('Jeu-detail', args=[self.jeu.id_jeu])
        
        # data à envoyer pour mise a jour 
        data = {'id_jeu': self.jeu.id_jeu ,'name': 'New Name'}
        
        # Envoie de data avec requête HTTP méthode PUT à l'url
        response = self.client.put(url, data, format='json')

        # Test si Status de la requête == HTTP_200_OK (Code de mise à jour réussi)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test si name de jeu<id_jeu> a été mis a jour en 'New Name'
        self.assertEqual(Jeu.objects.get(id_jeu=self.jeu.id_jeu).name, 'New Name')


    def test_delete_jeu(self):
        # url pour le delete '/api/jeu/<id_jeu>'
        url = reverse('Jeu-detail', args=[self.jeu.id_jeu])

        # Envoie de la requête de suppression sur url
        response = self.client.delete(url)

        # Test si status de la requête == HTTP_204_NO_CONTENT
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        #Test si l'objet a bien été supprimé
        self.assertEqual(Jeu.objects.count(), 0)
