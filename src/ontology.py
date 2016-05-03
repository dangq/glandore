from owlready import *


onto = Ontology("http://vsources.org/onto.owl")
onto_path.append("./")

class Drug(Thing):
   ontology=onto
class Ingredient(Thing):
   ontology=onto
class has_for_ingredient(Property):
    ontology=onto
    domain   = [Drug]
    range    = [float]


my_drug = Drug("my_drug")
#acetaminophen = Ingredient(0.4)

my_drug.has_for_ingredient.append(0.4)
onto.save()