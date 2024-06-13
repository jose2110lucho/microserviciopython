from flask import Blueprint, jsonify, request
import uuid

#Entities
from models.entities.Ventacombustible import Ventacombustible
#Models
from models.VentacombustibleModel import VentacombustibleModel

main=Blueprint('ventacombustible_blueprint', __name__)

#------ruta para metodo GET ventacombustible-----------------------------------------------------------------------------
@main.route('/')
def get_ventacombustibles():
    try:
        ventacombustibles=VentacombustibleModel.get_ventacombustibles()
        return jsonify(ventacombustibles)
    except Exception as ex:
        return jsonify({'message':str(ex)}),500
    
#-----------------------------------------------------------------------------
@main.route('/<id>')
def get_usuarioventacombustibles(id):
    try:
        ventacombustibles=VentacombustibleModel.get_usuarioventacombustibles(id)
        return jsonify(ventacombustibles)
    except Exception as ex:
        return jsonify({'message':str(ex)}),500
#------ruta para metodo POST ventacombustible-----------------------------------------------------------------------------
@main.route('/add', methods=['POST'])
def add_ventacombustibles():
    try:
        fecha = request.json['fecha']
        precio = int(request.json['precio'])
        cantidad = int(request.json['cantidad']) 
        id = uuid.uuid4()
        ventacombustible = Ventacombustible(str(id), fecha, precio , cantidad)
        
        affected_row = VentacombustibleModel.add_ventacombustibles(ventacombustible)

        if affected_row == 1:
            return jsonify(ventacombustible.id)
        else:
             return jsonify({'message':"Error on insert data"}),500
        return jsonify({})
    except Exception as ex:
        return jsonify({'message':str(ex)}),500
#-----------------------------------------------------------------------------------