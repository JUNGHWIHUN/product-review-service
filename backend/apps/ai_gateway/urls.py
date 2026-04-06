from django.urls import path
from .views import (
    EmbeddingAPIView,     # [유지] 기존 사용 중이면 유지
    SimilarityAPIView,    # [유지] 기존 사용 중이면 유지
    ReviewAnalyzeAPIView, # [유지] 분석 API
    ReviewAnalyzeTaskStatusAPIView,
)

urlpatterns = [
    # [유지] 기존 URL
    path("reviews/<int:review_id>/analyze/", ReviewAnalyzeAPIView.as_view(), name="ai-review-analyze"),
    path("tasks/<str:task_id>/status/", ReviewAnalyzeTaskStatusAPIView.as_view(), name="ai-task-status"),
]