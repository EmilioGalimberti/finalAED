__author__ = 'Cátedra AED'

# Una aplicación práctica para conocer el tamaño total del archivo usando seek,
# sin necesidad de usar la función os.path.getsize().
import io

def size(fd):
    file = open(fd, 'rb')
    file.seek(0, io.SEEK_END)
    t = file.tell()
    file.close()
    return t

def test():
    fd = 'libros.dat'
    print('El tamaño del archivo es:', size(fd), ' bytes')

if __name__ == '__main__':
    test()
