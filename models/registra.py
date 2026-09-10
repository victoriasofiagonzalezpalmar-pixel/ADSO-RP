class rejistra:
    def __init__(self,rej_id,rej_uuid,rej_usu_id,rej_com_id):
    
          self.rej_id          =     rej_id
          self.rej_uuid        =    rej_uuid
          self.rej_usu_id      =    rej_usu_id
          self.rej_com_id      =    rej_com_id
    
    
    def to_dict(self):
        return{
            
           'rej_id'     :   self.rej_id,
           'rej_uuid'   :   self.rej_uuid,
           'rej_usu_id' :   self.rej_usu_id,
           'rej_com_id' :   self.rej_com_id,
                        
                        
        }