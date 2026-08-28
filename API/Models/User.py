class User:

    def __init__(self, US_ID, US_UUID, US_FIRST_NAME, US_LAST_NAME, US_TYPE_DOC, US_DOCUMENT, US_DATE_BIRTH):
        self.US_ID          = US_ID
        self.US_UUID        = US_UUID
        self.US_FIRST_NAME  = US_FIRST_NAME
        self.US_LAST_NAME   = US_LAST_NAME
        self.US_TYPE_DOC    = US_TYPE_DOC
        self.US_DOCUMENT    = US_DOCUMENT
        self.US_DATE_BIRTH  = US_DATE_BIRTH


    def to_dict(self):
        return {
            'US_ID'         : self.US_ID,
            'US_UUID'       : self.US_UUID,
            'US_FIRST_NAME' : self.US_FIRST_NAME,
            'US_LAST_NAME'  : self.US_LAST_NAME,
            'US_TYPE_DOC'   : self.US_TYPE_DOC,
            'US_DOCUMENT'   : self.US_DOCUMENT,
            'US_DATE_BIRTH': self.US_DATE_BIRTH
        }

# Esta clase representa un usuario y tiene un método to_dict() que devuelve un diccionario
# con los atributos del usuario.

