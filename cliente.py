class cliente:
    def __init__(self,cli_id,cli_uuid,cli_identificacion,cli_primer_nombre,
                 cli_segundo_nombre,cli_primer_apellido,cli_segundo_apellido):
        
        self.cli_id              = cli_id
        self.cli_uuid            = cli_uuid
        self.cli_identificacion  = cli_identificacion
        self.cli_primer_nombre   = cli_primer_nombre
        self.cli_segundo_nombre  = cli_segundo_nombre
        self.cli_primer_apellido = cli_primer_apellido
        self.cli_segundo_apellido= cli_segundo_apellido


    def to_dict(self):
        return{
            'cli_id'              : self.cli_id,
            'cli_uuid'            : self.cli_uuid,
            'cli_identificacion'  : self.cli_identificacion,
            'cli_primer_nombre'   : self.cli_primer_nombre,
            'cli_segundo_nombre'  : self.cli_segundo_nombre,
            'cli_primer_apellido' : self.cli_primer_apellido,
            'cli_segundo_apellido': self.cli_segundo_apellido
        }