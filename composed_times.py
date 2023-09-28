from utils import *



class ComposedTime:
    utils = Utils()
    def __init__(self, verb:str):
        self.verb = verb
    def getAuxilliary(self, time:str, person:int):
        auxilliary = ""
        utils = ComposedTime.utils
        time = time.upper()
        if type(person) == int:
            match person:
                case 1:  
                    if time == utils.PASSE_COMPOSE:
                        auxilliary = "ai"
                    elif time == utils.PLUS_QUE_PARFAIT:
                        auxilliary = "avais"
                    elif time == utils.FUTUR_ANTERIEUR_DU_PASSE:
                        auxilliary = "aurais"
                    elif time == utils.FUTURE_ANTERIEUR:
                        auxilliary = "aurai"
                    else: 
                        auxilliary = "eus"   
                    
                case 2:
                        if time == utils.PASSE_COMPOSE:
                            auxilliary = "as"
                        elif time == utils.PLUS_QUE_PARFAIT:
                            auxilliary = "avais"
                        elif time == utils.FUTUR_ANTERIEUR_DU_PASSE:
                            auxilliary = "aurais"
                        elif time == utils.FUTURE_ANTERIEUR:
                            auxilliary = "auras"
                        else: 
                            auxilliary = "eus" 
                case 3:
                        if time == utils.PASSE_COMPOSE:
                            auxilliary = "a"
                        elif time == utils.PLUS_QUE_PARFAIT:
                            auxilliary += "avait"
                        elif time == utils.FUTUR_ANTERIEUR_DU_PASSE:
                            auxilliary = "aurait"
                        elif time == utils.FUTURE_ANTERIEUR:
                            auxilliary = "aura"
                        else: 
                            auxilliary = "eut" 
                case 4:
                        if time == utils.PASSE_COMPOSE:
                            auxilliary = "avons"
                        elif time == utils.PLUS_QUE_PARFAIT:
                            auxilliary = "avions"
                        elif time == utils.FUTUR_ANTERIEUR_DU_PASSE:
                            auxilliary = "aurions"
                        elif time == utils.FUTURE_ANTERIEUR:
                            auxilliary = "auront"
                        else: 
                            auxilliary = "eûmes" 
                case 5:
                        if time == utils.PASSE_COMPOSE:
                            auxilliary = "avez"
                        elif time == utils.PLUS_QUE_PARFAIT:
                            auxilliary = "aviez"
                        elif time == utils.FUTUR_ANTERIEUR_DU_PASSE:
                            auxilliary = "aurions"
                        elif time == utils.FUTURE_ANTERIEUR:
                            auxilliary = "aurons"
                        else: 
                            auxilliary = "eûtes" 
                case 6:
                        if time == utils.PASSE_COMPOSE:
                            auxilliary = "ont"
                        elif time == utils.PLUS_QUE_PARFAIT:
                            auxilliary = "avaeint"
                        elif time == utils.FUTUR_ANTERIEUR_DU_PASSE:
                            auxilliary = "auraient"
                        elif time == utils.FUTURE_ANTERIEUR:
                            auxilliary = "auront"
                        else: 
                            auxilliary = "eûssent" 
                case _:
                    return "-"
            
        return auxilliary
        
    def conjugateTime(self,  time:str, ):
        self.verb = self.verb.lower()
        utils = ComposedTime.utils
        pastParticiple = ComposedTime.utils.verbPastParticiple(verb=self.verb)
        print(time)
        print()
        for i in range (len(utils.personal_pronouns)):
            pronoun = utils.personal_pronouns[i]
            auxilliary = self.getAuxilliary(person=i+1, time=time)           
            if(i==0):
               pronoun = "J'"
            print(pronoun + " " + auxilliary + " " + pastParticiple)
        print("-"*15)
        print()

    def conjugateAllTimes(self):
        print("LES TEMPS COMPOSES")
        print(' - '*15)
        print()
        for time in ComposedTime.utils.COMPOSED_TIMES:
            self.conjugateTime(time=time)
        print('*'*20)