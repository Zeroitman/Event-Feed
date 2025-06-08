import factory
from event_feed.models import Note, Advertisement, Achievement, User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"user{n}")
    first_name = factory.Sequence(lambda n: f"First name {n}")
    last_name = factory.Sequence(lambda n: f"Last name {n}")

    @factory.post_generation
    def achievements(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for achievement in extracted:
                self.achievements.add(achievement)


class NoteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Note

    title = factory.Sequence(lambda n: f"Note {n}")
    body = factory.Faker("text", max_nb_chars=20)
    created_by = factory.SubFactory(UserFactory)


class AdvertisementFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Advertisement

    title = factory.Sequence(lambda n: f"Advertisement {n}")
    description = factory.Faker("text", max_nb_chars=20)
    image = factory.django.ImageField()
    url = factory.Faker("url")


class AchievementFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Achievement

    title = factory.Sequence(lambda n: f"Achievement {n}")
    condition = factory.Faker("text", max_nb_chars=20)
    icon = factory.django.ImageField()
