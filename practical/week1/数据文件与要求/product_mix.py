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

x1 = m.addVar(ub=100, name="x1")
x2 = m.addVar(ub=50, name="x2")

m.setObjective(45 * x1 + 60 * x2, GRB.MAXIMIZE)

m.addConstr(15 * x1 + 10 * x2 <= 2400)
m.addConstr(15 * x1 + 35 * x2 <= 2400)
m.addConstr(15 * x1 + 5 * x2 <= 2400)
m.addConstr(25 * x1 + 14 * x2 <= 2400)

m.optimize()

for v in m.getVars():
    print("%s %g" % (v.varName, v.x))

print("Obj: %g" % m.objVal)
