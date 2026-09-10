class Proveedor:
    def __init__(self, edor_id, edor_uuid, edor_nit, edor_nombre):
        self.edor_id         = edor_id
        self.edor_uuid       = edor_uuid
        self.edor_nit        = edor_nit
        self.edor_nombre     = edor_nombre
        
    def to_dict(self):
        return {
            'edor_id'        : self.edor_id,
            'edor_uuid'      : self.edor_uuid,
            'edor_nit'       : self.edor_nit,
            'edor_nombre'    : self.edor_nombre
        }