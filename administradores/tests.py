from django.test import TestCase



import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TiendaMusical.settings')
django.setup()

from tuapp.models import Disco, FormatoDisco

def crear_discos_de_prueba():
 

    # Crear discos de prueba
    discos = [
        {
            'nombre': 'Folklore',
            'nombreAlbum': 'Folklore',
            'artista': 'Taylor Swift',
            'precio': 20,
            'stock': 100,
            'annopublicacion': 2020,
            'imagen': 'folklore.jpeg',
            'formato': 1,
            'oferta': False
        },
        {
            'nombre': 'evermore',
            'nombreAlbum': 'evermore',
            'artista': 'Taylor Swift',
            'precio': 25,
            'stock': 80,
            'annopublicacion': 2020,
            'imagen': 'evermore.jpeg',
            'formato': 1,
            'oferta': True
        },
        {
            'nombre': '1989',
            'nombreAlbum': '1989',
            'artista': 'Taylor Swift',
            'precio': 18,
            'stock': 120,
            'annopublicacion': 2014,
            'imagen': '1989.jpg',
            'formato': 1,
            'oferta': False
        }
    ]

    for disco_data in discos:
        disco = Disco.objects.create(
            nombre=disco_data['nombre'],
            nombreAlbum=disco_data['nombreAlbum'],
            artista=disco_data['artista'],
            precio=disco_data['precio'],
            stock=disco_data['stock'],
            annopublicacion=disco_data['annopublicacion'],
            imagen=disco_data['imagen'],
            formatos=disco_data['formato'],
            oferta=disco_data['oferta']
        )
        disco.save()

    print("Se han creado los discos de prueba.")

if __name__ == "__main__":
    crear_discos_de_prueba()
