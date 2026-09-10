class Datoproveedor:
    def __init__(self, ato_id, ato_uuid, ato_telefono, ato_correo, ato_pro_id):
        self.ato_id         = ato_id
        self.ato_uuid       = ato_uuid
        self.ato_telefono   = ato_telefono
        self.ato_correo     = ato_correo
        self.ato_pro_id     = ato_pro_id
        
    def to_dict(self):
        return {
            'ato_id'         : self.ato_id,
            'ato_uuid'       : self.ato_uuid,
            'ato_telefono'   : self.ato_telefono,
            'ato_correo'     : self.ato_correo,
            'ato_pro_id'     : self.ato_pro_id
        }