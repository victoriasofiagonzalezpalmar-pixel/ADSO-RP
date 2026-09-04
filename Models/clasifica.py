class clasifica:

    def __init__(self,cla_id,cla_uuid,cla_pro_id,cla_cat_id):

        self.cla_id     = cla_id
        self.cla_uuid   = cla_uuid
        self.cla_pro_id = cla_pro_id
        self.cla_cat_id = cla_cat_id


    def to_dict(self):
        return{
            'cla_id'     : self.cla_id,
            'cla_uuid'   : self.cla_uuid,
            'cla_pro_id' : self.cla_pro_id,
            'cla_cat_id' : self.cla_cat_id


        }