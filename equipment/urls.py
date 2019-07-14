from django.urls import path, include, re_path

from .views import let_equipment_view, sell_equipment_view, all_let_equipments_view, all_sell_equipments_view, let_equipment_detail_view, sell_equipment_detail_view


urlpatterns = [
    path('let-equipment/', let_equipment_view, name="let-equipment"),
    path('sell-equipment/', sell_equipment_view, name="sell-equipment"),
    path('all-let-equipments/', all_let_equipments_view, name="all-let-equipments"),
    path('all-sell-equipments/', all_sell_equipments_view, name="all-sell-equipments"),
    path('let/detail/<int:equipment_id>', let_equipment_detail_view, name="let_equipment_detail"),
    path('sell/detail/<int:equipment_id>', sell_equipment_detail_view, name="sell_equipment_detail"),

    
]