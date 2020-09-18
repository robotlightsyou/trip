from django.urls import path
from inventory import views as iviews

urlpatterns = [
    path('', iviews.inventory_home, name='trip_inventory-home'),
    path('company/', iviews.company, name='trip_inventory-company'),
    path('out/', iviews.out, name='trip_inventory-out'),
    path('personal/', iviews.personal, name='trip_inventory-personal'),

    # add views for simpleisbetter... dynamic dropdown method
    path('fixture/', iviews.FixtureListView.as_view(), name='fixture-list'),
    path('fixture/add/', iviews.FixtureCreateView.as_view(), name='fixture-add'),
    path('fixture/<int:pk>/', iviews.FixtureUpdateView.as_view(), name='fixture_update'),
    path('ajax/load-kinds/', iviews.load_kinds, name='ajax_load_kinds'),
]
