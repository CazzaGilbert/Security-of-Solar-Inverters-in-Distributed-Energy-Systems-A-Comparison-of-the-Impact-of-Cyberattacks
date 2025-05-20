from config import DEFENCES

class Method: # get data on defence method chosen
    def __init__(self, name, level): # initialise 
        levels = DEFENCES[name].get("levels")
        data = levels[level]
        cost = data['cost']
        
        # attributes
        self.name = name
        self.level = level
        self.description = data['description']
        self.mitigates = data['mitigates']
        self.cost = cost

class Inverter: # instance of a base inverter that can allow for defence methods to be used to stop cyber attacks
    def __init__(self): # initialise
        self.defences = []
        self.total_cost = 0

    def implementDefence(self, method, level): # add security method to inverter
        security_feature = Method(method, level)
        self.defences.append(security_feature)
        self.total_cost += security_feature.cost