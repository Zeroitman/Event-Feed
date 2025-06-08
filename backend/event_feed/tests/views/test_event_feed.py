from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from event_feed.tests.factories import (
    UserFactory, AdvertisementFactory, NoteFactory, AchievementFactory
)


class TestEventFeedView(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()

        cls.advertisements = AdvertisementFactory.create_batch(3)
        cls.advertisement = AdvertisementFactory(title="search name")

        cls.achievements = AchievementFactory.create_batch(2)
        cls.achievement = AchievementFactory(title="search title")

        # data for user vasya
        cls.user_vasya = UserFactory(achievements=cls.achievements)
        cls.notes_vasya = NoteFactory.create_batch(2, created_by=cls.user_vasya)

        # data for user petya
        cls.user_petya = UserFactory(achievements=[cls.achievement])
        cls.notes_petya = NoteFactory.create_batch(4, created_by=cls.user_petya)

    def test_staff_user_return_404(self):
        staff_user = UserFactory(is_staff=True)
        response = self.client.get(reverse(
            viewname="event_feed:list",
            kwargs={"pk": staff_user.pk}
        ))
        self.assertEqual(response.status_code, 404)

    def test_user_not_found(self):
        response = self.client.get(reverse(
            viewname="event_feed:list",
            kwargs={"pk": 123}
        ))
        self.assertEqual(response.status_code, 404)

    def test_user_get_advertisements_without_achievements_and_notes(self):
        expected_result = 4
        user = UserFactory()
        response = self.client.get(reverse(
            viewname="event_feed:list",
            kwargs={"pk": user.pk}
        ))
        response_data = response.json()
        self.assertEqual(response_data["count"], expected_result)
        self.assertEqual(response.status_code, 200)

    def test_user_vasya_get_event_feed(self):
        expected_result = 8
        response = self.client.get(reverse(
            viewname="event_feed:list",
            kwargs={"pk": self.user_vasya.pk}
        ))
        response_data = response.json()
        self.assertEqual(response_data["count"], expected_result)
        self.assertEqual(response.status_code, 200)

    def test_user_vasya_get_event_feed_filter_by_achievements(self):
        expected_result = 6
        response = self.client.get(reverse(
            viewname="event_feed:list",
            kwargs={"pk": self.user_vasya.pk}
        ), query_params={"type": "achievement"})
        response_data = response.json()
        self.assertEqual(response_data["count"], expected_result)
        self.assertEqual(response.status_code, 200)

    def test_user_petya_get_event_feed(self):
        expected_result = 9
        response = self.client.get(reverse(
            viewname="event_feed:list",
            kwargs={"pk": self.user_petya.pk}
        ))
        response_data = response.json()
        self.assertEqual(response_data["count"], expected_result)
        self.assertEqual(response.status_code, 200)

    def test_user_petya_get_event_feed_filter_by_note(self):
        expected_result = 8
        response = self.client.get(reverse(
            viewname="event_feed:list",
            kwargs={"pk": self.user_petya.pk}
        ), query_params={"type": "note"})
        response_data = response.json()
        self.assertEqual(response_data["count"], expected_result)
        self.assertEqual(response.status_code, 200)

    def test_user_petya_get_event_feed_filter_by_search(self):
        expected_result = 2
        response = self.client.get(reverse(
            viewname="event_feed:list",
            kwargs={"pk": self.user_petya.pk}
        ), query_params={"search": "sea"})
        response_data = response.json()
        self.assertEqual(response_data["count"], expected_result)
        self.assertEqual(response.status_code, 200)
