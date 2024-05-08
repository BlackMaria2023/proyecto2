from arriendos.forms import RegistroUsuarioForm
from arriendos.models import Inmueble, Usuario
from django.core.exceptions import ObjectDoesNotExist


def crear_inmueble(
        nombre,
        direccion,
        descripcion,
        imagen,
        precio,
        comuna,
        disponible,
        m2_construidos,
        m2_terreno,
        cantidad_estacionamientos,
        cantidad_habitaciones,
        cantidad_banos,
        tipo_de_inmueble,
        propietario
):
    inmueble = Inmueble.objects.create(
        nombre=nombre,
        direccion=direccion,
        descripcion=descripcion,
        imagen=imagen,
        precio=precio,
        comuna=comuna,
        disponible=disponible,
        m2_construidos=m2_construidos,
        m2_terreno=m2_terreno,
        cantidad_estacionamientos=cantidad_estacionamientos,
        cantidad_habitaciones=cantidad_habitaciones,
        cantidad_banos=cantidad_banos,
        tipo_de_inmueble=tipo_de_inmueble,
        propietario=propietario,
    )

    return inmueble

def crear_usuario(
        nombres,
        apellidos,
        rut,
        direccion,
        telefono,
        tipo_usuario,
        correo_electronico,
        password,
        username
    ):

    usuario = Usuario.objects.filter(rut=rut)
    if usuario.exists():
        print("Usuario ya existe:", usuario.first().username)
        return usuario.first()
    
    data = {
        "nombres": nombres,
        "apellidos": apellidos,
        "rut": rut,
        "direccion": direccion,
        "telefono": telefono,
        "tipo_usuario": tipo_usuario,
        "correo_electronico": correo_electronico,
        "password": password,
        "username": username
    }
    form = RegistroUsuarioForm(data)
    if form.is_valid():
        usuario = form.save(commit=False)
        usuario.set_password(data['password'])
        usuario.save()
        print("Usuario creado con éxito:", usuario.username)
        return usuario
    else:
        print("Errores en el formulario:", form.errors)
        return None

def enlistar_inmuebles():
    inmuebles = Inmueble.objects.all()
    if len(inmuebles) == 0:
        print("No hay inmuebles")
        return
    for inmueble in inmuebles:
        print("ID:", inmueble.id)
        print("Nombre inmueble: ", inmueble.nombre)
        print("Tipo inmueble: ", inmueble.tipo_de_inmueble)
        print("Propietario: ", inmueble.propietario)
        print("________________________________")

def actualizar_campo_inmueble(inmueble_id, campo, valor):
    try:
        inmueble = Inmueble.objects.get(id=inmueble_id)
        if hasattr(inmueble, campo):
            setattr(inmueble, campo, valor)
            inmueble.save()
            return f"Campo '{campo}' actualizado exitosamente a '{valor}' en inmueble '{inmueble.nombre}'"
        else:
            return f"El campo '{campo}' no existe en el modelo Inmueble."
    except ObjectDoesNotExist:
        return f"No se encontró un inmueble con ID: {inmueble_id}"
    except Exception as e:
        return f"Ocurrió un error al actualizar el campo: {e}"
    

def borrar_inmueble(inmueble_id):
    try:
        Inmueble.objects.get(id=inmueble_id).delete()
        print(f"El inmueble '{inmueble_id}' ha sido eliminado con éxito.")
        return True
    except ObjectDoesNotExist:
        print(f"No se encontró un inmueble con ID: {inmueble_id}")
        return False
    except Exception as e:
        print(f"Ocurrió un error al eliminar el inmueble: {e}")
        return False


# usuario_marcos = crear_usuario(
#     nombres="Marcos",
#     apellidos="Jose",
#     rut="98765435",
#     direccion="Calle San Martín 123",
#     telefono="+56912345678",
#     tipo_usuario="arrendador",
#     correo_electronico="marcos.jose5@ejemplo.com",
#     password="11223344",
#     username="marcosjose5"
# )

# inmueble = crear_inmueble(
#     nombre="Departamento en Providencia",
#     direccion="Av. Andrés Bello 1500",
#     descripcion="Amplio departamento de 3 dormitorios",
#     imagen="departamento.jpg",
#     precio=1200000,
#     comuna="Providencia",
#     disponible=True,
#     m2_construidos=75,
#     m2_terreno=0,
#     cantidad_estacionamientos=1,
#     cantidad_habitaciones=3,
#     cantidad_banos=2,
#     tipo_de_inmueble="departamento",
#     propietario=usuario_marcos
# )