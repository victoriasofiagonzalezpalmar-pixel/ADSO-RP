class realiza:
    def __init__(self , rea_id , rea_uuid , rea_cli_id , rea_dev_id):
    
        self.rea_id          =    rea_id
        self.rea_uuid        =    rea_uuid
        self.rea_cli_id      =    rea_cli_id
        self.rea_dev_id      =    rea_dev_id
    
    
    def to_dict(self):
        return{
            
            
            'rea_id'     :   self.rea_id,
            'rea_uuid'   :   self.rea_uuid,
            'rea_cli_id' :   self.rea_cli_id,
            'rea_dev_id' :   self.rea_dev_id
            }