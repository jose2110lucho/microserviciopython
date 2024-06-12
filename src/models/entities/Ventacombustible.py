from utils.DateFormat import DateFormat

class Ventacombustible():

    def __init__(self,id,fecha=None,precio=None,cantidad=None,usuario_id=None)->None:
        self.id = id
        self.fecha = fecha
        self.precio = precio
        self.cantidad = cantidad
        self.usuario_id = usuario_id

    def to_JSON(self):
        return{
            'id':self.id,
            'fecha':DateFormat.convert_date(self.fecha),
            'precio':self.precio,
            'cantidad':self.cantidad,
            'usuario_id':self.usuario_id,
        }