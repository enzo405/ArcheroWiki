from django.urls import path
from calculator import views
from calculator import views_wiki
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('', views_wiki.menu),
    path('calculator/', views.index_calc),
    path('calculator/create/', views.formulaire_calc),
    path('calculator/calc/', views.traitement_calc),
    path('calculator/show/<str:pbid>/', views.affiche_calc),
    path('calculator/index/', views.index_calc),
    path('calculator/update/<str:pbid>/', views.update_calc),
    path('calculator/updatecalc/<str:pbid>/', views.updatetraitement_calc),
    path('calculator/delete/<str:pbid>/', views.delete_user),
    path('wiki/maze/', views_wiki.maze),
    path('login/', views_wiki.login),
    path('login/processing/<str:username_raw>/<str:id>/', views_wiki.login_processing),
    path('wiki/menu', views_wiki.wiki_theorycrafting),
    path('wiki/item', views_wiki.item_description),
    path('wiki/heroes', views_wiki.heros_description),
    path('wiki/skill-list', views_wiki.skill_description),
    path('wiki/damage-calculator', views_wiki.damage),
    path('wiki/damage-calculator/calc/<str:pbid>/', views_wiki.dmgCalc_processing),
    path('wiki/damage-calculator/<str:pbid>/', views_wiki.damageCalc),
    path('wiki/archive/', views_wiki.ghssetGrid),
    path('wiki/upgrade', views_wiki.upgrade_cost),
    path('habby-secret/', views_wiki.rickroll),
    path('wiki/promo-code', views_wiki.promocode)
]

urlpatterns += staticfiles_urlpatterns()