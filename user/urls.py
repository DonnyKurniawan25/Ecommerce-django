from django.urls import path, include

from . import views

urlpatterns = [

    path('', views.index, name='index'),


    # path('contact/', views.contact, name='contact'),
    # path('berita/', views.berita, name='berita'),
    # path('pengumuman/', views.pengumuman, name='pengumuman'),

    # ADMIN
    # path('loginadmin/', views.loginadmin, name='loginadmin'),
    # path('adminopd/', views.admin, name='adminopd'),
    # path('beritaadmin/', views.beritaadmin, name='beritaadmin'),
    # path('pengumumanadmin/', views.pengumumanadmin, name='pengumumanadmin'),
    # path('tambahberita/', views.tambahberita, name='tambahberita'),
    # path('hapusberita/<int:id>/', views.hapusberita),
    # path('ubahberita/<int:id_ubah>/', views.ubahberita, name='ubahberita'),
    # path('slideshow/', views.slideshow, name='slideshow'),
    # path('slideshow/tambahslide/', views.tambahslide, name='tambahslide'),
    # path('tampilberita/<int:id_tampil>/', views.tampilberita, name='tampilberita'),

    # path('Tentang/', views.tentang, name='Tentang'),
    # path('Visimisi/', views.visimisi, name='Visimisi'),
    # path('Tugasfungsi/', views.tugasfungsi, name='Tugasfungsi'),
    # path('Strukturorganisasi/', views.strukturorganisasi, name='Strukturorganisasi'),
    # path('Profilpejabat/', views.pejabat, name='Profilpejabat'),

    # path('Tentangadmin/', views.tentangadmin, name='Tentangadmin'),
    # path('edittentang/<int:id_edit>/', views.edittentang, name='edittentang'),

    # path('Visimisiadmin/', views.visimisiadmin, name='Visimisiadmin'),
    # path('Strukturadmin/', views.strukturadmin, name='Strukturadmin'),
    # path('Tugasfungsiadmin/', views.tugasfungsiadmin, name='Tugasfungsiadmin'),
    # path('Profiladmin/', views.profiladmin, name='Profiladmin'),

    # path('Fotoadmin/', views.fotoadmin, name='Fotoadmin'),
    # path('Videoadmin/', views.videoadmin, name='Videoadmin'),
    ]
