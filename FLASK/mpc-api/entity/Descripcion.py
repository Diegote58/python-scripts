class Description:
	def __init__(this, movil, empresa, velocidad, direccion,lastUpdate):    
		this.movil = movil
		this.empresa = empresa
		this.velocidad = velocidad
		this.direccion = direccion
		this.lastUpdate	= lastUpdate
		

def description_creator(map):
	return Description(map['movil'],map['empresa'],map['velocidad'],map['direccion'],map['ultima transmision'])
	
	