
class Producto():

    def __init__(self,id,nombre=None,estado=None,precio_compra=None, precio_venta=None)->None:
        self.id = id
        self.nombre = nombre
        self.estado = estado
        self.precio_compra = precio_compra
        self.precio_venta = precio_venta


    def to_JSON(self):
        return{
            'id':self.id,
            'nombre':self.nombre,
            'estado':self.estado,
            'precio_compra':self.precio_compra,
            'precio_venta':self.precio_venta,
        }