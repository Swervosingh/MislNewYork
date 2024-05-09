from flask import request, session
from flask_restful import Resource

# Local imports
from config import app, db, api
from models import Tshirt, Hoodie, Shastar

from flask_cors import CORS
from flask import request, jsonify





@app.route('/')
def index():
    return '<h1>Project Server</h1>'

@app.route('/tshirts', methods=['GET', 'POST'])
def tshirts():
    if request.method == 'GET':
        tshirts = Tshirt.query.all()
        tshirt_list = [tshirt.to_dict() for tshirt in tshirts]
        return jsonify(tshirt_list), 200
        
    elif request.method == 'POST':
        json_data = request.get_json()

        if not json_data:
            return jsonify({'error': 'No JSON data received'}), 400

        new_tshirt = Tshirt(
            name=json_data.get('name'),
            description=json_data.get('description'),
            image_url=json_data.get('image_url'),
            price=json_data.get('price')
        )
        try:
            db.session.add(new_tshirt)
            db.session.commit()
            return jsonify(new_tshirt.to_dict()), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500
    
    else:
        return 'Invalid request'

@app.route('/tshirts/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def tshirt(id):
    if request.method == 'GET':
        tshirt = Tshirt.query.filter(Tshirt.id == id).first()

        return tshirt.to_dict()
    
    elif request.method == 'PUT':
        tshirt = Tshirt.query.get(id)

        tshirt.name = request.form['name']
        tshirt.description = request.form['description']
        tshirt.image_url = request.form['image_url']
        tshirt.price = request.json.get('price', tshirt.price)
        
        db.session.commit()
        return jsonify(tshirt.to_dict())
    elif request.method == 'DELETE':
        tshirt = Tshirt.query.get(id)
        db.session.delete(tshirt)
        db.session.commit()
        return jsonify(tshirt.to_dict())
    else:   
        return 'Invalid request'

# Routes for Hoodies
@app.route('/hoodies', methods=['GET', 'POST'])
def hoodies():
    if request.method == 'GET':
        hoodies = Hoodie.query.all()
        hoodie_list = [hoodie.to_dict() for hoodie in hoodies]
        return jsonify(hoodie_list), 200
        
    elif request.method == 'POST':
        json_data = request.get_json()

        if not json_data:
            return jsonify({'error': 'No JSON data received'}), 400

        new_hoodie = Hoodie(
            name=json_data.get('name'),
            description=json_data.get('description'),
            image_url=json_data.get('image_url'),
            price=json_data.get('price')
        )
        try:
            db.session.add(new_hoodie)
            db.session.commit()
            return jsonify(new_hoodie.to_dict()), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500
    
    else:
        return 'Invalid request for Hoodies'

@app.route('/hoodies/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def hoodie(id):
    if request.method == 'GET':
        hoodie = Hoodie.query.get(id)
        if not hoodie:
            return jsonify({'error': 'Hoodie not found'}), 404
        return jsonify(hoodie.to_dict()), 200
    
    elif request.method == 'PUT':
        hoodie = Hoodie.query.get(id)
        if not hoodie:
            return jsonify({'error': 'Hoodie not found'}), 404
        
        json_data = request.get_json()

        if not json_data:
            return jsonify({'error': 'No JSON data received'}), 400

        hoodie.name = json_data.get('name', hoodie.name)
        hoodie.description = json_data.get('description', hoodie.description)
        hoodie.image_url = json_data.get('image_url', hoodie.image_url)
        hoodie.price = json_data.get('price', hoodie.price)
        
        try:
            db.session.commit()
            return jsonify(hoodie.to_dict()), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500
    
    elif request.method == 'DELETE':
        hoodie = Hoodie.query.get(id)
        if not hoodie:
            return jsonify({'error': 'Hoodie not found'}), 404

        db.session.delete(hoodie)
        db.session.commit()
        return jsonify(hoodie.to_dict()), 200
    
    else:
        return 'Invalid request'

# Routes for Shastars
@app.route('/shastars', methods=['GET', 'POST'])
def shastars():
    if request.method == 'GET':
        shastars = Shastar.query.all()
        shastar_list = [shastar.to_dict() for shastar in shastars]
        return jsonify(shastar_list), 200
        
    elif request.method == 'POST':
        json_data = request.get_json()

        if not json_data:
            return jsonify({'error': 'No JSON data received'}), 400

        new_shastar = Shastar(
            name=json_data.get('name'),
            description=json_data.get('description'),
            image_url=json_data.get('image_url'),
            price=json_data.get('price')
        )
        try:
            db.session.add(new_shastar)
            db.session.commit()
            return jsonify(new_shastar.to_dict()), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500
    
    else:
        return 'Invalid request for Shastars'

@app.route('/shastars/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def shastar(id):
    if request.method == 'GET':
        shastar = Shastar.query.get(id)
        if not shastar:
            return jsonify({'error': 'Shastar not found'}), 404
        return jsonify(shastar.to_dict()), 200
    
    elif request.method == 'PUT':
        shastar = Shastar.query.get(id)
        if not shastar:
            return jsonify({'error': 'Shastar not found'}), 404
        
        json_data = request.get_json()

        if not json_data:
            return jsonify({'error': 'No JSON data received'}), 400

        shastar.name = json_data.get('name', shastar.name)
        shastar.description = json_data.get('description', shastar.description)
        shastar.image_url = json_data.get('image_url', shastar.image_url)
        shastar.price = json_data.get('price', shastar.price)
        
        try:
            db.session.commit()
            return jsonify(shastar.to_dict()), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({'error': str(e)}), 500
    
    elif request.method == 'DELETE':
        shastar = Shastar.query.get(id)
        if not shastar:
            return jsonify({'error': 'Shastar not found'}), 404

        db.session.delete(shastar)
        db.session.commit()
        return jsonify(shastar.to_dict()), 200
    
    else:
        return 'Invalid request'

if __name__ == '__main__':
    app.run(port=5555, debug=True)