from flask import Blueprint, jsonify, request
import uuid

#Entities
from models.entities.Ventaproducto import Ventaproducto
#Models
from models.VentaproductoModel import VentaproductoModel

main=Blueprint('ventaproducto_blueprint', __name__)

#------ruta para metodo GET ventaproducto-----------------------------------------------------------------------------
@main.route('/<id>')
def get_ventaproductos(id):
    try:
        ventaproductos=VentaproductoModel.get_ventaproductos(id)
        return jsonify(ventaproductos)
    except Exception as ex:
        return jsonify({'message':str(ex)}),500
#------ruta para metodo POST ventaproducto-----------------------------------------------------------------------------
@main.route('/add', methods=['POST'])
def add_ventaproductos():
    try:
        fecha = request.json['fecha']
        total_pagar = int(request.json['total_pagar']) 
        id = uuid.uuid4()
        ventaproducto = Ventaproducto(str(id), fecha, total_pagar)
        
        affected_row = VentaproductoModel.add_ventaproductos(ventaproducto)

        if affected_row == 1:
            return jsonify(ventaproducto.id)
        else:
             return jsonify({'message':"Error on insert data"}),500
        return jsonify({})
    except Exception as ex:
        return jsonify({'message':str(ex)}),500
#-----------------------------------------------------------------------------------