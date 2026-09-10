class devolucion:
    def __init__(self , dev_id , dev_uuid, dev_estado_producto , dev_motivos ,
                  dev_tipo_producto , dev_fecha_devolucion):

          self.dev_id                 = dev_id
          self.dev_uuid               = dev_uuid
          self.dev_estado_producto    = dev_estado_producto
          self.dev_motivos            = dev_motivos
          self.dev_tipo_producto      = dev_tipo_producto
          self.dev_fecha_devolucion   = dev_fecha_devolucion
    
    
    def to_dict(self):
        return{
             'dev_id'               : self.dev_id,
             'dev_uuid'             : self.dev_uuid,
             'dev_estado_producto'  : self.dev_estado_producto,
             'dev_motivos'          : self.dev_motivos,
             'dev_tipo_producto'    : self.dev_tipo_producto,
             'dev_fecha_devolucion' : self.dev_fecha_devolucion
             }