from utils.DateFormat import DateFormat

class Ventaproducto():

    def __init__(self,id,fecha=None,total_pagar=None,usuario_id=None)->None:
        self.id = id
        self.fecha = fecha
        self.total_pagar = total_pagar
        self.usuario_id = usuario_id

    def to_JSON(self):
        return{
            'id':self.id,
            'fecha':DateFormat.convert_date(self.fecha),
            'total_pagar':self.total_pagar,
            'usuario_id':self.usuario_id,
        }