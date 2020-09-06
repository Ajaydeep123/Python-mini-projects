#apni dictionary

world = {"india": "meri matrabhoomi"
          ,"bundelkhand" : "meri janmbhooi"
          ,"greater noida" : "meri karmbhoomi"}
print("swagat hai aapka, bataiye kaise sahayta kar skta hu:")
sawal = input()
if sawal in world:
    print("Apke sawal ka jawab hai:-",(world[sawal]))
else:
    print("maaf kariye")