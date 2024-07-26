from django.test import TestCase
from news.models import News, Category
from django.shortcuts import reverse


class NewsTest(TestCase):
    def setUp(self):
        self.tag1 = Category.objects.create(name='test')
        self.tag2 = Category.objects.create(name='test2')
        self.newsOne = News.objects.create(
            title='t1',
            content='This is t1',
            source='t1.com',
        )
        self.newsOne.category.set([self.tag1, self.tag2])

    def test_home_url(self):
        res = self.client.get('/')
        res2 = self.client.get(reverse('home'))
        res3 = self.client.get('/?category=1')
        self.assertEqual(res3.status_code, 200)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res2.status_code, 200)
        self.assertEqual(self.newsOne.title, "t1")
        self.assertEqual(self.newsOne.content, "This is t1")
        self.assertEqual(self.newsOne.source, 't1.com')