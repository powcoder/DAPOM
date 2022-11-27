https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder
"""

With this example we compute the minimally required capacity to
satisfy all demand for the product mix example of FP, Appendix 16.A.
See eqs 16.107--16.113.


Petra de Jonge, Nicky van Foreest, 2019

"""

%reset -f

from gurobipy import Model, GRB

m = Model("product mix")


x1 = m.addVar(name="x1")
x2 = m.addVar(name="x2")
c1 = m.addVar(name="c1")
c2 = m.addVar(name="c2")
c3 = m.addVar(name="c3")
c4 = m.addVar(name="c4")

m.setObjective(c1 + c2 + c3 + c4, GRB.MINIMIZE)

m.addConstr(15 * x1 + 10 * x2 <= c1)
m.addConstr(15 * x1 + 35 * x2 <= c2)
m.addConstr(15 * x1 + 5 * x2 <= c3)
m.addConstr(25 * x1 + 14 * x2 <= c4)
m.addConstr(x1 >= 100)
m.addConstr(x2 >= 50)

# Of course we could have absorbed the constraints on x1 and x2 in the
# functions addVar above. Here we implemented it as explicit
# constraints to make the shift in interpretation of the problem
# explicit.


m.optimize()

for v in m.getVars():
    print("%s %g" % (v.varName, v.x))

print("Obj: %g" % m.objVal)
