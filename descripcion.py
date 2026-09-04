class descripcion:
 def __init__(self , des_id , des_uuid, des_talla , des_color , des_pro_id):
     
     self.des_id     = des_id
     self.des_uuid   = des_uuid
     self.des_talla  = des_talla
     self.des_color  = des_color
     self.des_pro_id = des_pro_id
     
         
     def to_dict(self):
      return{
          
          'des_id'      :self.des_id,
          'des_uuid'    :self.des_uuid,  
          'des_talla'   :self.des_talla,
          'des_color'   :self.des_color,
          'des_pro_id'  :self.des_pro_id,
      }