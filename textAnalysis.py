import nltk
from nltk.tokenize import sent_tokenize


def TextPosTagger(text1):
    text=text1.replace("She","Alice")
    elements=list()
    datatosend=""
    action=""
    actor=""
    objet=""
    weather=""
    sentences = sent_tokenize(text)
    for sent in sentences:
        tokens = nltk.word_tokenize(sent)
        tags=nltk.pos_tag(tokens)
        print("my sentence: ",tags)
        for tag in tags:
            if "NN" in tag[1] and actor=="" :
                actor=tag[0]
                
            if "VB" in tag[1]:
                action=tag[0]
                if "ran" in action or "running" in action:
                    action="run"
                if "trip" in action:
                    action="trip"
                if "walk" in action :
                    action="walk"
                if "kneel" in action or "knelt" in action:
                    action="kneele"
                if "slep" in action or "sleep" in action:
                    action="sleep"
                if "cri" in action or "cry" in action:
                    action="cry"
                if "stop" in action or "stand" in action or "was" in action or "is" in action or "feels" in action:
                    action="stand"
                                 
                
            if ("NN" in tag[1] or "JJ" in tag [1]) and action!="" and actor!="" :
                objet=tag[0]
                if action=="stand":
                    if objet=="angry":
                        action="angry"
                    if objet=="happy" or objet=="joyful":
                        action="happy"
                    if objet=="dizzy":
                        action="dizzy"
        
        
        
        elements.append("["+actor+"]"+"("+action+")"+"{"+objet+"}")
        actor,action,objet="","",""
    for elem in elements:
        if datatosend=="":
            datatosend=elem
        else:
            datatosend=datatosend+","+elem
        print(elem)
    print(datatosend)
    
    return datatosend


