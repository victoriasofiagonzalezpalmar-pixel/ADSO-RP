class almacena:
    def __init__(self,alm_id,alm_uuid,alm_cantidad,alm_com_id,alm_pro_id):
        self.alm_id         = alm_id
        self.alm_uuid       = alm_uuid
        self.alm_cantidad   = alm_cantidad
        self.alm_com_id     = alm_com_id
        self.alm_pro_id     = alm_pro_id
        
    def to_dict(self):
        return {
            'alm_id'         : self.alm_id,
            'alm_uuid'       : self.alm_uuid,
            'alm_cantidad'   : self.alm_cantidad,
            'alm_com_id'     : self.alm_com_id,
            'alm_pro_id'     : self.alm_pro_id
        }