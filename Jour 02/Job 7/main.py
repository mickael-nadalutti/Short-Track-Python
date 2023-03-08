def qui_suis_je (langage):
    if langage == ("javascript"):
        return ("Tu es developpeur web")
    elif langage == ("python"):
        return ("Tu es developpeur IA")
    elif langage == ("java"):
        return ("Tu es developpeur logiciel")
    elif langage == ("reactjs"):
        return ("Tu es developpeur mobile")
    else :
        return ("Un jour je serai le meilleur developpeur ...")

print (qui_suis_je ("javascript"))
print (qui_suis_je ("python"))
print (qui_suis_je ("java"))
print (qui_suis_je ("reactjs"))
print (qui_suis_je (""))

