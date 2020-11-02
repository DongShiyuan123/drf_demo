from . import views

urlpatterns = [

]

# drf中的路由
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', views.BookInfoModelViewSet, basename="books")
urlpatterns += router.urls
