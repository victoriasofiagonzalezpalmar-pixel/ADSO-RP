class pagos:
    def __init__(self, pag_id, pag_uuid, pag_monto, pag_metodo_transaccion):

        self.pag_id                 = pag_id
        self.pag_uuid               = pag_uuid
        self.pag_monto              = pag_monto
        self.pag_metodo_transaccion = pag_metodo_transaccion

    def to_dict(self):
        return {
            'pag_id'                 : self.pag_id,
            'pag_uuid'               : self.pag_uuid,
            'pag_monto'              : self.pag_monto,
            'pag_metodo_transaccion' : self.pag_metodo_transaccion
        }