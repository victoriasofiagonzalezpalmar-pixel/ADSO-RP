class compra:
    def __init__(self, com_id, com_uuid, com_numero_compra, com_monto_total,
                  com_fecha_compra, com_pag_id, com_cli_id):

        self.com_id              = com_id
        self.com_uuid            = com_uuid
        self.com_numero_compra   = com_numero_compra
        self.com_monto_total     = com_monto_total
        self.com_fecha_compra    = com_fecha_compra
        self.com_pag_id          = com_pag_id
        self.com_cli_id          = com_cli_id


    
    def to_dict(self):
        return {
            'com_id'             : self.com_id,
            'com_uuid'           : self.com_uuid,
            'com_numero_compra'  : self.com_numero_compra,
            'com_monto_total'    : self.com_monto_total,
            'com_fecha_compra'   : self.com_fecha_compra,
            'com_pag_id'         : self.com_pag_id,
            'com_cli_id'         : self.com_cli_id
        }