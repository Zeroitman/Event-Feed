from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from event_feed.models import Note, Advertisement, User, UserAchievement
from event_feed.serializers import (
    EventFeedSerializer, EventFeedQueryParamSerializer
)
from event_feed.service.get_event_feed import get_event_feed


class EventFeedAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = EventFeedSerializer
    query_serializer = EventFeedQueryParamSerializer
    pagination_class = PageNumberPagination
    queryset = User.objects.exclude(is_staff=True)
    lookup_field = "pk"

    @extend_schema(
        summary="Get Event Feed",
        responses={status.HTTP_200_OK: EventFeedSerializer(many=True)},
        parameters=[EventFeedQueryParamSerializer]
    )
    def get(self, request, *args, **kwargs):
        lookup_value = self.kwargs.get(self.lookup_field)
        user = get_object_or_404(
            self.queryset, **{self.lookup_field: lookup_value}
        )

        query = self.request.query_params

        models = dict()
        for model in [Note, Advertisement, UserAchievement]:
            models[model] = [f.name for f in model._meta.get_fields()]

        data = get_event_feed(
            models=models,
            user_id=user.id,
            event_type=query.get("event_type", ""),
            search=query.get("search", "")
        )
        serializer_data = self.serializer_class(data, many=True).data
        paginator = self.pagination_class()
        paginated = paginator.paginate_queryset(serializer_data, request)
        return paginator.get_paginated_response(paginated)
