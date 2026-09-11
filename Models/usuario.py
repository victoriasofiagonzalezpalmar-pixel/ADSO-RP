class usario:
    def __init__(self,usu_id,usu_uuid,usu_cedula, usu_nombre, usu_apellido,
                  usu_contrasena):
        
        self.usu_id         = usu_id
        self.usu_uuid       = usu_uuid
        self.usu_cedula     = usu_cedula
        self.usu_nombre     = usu_nombre
        self.usu_apellido   = usu_apellido
        self.usu_contrasena = usu_contrasena
        
    def to_dict(self):
        return {
            'usu_id'        : self.usu_id,
            'usu_uuid'      : self.usu_uuid,
            'usu_cedula'    : self.usu_cedula,
            'usu_nombre'    : self.usu_nombre,
            'usu_apellido'  : self.usu_apellido,
            'usu_contrasena': self.usu_contrasena
        }