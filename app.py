from flask import Flask, jsonify,request
import os

app = Flask(__name__)

from pet import pets
from user import users

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

#METODOS MASCOTAS

@app.route('/pet', methods=['GET'])
def getAllPets():
    return jsonify(pets)

@app.route('/pet/<int:pet_id>',methods=['GET'])
def getPetById(pet_id):
    petFound = [pet for pet in pets if pet['id'] == pet_id]

    if (len(petFound)>0):
        return jsonify(petFound[0])
    return jsonify({'mensaje':'Mascota no encontrada'})

@app.route('/pet', methods=['POST'])
def addPet():
    new_pet = {
        "id": request.json['id'],
        "category": request.json['category'],
        "name": request.json['name'],
        "photoUrls":request.json['photoUrls'],
         "tags":request.json['tags'],
         "status":request.json['status']
    }

    pets.append(new_pet)
    return jsonify({"message":"Mascota agregada correctamane", "pet":new_pet})

@app.route('/pet/<int:pet_id>', methods=['PUT'])
def updatePet(pet_id):
    petFound = [pet for pet in pets if pet['id'] == pet_id]
    if (len(petFound)>0):
        petFound[0]['category']=request.json['category']
        petFound[0]['name']=request.json['name']
        petFound[0]['photoUrls']=request.json['photoUrls']
        petFound[0]['tags']=request.json['tags']
        petFound[0]['status']=request.json['status']

        return jsonify({"message":"Mascota actulizada correctamente",
        "pet":petFound[0]})
    return jsonify({"message":"No fue posible actualizar la mascota"})

@app.route('/pet/<int:pet_id>', methods=['DELETE'])
def deletePet(pet_id):
    petFound = [pet for pet in pets if pet['id'] == pet_id]
    if (len(petFound)>0):
        pets.remove(petFound[0])
        
        return jsonify({"message":"Mascota eliminada correctamente",
        "pets":pets})
    return jsonify({"message":"Error al eliminar la mascota del registro"})

@app.route('/pet/findByStatus', methods=['GET'])
def getByPetStatus():

    if "status" in request.args:
        status=request.args.get("status")

    petsFound = [pet for pet in pets if pet['status'] == status]

    if (len(petsFound)>0):
        return jsonify({"message":"pets","pets":petsFound})
    return jsonify({"message":"Error al encontrar las mascotas"})

@app.route('/pet/<int:pet_id>',methods=['POST'])
def updatePetForm(pet_id):
    petFound = [pet for pet in pets if pet['id'] == pet_id]
    if (len(petFound)>0):
        petFound[0]['name']=request.json['name']
        petFound[0]['status']=request.json['status']

        return jsonify({"message":"Mascota actualizada correctamente",
        "pet":petFound[0]}) 
    return jsonify({"message":"No fue posible actualizar la mascota"})

@app.route('/pet/<int:pet_id>/uploadImage', methods=['POST'])
def uploapPetImage(pet_id):

    petFound = [pet for pet in pets if pet['id'] == pet_id]

    if (len(petFound)>0):
        target=os.path.join(APP_ROOT,'images')

        print(target)

        if not os.path.isdir(target):
            os.mkdir(target)
        
        for file in request.files.getlist("file"):
            filename=file.filename
            destination="/".join([target,filename])
            print(destination)
            petFound[0]['photoUrls'].append(destination)
            file.save(destination)
        return jsonify({"message":"La imagen fue cargada correctamente",
        "pet":petFound[0]})
    return jsonify({"message":"Error al cargar imagen"})

#METODOS USUARIOS

@app.route('/user', methods=['GET'])
def getAllUsers():
    return jsonify(users)

@app.route('/user/<int:user_id>',methods=['GET'])
def getUserById(pet_id):
    userFound = [user for user in users if user['id'] == user_id]

    if (len(userFound)>0):
        return jsonify(userFound[0])
    return jsonify({'mensaje':'Usuario no encontrado'})

@app.route('/user', methods=['POST'])
def addUser():
    new_user = {
        "id": request.json['id'],
        "username": request.json['username'],
        "firstName": request.json['firstName'],
        "lastName": request.json['lastName'],
        "email": request.json['email'],
        "password": request.json['password'],
        "phone": request.json['phone'],
        "userStatus": request.json['userStatus']
    }
    users.append(new_users)
    return jsonify({"message":"Usuario agregado correctamente", "user":new_user})

@app.route('/user/<int:user_id>', methods=['PUT'])
def updateUser(user_id):
    userFound = [user for user in userss if user['id'] == user_id]
    if (len(userFound)>0):
        userFound[0]['id']=request.json['id']
        userFound[0]['username']=request.json['username']
        userFound[0]['firstName']=request.json['firstName']
        userFound[0]['lastName']=request.json['lastName']
        userFound[0]['email']=request.json['email']
        userFound[0]['password']=request.json['password']
        userFound[0]['phone']=request.json['phone']
        userFound[0]['userStatus']=request.json['userStatus']

        return jsonify({"message":"Usuario actualizado correctamente",
        "user":userFound[0]})
    return jsonify({"message":"No fue posible actualizar el usuario"})

@app.route('/user/<int:user_id>', methods=['DELETE'])
def deleteUser(user_id):
    userFound = [user for user in users if user['id'] == user_id]
    if (len(userFound)>0):
        users.remove(userFound[0])
        
        return jsonify({"message":"Usuario eliminado correctamente",
        "users":users})
    return jsonify({"message":"Error al eliminar al usuario del registro"})

@app.route('/user/findByStatus', methods=['GET'])
def getByUserStatus():

    if "userStatus" in request.args:
        userStatus=request.args.get("userStatus")

    userFound = [user for user in users if user['userStatus'] == userStatus]

    if (len(usersFound)>0):
        return jsonify({"message":"users","users":petsFound})
    return jsonify({"message":"Error al buscar usuario"})

@app.route('/user/<int:user_id>',methods=['POST'])
def updateUserForm(user_id):
    userFound = [user for user in users if user['id'] == user_id]
    if (len(userFound)>0):
        userFound[0]['username']=request.json['username']
        userFound[0]['userStatus']=request.json['userStatusStatus']

        return jsonify({"message":"Usuario actualizado correctamente",
        "user":petFound[0]}) 
    return jsonify({"message":"No fue posible actualizar el usuario"})

@app.route('/user/<int:user_id>/uploadImage', methods=['POST'])
def uploadUserImage(user_id):

    userFound = [user for user in users if user['id'] == user_id]

    if (len(userFound)>0):
        target=os.path.join(APP_ROOT,'images')

        print(target)

        if not os.path.isdir(target):
            os.mkdir(target)
        
        for file in request.files.getlist("file"):
            filename=file.filename
            destination="/".join([target,filename])
            print(destination)
            userFound[0]['photoUrls'].append(destination)
            file.save(destination)
        return jsonify({"message":"La imagen fue cargada correctamente",
        "user":userFound[0]})
    return jsonify({"message":"Error al cargar imagen"})

if __name__=='__main__':
    app.run(debug=True, port=8080)