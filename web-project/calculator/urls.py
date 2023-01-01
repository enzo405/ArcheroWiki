from django.urls import path
from calculator import views
from calculator import views_wiki
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views_wiki.menu),
    path('calculator/', views.index_calc),
    path('calculator/create/', views.formulaire_calc),
    path('calculator/calc/', views.traitement_calc),
    path('calculator/show/<str:iid>/', views.affiche_calc),
    path('calculator/index/', views.index_calc),
    path('calculator/update/<str:iid>/', views.update_calc),
    path('calculator/updatecalc/<str:iid>/', views.updatetraitement_calc),
    path('calculator/delete/<str:iid>/', views.delete_user),
    path('wiki/maze/', views_wiki.maze),
    path('login/', views_wiki.login),
    path('wiki/menu', views_wiki.wiki_theorycrafting),
    path('wiki/item', views_wiki.item_description),
    path('wiki/skill-list', views_wiki.skill_description),
    path('wiki/runes', views_wiki.runes),
    path('wiki/runes/calc/<str:iid>/', views_wiki.runesCalc_processing),
    path('wiki/runes/<str:iid>/', views_wiki.runesCalc),
    path('wiki/archive/', views_wiki.ghssetGrid)
]

urlpatterns += staticfiles_urlpatterns()