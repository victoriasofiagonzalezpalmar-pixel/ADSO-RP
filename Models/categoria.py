class categoria:

    def __init__(self,cat_id,cat_uuid,cat_nombre,cat_tipo,):

        self.cat_id     = cat_id
        self.cat_uuid   = cat_uuid
        self.cat_nombre = cat_nombre
        self.cat_tipo   = cat_tipo

    def to_dict(self):
        return{
            'cat_id'  : self.cat_id,
            'cat_uuid': self.cat_uuid,
            'cat_nombre': self.cat_nombre,
            'cat_tipo' : self.cat_tipo

        }