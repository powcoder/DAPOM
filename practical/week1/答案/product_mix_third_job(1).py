https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
#!/usr/bin/python

# This example  implements the product mix example of FP,
# Appendix 16.A. See eqs 16.107--16.113.

# Nicky van Foreest, 2019

%reset -f

from gurobipy import Model, GRB

m = Model("product mix")

# Set the lower bounds to 0 when we do not include the contractual
# obligations for product types 1 and 2.

x1 = m.addVar(lb=80, ub=100, name="x1")
x2 = m.addVar(lb=20, ub=50, name="x2")
x3 = m.addVar(lb=0, ub=20, name="x3")

m.setObjective(45 * x1 + 60 * x2 + (120 - 30) * x3, GRB.MAXIMIZE)

m.addConstr(15 * x1 + 10 * x2 + 10 * x3 <= 2400)
m.addConstr(15 * x1 + 35 * x2 + 5 * x3 <= 2400)
m.addConstr(15 * x1 + 5 * x2 + 18 * x3 <= 2400)
m.addConstr(25 * x1 + 14 * x2 + 10 * x3 <= 2400)

m.optimize()

for v in m.getVars():
    print("%s %g" % (v.varName, v.x))

print("Obj: %g" % m.objVal)
