from database.db import get_connection
from .entities.Ventacombustible import Ventacombustible

class VentacombustibleModel():

#---------------------------------------------------------------------------------------------------------------------------    
#API metodo GET , devuelve una lista con todas las ventas de combustible    
    @classmethod
    def get_ventacombustibles(self):
        try:
            connection=get_connection()
            ventacombustibles=[]

            with connection.cursor() as cursor:
                cursor.execute("SELECT id, fecha, precio, cantidad, usuario_id FROM ventacombustible")
                resultset=cursor.fetchall()

                for row in resultset:
                    ventacombustible=Ventacombustible(row[0],row[1],row[2],row[3],row[4],)
                    ventacombustibles.append(ventacombustible.to_JSON())
            connection.close()
            return ventacombustibles
        except Exception as ex:
            raise Exception(ex)

#-----------------------------------------------------------------------------------------------------
    @classmethod
    def get_usuarioventacombustibles(self,id):
            try:
                connection=get_connection()
                lista_ventas_combustible_usuario=[]

                with connection.cursor() as cursor:
                    cursor.execute("SELECT id, fecha, precio, cantidad, usuario_id FROM ventacombustible WHERE ventacombustible.usuario_id =  %s", (id,))
                    resultset=cursor.fetchall()

                    for row in resultset:
                        usuarioventacombustible=Ventacombustible(row[0],row[1],row[2],row[3],row[4],)
                        lista_ventas_combustible_usuario.append(usuarioventacombustible.to_JSON())
                connection.close()
                return lista_ventas_combustible_usuario
            except Exception as ex:
                raise Exception(ex)

#----------------------------------------------------------------------------------------------------------------------------
    @classmethod
    def add_ventacombustibles(self, ventacombustible):
            try:
                connection=get_connection()
                #ventacombustibles=[]

                with connection.cursor() as cursor:
                    cursor.execute(" INSERT INTO ventacombustible (id, fecha, precio , cantidad ,usuario_id) VALUES (%s, %s, %s, %s, %s) ", (ventacombustible.id, ventacombustible.fecha, ventacombustible.precio, ventacombustible.cantidad, ventacombustible.usuario_id))
                    
                    affected_rows = cursor.rowcount
                    connection.commit()

                connection.close()
                return affected_rows
            except Exception as ex:
                raise Exception(ex) 
#----------------------------------------------------------------------------------------------------------------------------

