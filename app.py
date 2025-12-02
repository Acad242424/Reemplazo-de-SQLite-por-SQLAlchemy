from database import SessionLocal, engine
from models import Base, Libro

Base.metadata.create_all(bind=engine)

def crear_libro():
    session = SessionLocal()

    titulo = input("Título del libro: ")
    autor = input("Autor: ")
    genero = input("Género: ")
    estado = input("Estado de lectura: ")

    libro = Libro(
        titulo=titulo,
        autor=autor,
        genero=genero,
        estado=estado
    )

    session.add(libro)
    session.commit()
    session.close()
    print("Libro agregado correctamente.")

def actualizar_libro():
    session = SessionLocal()
    id_libro = int(input("ID del libro a actualizar: "))

    libro = session.query(Libro).filter_by(id=id_libro).first()

    if libro:
        libro.titulo = input(f"Título ({libro.titulo}): ") or libro.titulo
        libro.autor = input(f"Autor ({libro.autor}): ") or libro.autor
        libro.genero = input(f"Género ({libro.genero}): ") or libro.genero
        libro.estado = input(f"Estado ({libro.estado}): ") or libro.estado

        session.commit()
        print("Libro actualizado.")
    else:
        print("Libro no encontrado.")

    session.close()

def eliminar_libro():
    session = SessionLocal()
    id_libro = int(input("ID del libro a eliminar: "))

    libro = session.query(Libro).filter_by(id=id_libro).first()

    if libro:
        session.delete(libro)
        session.commit()
        print("Libro eliminado.")
    else:
        print("Libro no encontrado.")

    session.close()

def ver_libros():
    session = SessionLocal()
    libros = session.query(Libro).all()

    for libro in libros:
        print(f"ID: {libro.id} | {libro.titulo} - {libro.autor} - {libro.genero} - {libro.estado}")

    session.close()

def buscar_libros():
    session = SessionLocal()
    termino = input("Buscar por título, autor o género: ")

    resultados = session.query(Libro).filter(
        (Libro.titulo.like(f"%{termino}%")) |
        (Libro.autor.like(f"%{termino}%")) |
        (Libro.genero.like(f"%{termino}%"))
    ).all()

    for libro in resultados:
        print(f"ID: {libro.id} | {libro.titulo} - {libro.autor} - {libro.genero} - {libro.estado}")

    session.close()

def menu():
    while True:
        print("
BIBLIOTECA PERSONAL")
        print("1. Agregar libro")
        print("2. Actualizar libro")
        print("3. Eliminar libro")
        print("4. Ver lista de libros")
        print("5. Buscar libros")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            crear_libro()
        elif opcion == "2":
            actualizar_libro()
        elif opcion == "3":
            eliminar_libro()
        elif opcion == "4":
            ver_libros()
        elif opcion == "5":
            buscar_libros()
        elif opcion == "6":
            break

if __name__ == "__main__":
    menu()
