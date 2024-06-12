from database.db import get_connection
from .entities.Ventaproducto import Ventaproducto
from .entities.Producto import Producto
from .entities.Detallenotaventa import Detallenotaventa
import json
from utils.DateFormat import DateFormat



class VentaproductoModel():

#---------------------------------------------------------------------------------------------------------------------------    
#API metodo GET , devuelve una lista con todas las ventas de productos    
    @classmethod
    def get_ventaproductos(self,id):
        try:
            connection=get_connection()
            productos=[]

            with connection.cursor() as cursor:
                cursor.execute("SELECT fecha, total_pagar FROM ventaproducto WHERE id=%s",(id,))
                row = cursor.fetchone()

                if row != None:
                     cursor.execute("SELECT producto.nombre ,detallenotaventa.cantidad, detallenotaventa.sub_total FROM detallenotaventa JOIN producto ON detallenotaventa.producto_id=producto.id  WHERE ventaproducto_id=%s", (id,))
                     detallenotaventas = cursor.fetchall()
                     for detalle in detallenotaventas:
                        
                            productos.append(
                                {
                                    "nombre": detalle[0],
                                    "cantidad": detalle[1], 
                                    "sub_total": detalle[2],
                                }
                            )

                     data = {
                            "fecha": DateFormat.convert_date(row[0]),
                            "total_pagar": row[1],
                            "productos": productos
                        }   
                     print(data)  
                else:  
                     data = {}
            connection.close()
            return data
        except Exception as ex:
            raise Exception(ex)
        
#----------------------------------------------------------------------------------------------------------------------------
    @classmethod
    def add_ventaproductos(self, ventaproducto):
            try:
                connection=get_connection()
                #ventacombustibles=[]

                with connection.cursor() as cursor:
                    cursor.execute(" INSERT INTO ventaproducto (id, fecha, total_pagar, usuario_id) VALUES (%s, %s, %s, %s) ", (ventaproducto.id, ventaproducto.fecha, ventaproducto.total_pagar, ventaproducto.usuario_id))
                    
                    affected_rows = cursor.rowcount
                    connection.commit()

                connection.close()
                return affected_rows
            except Exception as ex:
                raise Exception(ex) 
#----------------------------------------------------------------------------------------------------------------------------
   

    