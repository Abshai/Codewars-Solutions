def greet(language):
    
    languages = { "english": "Welcome"
    , "czech": "Vitejte"
    , "danish": "Velkomst"
    , "dutch": "Welkom"         
    , "estonian": "Tere tulemast"
    , "finnish": "Tervetuloa"
    , "flemish": "Welgekomen"
    , "french": "Bienvenue"
    , "german": "Willkommen"
    , "irish" : "Failte"
    , "italian": "Benvenuto"
    , "latvian": "Gaidits"
    , "lithuanian": "Laukiamas"
    , "polish": "Witamy"
    , "spanish": "Bienvenido"
    , "swedish": "Valkommen"
    , "welsh": "Croeso"
    }

    for x, y in languages.items():
        if language == x:
            return(y)
        
    return languages["english"]

    # Pythonic way:
    # return languages.get(language, languages["english"])