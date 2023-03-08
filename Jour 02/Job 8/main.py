def alimentation (type,saison):
    if type == ("fruit"):
        if saison == ("ete"):
            return ("Poire, fraise, cassis")
        if saison == ("hiver"):
            return ("Orange, mandarine, kiwi")
    elif type == ("legume"):
        if saison == ("ete"):
            return ("Artichaut, aubergine,navet")
        if saison == ("hiver"):
            return ("Carotte, topinambour, endive")

print (alimentation ("fruit","ete"))
print (alimentation ("fruit","hiver"))
print (alimentation ("legume","ete"))
print (alimentation("legume","hiver"))