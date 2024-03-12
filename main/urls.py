from django.urls import path

from main import views


urlpatterns = [
    # main list
    path('statistics/', views.MainListStatisticsAPI.as_view()),
    path('list/', views.SiteListAPI.as_view()),
    path('category/', views.MainListCategoryListAPI.as_view()),
    path('increase/', views.IncreaseECommerceResourceAPI.as_view()),
    path('os-diagram/', views.MainListOSStatisticsAPI.as_view()),
    path('browser-diagram/', views.MainListBrowserStatisticsAPI.as_view()),

]

