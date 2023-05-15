from conexion import Conexion
from entidades.usuario import Usuario


class DT_Usuario:
    _INSERT = "INSERT INTO seguridad.usuario (clave, correo, id_pregunta, id_usuario, nombre, respuesta) values (%s, %s, %d, %d, %s, %s)"

    @classmethod
    def listarUsuario(cls):
        with Conexion.getConnection() as conexion:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT * FROM sermiccsa.usuario")
                resultado = cursor.fetchall()
                usuarios = []
                try:
                    for x in resultado:
                        u = Usuario(x['nombre'], x['correo'], x['id_pregunta'], x['id_usuario'],
                                     x['clave'],x['respuesta'])
                        usuarios.append(u)
                    print('usuarios', usuarios)
                    return usuarios
                except Exception as e:
                    print(f'Excepción {e}')

    @classmethod
    def guardarUsuario(cls, usuario):
        with Conexion.getConnection() as conexion:
            with conexion.cursor() as cursor:
                try:
                    print(f'Usuario a insertar: {usuario}')
                    valores = (usuario.contrasenia, usuario.correo, usuario.idUsuario, usuario.pregunta,usuario.nombre, usuario.respuesta)
                    cursor.execute(cls._INSERT, valores)
                    print(f'Usuario insertado: {usuario}')
                    conexion.commit()
                    return cursor.rowcount
                except Exception as e:
                    print(f'Exception {e}')

    #def autentificar_usuario(self):
        #with Conexion.getConnection() as conexion:
            #with conexion.cursor() as cursor


if __name__ == '__main__':
    #LISTAR USUARIOS
    users = DT_Usuario.listarUsuario()
    for x in users:
        print(x)