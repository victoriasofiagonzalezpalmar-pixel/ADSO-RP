class datocliente:
    def __init__(self,dat_id,dat_uuid,dat_correo,dat_telefono,
                 dat_direccion,dat_cli_id):
        
        self.dat_id              = dat_id
        self.dat_uuid            = dat_uuid
        self.dat_correo          = dat_correo
        self.dat_telefono        = dat_telefono
        self.dat_direccion       = dat_direccion
        self.dat_cli_id          = dat_cli_id
        


    def to_dict(self):
        return{
            'dat_id'              : self.dat_id,
            'dat_uuid'            : self.dat_uuid,
            'dat_correo'          : self.dat_correo,
            'dat_telefono'        : self.dat_telefono,
            'dat_direccion'       : self.dat_direccion,
            'dat_cli_id'          : self.dat_cli_id
        }