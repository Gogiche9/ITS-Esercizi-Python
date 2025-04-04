#8-7. Album

def make_album(artist_name,album_title,songs = None):
    if songs != None and songs > 0:
        album = {"artist":artist_name,"album":album_title,"songs":songs}
        for k,v in album.items():
            print(k,v)
    else:
        album = {"artist":artist_name,"album":album_title}
        for k,v in album.items():
            print(k,v)
        
make_album("Caparezza","Museica")
make_album("De Andre","La lieta Novella")
make_album("Ozzy","Robe")
make_album("Tizio","Album1",11)




