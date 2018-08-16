class GetFormSchemaByEntity:
    
    def __init__(self, entity):
        self.entity = entity
        self.schema = {}
        self.schema['fields'] = []
    
    def build_form(self):
        for k in self.entity:
            print(k)

class FormAPI:
    
    def __init__(self, obj):
        self.obj = obj
        pass
    
    def _set_type(self, objtype):
        self.obj.type = objtype # entity type

    def _set_schema(self, schema):
        pass

    def _get_schema(self, schema):
        pass