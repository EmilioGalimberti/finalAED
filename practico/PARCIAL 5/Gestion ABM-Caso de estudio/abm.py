__author__ = 'Cátedra AED'

import io
import pickle
import os.path

class Estudiante:
    def __init__(self, leg, nom, prom):
        self.legajo = leg
        self.nombre = nom
        self.promedio = prom
        self.activo = True


def to_string(est):
    r = ''
    r += '{:<20}'.format('Legajo: ' + str(est.legajo))
    r += '{:<30}'.format('Nombre: ' + est.nombre.strip())
    r += '{:<20}'.format('Promedio: ' + str(est.promedio))
    return r


def validar_legajo(inf, sup):
    n = inf - 1
    while n < inf or n > sup:
        n = int(input('Valor entre ' + str(inf) + ' y ' + str(sup) + ' por favor: '))
        if n < inf or n > sup:
            print('Se pidió entre', inf, 'y', sup, '... cargue de nuevo...')
    return n


def validar_promedio():
    n = -1.0
    while n < 0.0 or n > 10.0:
        n = float(input('Valor entre 0 y 10 por favor (puede tener decimales): '))
        if n < 0 or n > 10:
            print('Error... se pidió entre 0 y 10... cargue de nuevo...')
    return n

def buscar(fd, m, leg):
    t = os.path.getsize(fd)
    #Guardamos en fp_inicial donde el file pointer se encuentra ubicado antes de
    #iniciar la búsqueda.
    fp_inicial = m.tell()
    #Nos posicionamos al principio del archivo..
    m.seek(0, io.SEEK_SET)
 
    posicion = -1
    while m.tell() < t:
        #En fp guardo el nro de byte (de inicio)
        #del registro que voy a leer..(Aun no lo he leído..)
        fp = m.tell()
        est = pickle.load(m)
        if est.activo == True and est.legajo == leg:
            #En posición guardo el nro de byte en que inicio el registro..
            posicion = fp
            break

    #Dejamos el puntero en el mismo lugar antes de iniciar el proceso de busqueda..
    m.seek(fp_inicial, io.SEEK_SET)
    return posicion


def alta(fd):
    """Agrega el registro de un estudiante al archivo.
    Los datos del estudiante se toman por teclado. El registro será grabado sólo si el
    archivo no contenía ya un estudiante con el mismo legajo.
    """

    m = open(fd, 'a+b')

    print()
    print('Legajo del estudiante a registrar (cargue 0 para salir): ')
    leg = validar_legajo(0, 99999)
    while leg != 0:
        # buscamos el registro con ese legajo...
        pos = buscar(fd, m, leg)
        if pos == -1:
            # no estaba repetido... lo cargamos por teclado...
            nom = input('Nombre: ')

            # ...ajustamos a 30 caracteres, rellenando con blancos al final...
            nom = nom.ljust(30, ' ')[:30]

            print('Promedio...')
            pro = validar_promedio()

            est = Estudiante(leg, nom, pro)

            # ...lo grabamos...
            pickle.dump(est, m)

            # ...volcamos el buffer de escritura
            # para que el sistema operativo REALMENTE
            # grabe en disco el registro...
            m.flush()

            print('Registro grabado en el archivo...')

        else:
            print('Legajo repetido... alta rechazada...')

        print()
        print('Otro legajo de estudiante a registrar (cargue 0 para salir): ')
        leg = validar_legajo(0, 99999)

    m.close()

    print()
    print('Operación de altas finalizada...')
    input('Presione <Enter> para seguir...')

# Baja física.
def depuracion(fd):
    """Optimiza el espacio físico del archivo.

    La función aplica un proceso de baja física generalizada: todos los registros que estaban
    marcados en forma lógica como eliminados, son físicamente eliminados del archivo.
    """

    if not os.path.exists(fd):
        print('El archivo', fd, 'no existe... use la opción 1 para crearlo y grabarle registros...')
        print()
        return

    tbm = os.path.getsize(fd)

    original = open(fd, 'rb')
    temporal = open('temporal.dat', 'wb')

    print('Procediendo a optimizar el archivo', fd, '(eliminación física de registros borrados)')
    while original.tell() < tbm:
        # cargar un registro del archivo original...
        est = pickle.load(original)

        # ...y si no estaba marcado como eliminado, grabarlo en el archivo temporal...
        if est.activo:
            pickle.dump(est, temporal)

    # cerrar ambos archivos...
    original.close()
    temporal.close()

    # eliminar el archivo original...
    os.remove(fd)

    # y renombrar el temporal...
    os.rename('temporal.dat', fd)

    print('Optimización terminada... se eliminaron los registros marcados como borrados...')
    input('Presione <Enter> para seguir...')

# Baja lógica.
def baja(fd):
    """Elimina (por marcado lógico) el registro de un estudiante del archivo.

    El legajo del estudiante a eliminar se toma por teclado. El registro será eliminado sólo si el
    usuario confirma que está seguro de querer hacerlo, y el registro será en ese caso marcado en forma
    lógica y vuelto a grabar.
    """

    if not os.path.exists(fd):
        print('El archivo', fd, 'no existe... use la opción 1 para crearlo y grabarle registros...')
        print()
        return

    m = open(fd, 'r+b')

    print()
    print('Legajo del estudiante a borrar (cargue 0 para salir): ')
    leg = validar_legajo(0, 99999)
    while leg != 0:
        # buscamos el registro con ese legajo...
        pos = buscar(fd, m, leg)
        if pos != -1:
            # encontrado... procedemos a borrarlo...
            m.seek(pos, io.SEEK_SET)
            est = pickle.load(m)

            # ...mostramos el registro tal como estaba...
            print()
            print('El registro actualmente grabado es:')
            print(to_string(est))

            # ...chequemos si el usario está seguro de lo que hace...
            r = input('Está seguro de querer borrarlo (s/n)?: ')
            if r in ['s', 'S']:
                # lo marcamos como borrado, y ya...
                est.activo = False

                # ...reubicamos el file pointer en donde inicia el registro a borrar...
                m.seek(pos, io.SEEK_SET)

                # ...y lo volvemos a grabar para actualizar el campo activo a False...
                pickle.dump(est,m)

                print()
                print('Registro eliminado del archivo...')

        else:
            print('Ese registro no existe en el archivo...')

        print()
        print('Otro legajo de estudiante a borrar (cargue 0 para salir): ')
        leg = validar_legajo(0, 99999)

    m.close()

    print()
    print('Operación de bajas finalizada...')
    input('Presione <Enter> para seguir...')



def modificacion(fd):
    """Modifica el contenido de un registro de un estudiante del archivo.

    El legajo del estudiante a modificar se toma por teclado. Sólo se permitirá modificar el valor
    de los campos nombre y promedio, cuyos nuevos valores serán tomados por teclado mediante un menú.
    Cuando el usuario disponga terminar de cargar los nuevos datos, el registro se vuelve a grabar con
    sus nuevos datos en su ubicación original.
    """

    if not os.path.exists(fd):
        print('El archivo', fd, 'no existe... use la opción 1 para crearlo y grabarle registros...')
        print()
        return

    m = open(fd, 'r+b')

    print()
    print('Legajo del estudiante a modificar (cargue 0 para salir): ')
    leg = validar_legajo(0, 99999)
    while leg != 0:
        # buscamos el registro con ese legajo...
        pos = buscar(fd, m, leg)
        if pos != -1:
            # encontrado... procedemos a modificarlo...
            m.seek(pos, io.SEEK_SET)
            est = pickle.load(m)

            # ...mostramos el registro tal como estaba...
            print()
            print('El registro actualmente grabado es:')
            print(to_string(est))

            # ...modificamos el valor de los campos...
            op = 0
            while op != 3:
                print('1. Modificar nombre.')
                print('2. Modificar promedio.')
                print('3. Terminar modificaciones.')
                op = int(input('\t\tIngrese opción: '))

                if op == 1:
                    nom = input('Nuevo nombre: ')
                    est.nombre = nom.ljust(30, ' ')[:30]

                elif op == 2:
                    print('Nuevo promedio:')
                    est.promedio = validar_promedio()

                elif op == 3:
                    pass

            # ...registro modificado en memoria...
            # ...ahora nos volvemos a su posición en el archivo...
            m.seek(pos, io.SEEK_SET)

            # ...y volvemos a grabar el registro modificado...
            pickle.dump(est, m)

            print()
            print('Los datos del registro se actualizaron en el archivo...')

        else:
            print('Ese registro no existe en el archivo...')

        print('Otro legajo de estudiante a modificar (cargue 0 para salir): ')
        leg = validar_legajo(0, 99999)

    m.close()

    print()
    print('Operación de modificaciones finalizada...')
    input('Presione <Enter> para seguir...')

def listado_completo(fd):
    """Muestra el contenido completo del archivo.
    """

    if not os.path.exists(fd):
        print('El archivo', fd, 'no existe... use la opción 1 para crearlo y grabarle registros...')
        print()
        return

    tbm = os.path.getsize(fd)

    m = open(fd, 'rb')

    print('Listado general de estudiantes registrados:')
    while m.tell() < tbm:
        est = pickle.load(m)
        if est.activo: # est.activo == True
            print(to_string(est))

    m.close()

    print()
    input('Presione <Enter> para seguir...')


def listado_filtrado(fd):
    """Muestra los registros de los estudiantes cuyo promedio sea >= 7.

    """

    if not os.path.exists(fd):
        print('El archivo', fd, 'no existe... use la opción 1 para crearlo y grabarle registros...')
        print()
        return

    tbm = os.path.getsize(fd)

    m = open(fd, 'rb')

    print('Listado de estudiantes con promedio mayor o igual a 7:')
    while m.tell() < tbm:
        est = pickle.load(m)
        if est.activo and est.promedio >= 7:
            print(to_string(est))

    m.close()

    print()
    input('Presione <Enter> para seguir...')


def main():
    fd = 'estudiantes.dat'

    op = 0
    while op != 7:
        print('Opciones ABM del archivo de estudiantes')
        print('   1. Alta de estudiantes')
        print('   2. Baja de estudiantes')
        print('   3. Modificación de estudiantes')
        print('   4. Listado completo de estudiantes')
        print('   5. Listado de estudiantes con promedio mayor o igual a 7')
        print('   6. Depuración del archivo de estudiantes')
        print('   7. Salir')
        op = int(input('\t\tIngrese número de la opción elegida: '))
        print()

        if op == 1:
            alta(fd)

        elif op == 2:
            baja(fd)

        elif op == 3:
            modificacion(fd)

        elif op == 4:
            listado_completo(fd)

        elif op == 5:
            listado_filtrado(fd)

        elif op == 6:
            depuracion(fd)

        elif op == 7:
            print('Gracias por usar el programa!')


# script principal...
if __name__ == '__main__':
    main()