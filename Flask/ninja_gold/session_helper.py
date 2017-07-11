from flask import session
import json

class SessionHelper(object):
  
    def save(self, name):
        session[name] = self
        return self

    # def toJson(self):
    #     try:
    #         return json.dumps(self.__dict__)
    #     except:
    #         try:
    #             return json.dumps([x.__dict__ for x in self])
    #         except:
    #             return 'Could not convert to json'
        

        
        
    
