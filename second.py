from cadabra2 import *

Indices(Ex(r'''{a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z#}'''), Ex(r'''fourD, position=independent''') )

KroneckerDelta(Ex(r'''\delta{#}'''), Ex(r'''''') )
Symmetric(Ex(r'''g_{a b}'''), Ex(r'''''') )
Symmetric(Ex(r'''g^{a b}'''), Ex(r'''''') )
Symmetric(Ex(r'''\eta_{a b}'''), Ex(r'''''') )
Symmetric(Ex(r'''\eta^{a b}'''), Ex(r'''''') )
Symmetric(Ex(r'''h^{a b}'''), Ex(r'''''') )

PartialDerivative(Ex(r'''\partial{#}'''), Ex(r'''''') )
Depends(Ex(r'''g{#}'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''h{#}'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''G{#}'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''\Gamma{#}'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''R{#}'''), Ex(r'''\partial{#})''') )

Weight(Ex(r'''h{#}'''), Ex(r'''label=l, value=1'''))
WeightInherit(Ex(r'''\partial{#}'''), Ex(r'''label=all, type=multiplicative'''))

ruleMetricUp = Ex(r'''g^{a b} -> \eta^{a b} + h^{a b}''')
ruleMetricDown = Ex(r'''g_{a b} -> \eta_{a b} - \eta_{a p} \eta_{b q} h^{p q}''')

ruleChristoffel = Ex(r'''\Gamma^{a}_{b c} -> 1/2 g^{a p} (\partial_{b}{g_{p c}} + \partial_{c}{g_{p b}} - \partial_{p}{g_{b c}})''')
ruleRicci = Ex(r'''R_{a b} -> \partial_{p}{\Gamma^{p}_{a b}} - \partial_{b}{\Gamma^{p}_{p a}} + \Gamma^{p}_{p q} \Gamma^{q}_{a b} - \Gamma^{p}_{b q} \Gamma^{q}_{p a}''')
ruleEinstein = Ex(r'''G_{a b} -> R_{a b} - 1/2 g_{a b} g^{p q} R_{p q}''')

rulegg1 = Ex(r'''g_{a p} g^{a q} -> \delta^{q}_{p}''')
rulegg2 = Ex(r'''g_{a p} g^{q a} -> \delta^{q}_{p}''')
rulegg3 = Ex(r'''g_{p a} g^{a q} -> \delta^{q}_{p}''')
rulegg4 = Ex(r'''g_{p a} g^{q a} -> \delta^{q}_{p}''')
rulegg5 = Ex(r'''g_{a b} g^{a b} -> 4''')
rulegg6 = Ex(r'''g_{a b} g^{b a} -> 4''')

ruleEtaEta1 = Ex(r'''\eta_{a p} \eta^{a q} -> \delta^{q}_{p}''')
ruleEtaEta2 = Ex(r'''\eta_{a p} \eta^{q a} -> \delta^{q}_{p}''')
ruleEtaEta3 = Ex(r'''\eta_{p a} \eta^{a q} -> \delta^{q}_{p}''')
ruleEtaEta4 = Ex(r'''\eta_{p a} \eta^{q a} -> \delta^{q}_{p}''')
ruleEtaEta5 = Ex(r'''\eta_{a b} \eta^{a b} -> 4''')
ruleEtaEta6 = Ex(r'''\eta_{a b} \eta^{b a} -> 4''')
