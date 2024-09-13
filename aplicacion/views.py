from django.shortcuts import render

def app(request):
    
    capitan= {'pelicula': 'ciencia ficcion',
              'autor' : 'Jack Kitby',
              'Anio Salida' : '2026'}
    
    kunfupanda = {'pelicula' : 'entretenimiento',
                  'autor' : 'DreamWorks',
                  'Anio salida' : '2024'}
    
    soul = {'pelicula' : 'entretenimiento',
            'autor' : 'Peter Docter',
            'Anio salida' : '2024'}
    
    return app