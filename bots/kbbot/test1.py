import sys
from kb import KB, Boolean, Integer, Constant

# Define our symbols
A = Boolean('A')
B = Boolean('B')
C = Boolean('C')
D = Boolean('D')

# Create a new knowledge base
kb = KB()

# Add clauses
# kb.add_clause(A, B, C)
# kb.add_clause(~A, B)
# kb.add_clause(C)
# kb.add_clause(C)

# # Question 3
# kb.add_clause(A)
# kb.add_clause(C)
# kb.add_clause(D)
# kb.add_clause(~A)

# Question 4
kb.add_clause(A, B)
kb.add_clause(B, ~C)
kb.add_clause(~C, ~A)


# This needs to be unsatisfiable for entailment 
kb.add_clause(A, ~B)
kb.add_clause(~A, B)



# Print all models of the knowledge base
for model in kb.models():
    print(model)

# Print out whether the KB is satisfiable (if there are no models, it is not satisfiable)
print("It is satisfiable" if kb.satisfiable() else "It is not satisfiable")
