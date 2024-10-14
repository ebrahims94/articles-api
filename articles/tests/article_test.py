from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework import status
from articles.models import Article

ARTICLE_DATA = dict(
    title='test article title', 
    description='this is description for article',
    image='https://www.google.com/images',
    status=Article.STATUS_CHOICES[0][0],
)

ARTICLE_DATA1 = dict(
    title='test article title new', 
    description='this is description for article new',
    image='https://www.google.com/images2',
    status=Article.STATUS_CHOICES[1][0],
)

ARTICLE_DATA_NEW_USER = dict(
    title='test article title new user', 
    description='this is description for article new user',
    image='https://www.google.com/images2123',
    status=Article.STATUS_CHOICES[0][0],
)

class ArticleListCreateViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.user_access_token = AccessToken.for_user(self.user)
        self.new_user = User.objects.create(username='new_testuser')
        self.new_user_access_token = AccessToken.for_user(self.new_user)
        ARTICLE_DATA['user'] = self.user
        ARTICLE_DATA1['user'] = self.user
        ARTICLE_DATA_NEW_USER['user'] = self.new_user
        self.article1 = Article.objects.create(**ARTICLE_DATA)
        self.article2 = Article.objects.create(**ARTICLE_DATA_NEW_USER)

    def test_list_articles_user_1(self):
        url = reverse('article-list')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.user_access_token}')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_list_articles_user_2(self):
        url = reverse('article-list')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.new_user_access_token}')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
    
    def test_create_article(self):
        url = reverse('article-list')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.user_access_token}')
        response = self.client.post(url, ARTICLE_DATA1)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data['title'], ARTICLE_DATA1['title'])
        self.assertEqual(response.data['description'], ARTICLE_DATA1['description'])
        self.assertEqual(response.data['image'], ARTICLE_DATA1['image'])
        self.assertEqual(response.data['status'], ARTICLE_DATA1['status'])
        self.assertEqual(response.data['user'], self.user.pk)

   

class ArticleDetailViewTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser')
        self.user_access_token = AccessToken.for_user(self.user)
        self.new_user = User.objects.create(username='new_testuser')
        self.new_user_access_token = AccessToken.for_user(self.new_user)
        ARTICLE_DATA['user'] = self.user
        ARTICLE_DATA1['user'] = self.user
        ARTICLE_DATA_NEW_USER['user'] = self.new_user
        self.article1 = Article.objects.create(**ARTICLE_DATA)
        self.article2 = Article.objects.create(**ARTICLE_DATA1)
        self.article3 = Article.objects.create(**ARTICLE_DATA_NEW_USER)

    def test_retrieve_article(self):
        url = reverse('article-detail', kwargs={'pk': self.article1.pk})
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.user_access_token}')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'test article title')
    
    def test_update_article(self):
        data = {'title': 'Updated title', 'description': 'Updated descreption', 'status': Article.STATUS_CHOICES[0][0]}
        url = reverse('article-detail', kwargs={'pk': self.article1.pk})
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.user_access_token}')
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], data['title'])
        self.assertEqual(response.data['description'], data['description'])
        self.assertEqual(response.data['status'], data['status'])
        self.assertEqual(response.data['user'], self.user.pk)
    
    def test_delete_article(self):
        url = reverse('article-detail', kwargs={'pk': self.article2.pk})
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.user_access_token}')
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
    