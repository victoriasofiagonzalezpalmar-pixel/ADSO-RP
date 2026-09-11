class producto:
    def __init__(self,pro_id,pro_uuid,pro_cofigo,pro_nombre,pro_pricio,pro_stock,
                 pro_edor_id):

        self.pro_id      = pro_id
        self.pro_uuid    = pro_uuid
        self.pro_cofigo  = pro_cofigo
        self.pro_nombre  = pro_nombre
        self.pro_pricio  = pro_pricio
        self.pro_stock   = pro_stock
        self.pro_edor_id = pro_edor_id

    def to_dict(self):
        return{
            'pro_id'      : self.pro_id,
            'pro_uuid'    : self.pro_uuid,
            'pro_cofigo'  : self.pro_cofigo,
            'pro_nombre'  : self.pro_nombre,
            'pro_pricio'  : self.pro_pricio,
            'pro_stock'   : self.pro_stock,
            'pro_edor_id' : self.pro_edor_id

        }