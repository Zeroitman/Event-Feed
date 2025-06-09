from django.test import TestCase
from django.urls import reverse
from freezegun import freeze_time
from rest_framework.test import APIClient
from event_feed.tests.factories import (
    UserFactory, AdvertisementFactory, NoteFactory, AchievementFactory
)


class TestEventFeedOrderView(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()

    def test_user_get_event_feed_with_right_order(self):
        achievement = AchievementFactory(title="Must Be Last")

        with freeze_time("2025-06-04 11:00:00+06:00"):
            AdvertisementFactory(title="Should be in the middle")

        with freeze_time("2025-06-01 11:00:00+06:00"):
            user = UserFactory(achievements=[achievement])
        with freeze_time("2025-06-08 11:00:00+06:00"):
            NoteFactory(created_by=user, title="Must Be First")

        expected_result = 3
        expected_titles = [
            'Must Be First', 'Should be in the middle', 'Must Be Last'
        ]
        response = self.client.get(reverse(
            viewname="event_feed:list",
            kwargs={"pk": user.pk}
        ))
        response_data = response.json()

        self.assertEqual(response_data["count"], expected_result)
        self.assertEqual(response.status_code, 200)

        titles = [item['title'] for item in response_data["results"]]
        self.assertEqual(titles, expected_titles)
