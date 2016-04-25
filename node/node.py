# Copyright (c) GearDragon Software 2016
class __Node__(object):
    def __init__(self, value="null", **kwargs):
        self.value = value
        for kw, arg in kwargs.items():
            setattr(self, kw, arg)
    
    def __repr__(self):
        return repr([self.value])
    
    def hierarchy(self):
        result = self
        # TODO: Get code from home
        return result
