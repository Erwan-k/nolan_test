from flask_restful import Resource, reqparse

get_params = reqparse.RequestParser()
get_params.add_argument("nom",type=str,required=True)
put_params = reqparse.RequestParser()
put_params.add_argument("ancien_nom",type=str,required=True)
put_params.add_argument("nouveau_nom",type=str,required=True)
delete_params = reqparse.RequestParser()
delete_params.add_argument("nom",type=str,required=True)

liste = []

class nom(Resource): 
	
	def get(self):
		global liste
		return liste

	def post(self):
		global liste
		body = get_params.parse_args()
		[nom] = [body[i] for i in body]

		liste += [nom]

		return {"retour":"ok"}

	def put(self):
		global liste
		body = put_params.parse_args()
		[ancien_nom, nouveau_nom] = [body[i] for i in body]

		nouvelle_liste = []
		for i in liste:
			if i == ancien_nom:
				nouvelle_liste += [nouveau_nom]
			else:
				nouvelle_liste += [i]
		liste = nouvelle_liste

		return {"retour":"ok"}

	def delete(self):
		global liste
		body = delete_params.parse_args()
		[nom] = [body[i] for i in body]

		nouvelle_liste = []
		for i in liste:
			if i != nom:
				nouvelle_liste += [i]
		liste = nouvelle_liste

		return {"retour":"ok"}




