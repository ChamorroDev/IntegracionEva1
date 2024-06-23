from django.test import TestCase
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'TiendaMusical.settings')
django.setup()

from tienda.models import Disco, FormatoDisco

def crear_discos_de_prueba():
 
   
    try:
        formato_id = FormatoDisco.objects.get(id=int(3))
    except FormatoDisco.DoesNotExist:
        print(f'El FormatoDisco con ID {formato_id} no existe.')
        return
    discos = [
        {
            'nombre': 'Folklore',
            'nombreAlbum': 'Folklore',
            'artista': 'Taylor Swift',
            'precio': 20,
            'stock': 100,
            'annopublicacion': 2020,
            'imagen': 'folklore.jpeg',
            'formato': formato_id,
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
            'formato':formato_id,
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
            'formato': formato_id,
            'oferta': False
        }
    ]

    for disco_data in discos:
        disco = Disco(nombre=disco_data['nombre'],
            nombreAlbum=disco_data['nombreAlbum'],
            artista=disco_data['artista'],
            precio=disco_data['precio'],
            stock=disco_data['stock'],
            annopublicacion=disco_data['annopublicacion'],
            imagen=disco_data['imagen'],
            formatos_id=disco_data['formato'],
            oferta=disco_data['oferta']
        )
        disco.save()

    print("Se han creado los discos de prueba.")

if __name__ == "__main__":
    crear_discos_de_prueba()
