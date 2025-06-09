from django.db.models import CharField, Value, F
from event_feed.serializers import Entity


def get_event_feed(
        models: dict, user_id: int, event_type: str, search: str
) -> list:
    result_list = []

    for model, fields in models.items():
        entity_name = model.__name__.lower()

        records = model.objects.annotate(
            entity=Value(
                entity_name,
                output_field=CharField()
            ),
            head=(
                F('achievement__title')
                if 'achievement' in fields
                else F('title')
            )
        ).order_by('-created_at')

        if entity_name == Entity.Note.value:
            records = records.filter(created_by=user_id)
        elif entity_name == Entity.Achievement.value:
            records = records.filter(user_id=user_id)

        if event_type:
            records = records.filter(entity__in=['advertisement', event_type])
        if search:
            records = records.filter(head__icontains=search)

        result_list += list(records)
    return sorted(result_list, key=lambda x: x.created_at, reverse=True)
