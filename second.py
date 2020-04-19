from cadabra2 import *

Indices(Ex(r'''{a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z#}'''), Ex(r'''fourD, position=independent''') )
Integer(Ex(r'''{a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z#}'''), Ex(r'''0..3''') )

Indices(Ex(r'''{\alpha,\beta,\gamma,\delta,\epsilon,\zeta,\theta,\iota,\kappa,\lambda,\mu,\nu,\rho,\sigma,\tau#}'''), Ex(r'''threeD, position=independent, parent=fourD''') )
Integer(Ex(r'''{\alpha,\beta,\gamma,\delta,\epsilon,\zeta,\theta,\iota,\kappa,\lambda,\mu,\nu,\rho,\sigma,\tau#}'''), Ex(r'''1..3''') )

KroneckerDelta(Ex(r'''\delta{#}'''), Ex(r'''''') )
Symmetric(Ex(r'''g_{a? b?}'''), Ex(r'''''') )
Symmetric(Ex(r'''g^{a? b?}'''), Ex(r'''''') )
Symmetric(Ex(r'''\eta_{a? b?}'''), Ex(r'''''') )
Symmetric(Ex(r'''\eta^{a? b?}'''), Ex(r'''''') )
Symmetric(Ex(r'''h^{a? b?}'''), Ex(r'''''') )

Symmetric(Ex(r'''\gamma_{\alpha \beta}'''), Ex(r'''''') )
Symmetric(Ex(r'''\gamma^{\alpha \beta}'''), Ex(r'''''') )

PartialDerivative(Ex(r'''\partial{#}'''), Ex(r'''''') )
Depends(Ex(r'''g{#}'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''h{#}'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''G{#}'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''\Gamma{#}'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''R{#}'''), Ex(r'''\partial{#})''') )
Depends(Ex(r'''\Phi'''), Ex(r'''\partial{#})''') )

Weight(Ex(r'''h{#}'''), Ex(r'''label=l, value=1'''))
WeightInherit(Ex(r'''\partial{#}'''), Ex(r'''label=all, type=multiplicative'''))

SortOrder(Ex(r'''\eta_{a b},\eta^{a b}'''), Ex(r''''''))

def my_canonicalise(e):
  sort_product(e)
  sort_sum(e)
  collect_terms(e)
  rename_dummies(e)
  collect_terms(e)

def my_eliminate_kronecker(e):
  substitute(e, Ex(r'''\delta_{a?}^{b?} -> \delta^{b?}_{a?}'''), repeat=True)

  substitute(e, Ex(r'''\delta^{a}_{a} -> 4'''), repeat=True)

  substitute(e, Ex(r'''\delta^{0}_{0} -> 1'''), repeat=True)

  substitute(e, Ex(r'''\delta^{0}_{\alpha} -> 0'''), repeat=True)
  substitute(e, Ex(r'''\delta^{\alpha}_{0} -> 0'''), repeat=True)
  substitute(e, Ex(r'''\delta^{\alpha}_{\alpha} -> 3'''), repeat=True)

  substitute(e, Ex(r'''\delta^{a}_{0} \delta^{0}_{a} -> 1'''), repeat=True)
  substitute(e, Ex(r'''\delta^{a}_{\alpha} \delta^{0}_{a} -> 0'''), repeat=True)
  substitute(e, Ex(r'''\delta^{a}_{0} \delta^{\alpha}_{a} -> 0'''), repeat=True)
  substitute(e, Ex(r'''\delta^{a}_{\alpha} \delta^{\beta}_{a} -> \delta^{\beta}_{\alpha}'''), repeat=True)

  substitute(e, Ex(r'''\delta^{\alpha}_{\beta} \delta^{\beta}_{\gamma} -> \delta^{\alpha}_{\gamma}'''), repeat=True)
  substitute(e, Ex(r'''\delta^{\beta}_{\alpha} \delta^{\gamma}_{\beta} -> \delta^{\gamma}_{\alpha}'''), repeat=True)

  substitute(e, Ex(r'''\delta^{\alpha}_{\beta} \gamma^{\beta \delta} -> \gamma^{\alpha \delta}'''), repeat=True)
  substitute(e, Ex(r'''\delta^{\alpha}_{\beta} \gamma^{\delta \beta} -> \gamma^{\alpha \delta}'''), repeat=True)
  substitute(e, Ex(r'''\delta^{\alpha}_{\beta} \gamma_{\alpha \delta} -> \gamma_{\beta \delta}'''), repeat=True)
  substitute(e, Ex(r'''\delta^{\alpha}_{\beta} \gamma_{\delta \alpha} -> \gamma_{\beta \delta}'''), repeat=True)

  substitute(e, Ex(r'''\delta^{\alpha}_{\beta} \partial_{\alpha}{Q??} -> \partial_{\beta}{Q??}'''))
  substitute(e, Ex(r'''\delta^{\alpha}_{\beta} \partial_{\alpha 0}{Q??} -> \partial_{\beta 0}{Q??}'''))
  substitute(e, Ex(r'''\delta^{\alpha}_{\beta} \partial_{0 \alpha}{Q??} -> \partial_{0 \beta}{Q??}'''))
  substitute(e, Ex(r'''\delta^{\alpha}_{\beta} \partial_{\alpha \gamma}{Q??} -> \partial_{\beta \gamma}{Q??}'''))
  substitute(e, Ex(r'''\delta^{\alpha}_{\beta} \partial_{\gamma \alpha}{Q??} -> \partial_{\gamma \beta}{Q??}'''))

def my_eliminate_metric(e):
  substitute(e, Ex(r'''\gamma^{\alpha \beta} \gamma_{\alpha \beta} -> 3'''), repeat=True)
  substitute(e, Ex(r'''\gamma^{\alpha \beta} \gamma_{\beta \alpha} -> 3'''), repeat=True)

  substitute(e, Ex(r'''\gamma^{\alpha \beta} \gamma_{\beta \gamma} -> \delta^{\alpha}_{\gamma}'''), repeat=True)
  substitute(e, Ex(r'''\gamma^{\beta \alpha} \gamma_{\beta \gamma} -> \delta^{\alpha}_{\gamma}'''), repeat=True)
  substitute(e, Ex(r'''\gamma^{\alpha \beta} \gamma_{\gamma \beta} -> \delta^{\alpha}_{\gamma}'''), repeat=True)
  substitute(e, Ex(r'''\gamma^{\beta \alpha} \gamma_{\gamma \beta} -> \delta^{\alpha}_{\gamma}'''), repeat=True)

  substitute(e, Ex(r'''\gamma^{\alpha \beta} \partial_{\beta \alpha}{Q??} -> \gamma^{\alpha \beta} \partial_{\alpha \beta}{Q??}'''), repeat=True)

def three_plus_one_metric(e):
  substitute(e, Ex(r'''\eta_{0 0} -> 1'''), repeat=True)
  substitute(e, Ex(r'''\eta_{0 a} -> \delta^{0}_{a}'''), repeat=True)
  substitute(e, Ex(r'''\eta_{a 0} -> \delta^{0}_{a}'''), repeat=True)
  substitute(e, Ex(r'''\eta_{a b} -> \delta^{0}_{a} \delta^{0}_{b} - \delta^{\alpha}_{a} \delta^{\beta}_{b} \gamma_{\alpha \beta}'''), repeat=True)

  substitute(e, Ex(r'''\eta^{0 0} -> 1'''), repeat=True)
  substitute(e, Ex(r'''\eta^{0 a} -> \delta^{a}_{0}'''), repeat=True)
  substitute(e, Ex(r'''\eta^{a 0} -> \delta^{a}_{0}'''), repeat=True)
  substitute(e, Ex(r'''\eta^{a b} -> \delta^{a}_{0} \delta^{b}_{0} - \delta^{a}_{\alpha} \delta^{b}_{\beta} \gamma^{\alpha \beta}'''), repeat=True)

  substitute(e, Ex(r'''h^{0 0} -> \Phi'''), repeat=True)
  substitute(e, Ex(r'''h^{0 a} -> \delta^{a}_{0} \Phi'''), repeat=True)
  substitute(e, Ex(r'''h^{a 0} -> \delta^{a}_{0} \Phi'''), repeat=True)
  substitute(e, Ex(r'''h^{a b} -> \delta^{a}_{0} \delta^{b}_{0} \Phi + \delta^{a}_{\alpha} \delta^{b}_{\beta} \gamma^{\alpha \beta} \Phi'''), repeat=True)

def three_plus_one_partial(e):
  substitute(e, Ex(r'''\partial_{a}{Q??} -> \delta^{0}_{a} \partial_{0}{Q??} + \delta^{\alpha}_{a} \partial_{\alpha}{Q??}'''))
  substitute(e, Ex(r'''\partial_{a b}{Q??} -> \delta^{0}_{a} \delta^{0}_{b} \partial_{0 0}{Q??} + \delta^{0}_{a} \delta^{\beta}_{b} \partial_{0 \beta}{Q??} + \delta^{\alpha}_{a} \delta^{0}_{b} \partial_{\alpha 0}{Q??} + \delta^{\alpha}_{a} \delta^{\beta}_{b} \partial_{\alpha \beta}{Q??}'''))

ruleMetricUp = Ex(r'''g^{a b} -> \eta^{a b} + h^{a b}''')
ruleMetricDown = Ex(r'''g_{a b} -> \eta_{a b} - \eta_{a p} \eta_{b q} h^{p q}''')

ruleChristoffel = Ex(r'''\Gamma^{a}_{b c} -> 1/2 g^{a p} (\partial_{b}{g_{p c}} + \partial_{c}{g_{p b}} - \partial_{p}{g_{b c}})''')
ruleRicci = Ex(r'''R_{a b} -> \partial_{p}{\Gamma^{p}_{a b}} - \partial_{b}{\Gamma^{p}_{p a}} + \Gamma^{p}_{p q} \Gamma^{q}_{a b} - \Gamma^{p}_{b q} \Gamma^{q}_{p a}''')
ruleEinstein = Ex(r'''G_{a b} -> R_{a b} - 1/2 g_{a b} g^{p q} R_{p q}''')

ruleEvalEtaUp = Ex(r'''\eta^{t t} = 1, \eta^{t x} = 0, \eta^{t y} = 0, \eta^{t z} = 0, \eta^{x x} = -1, \eta^{x y} = 0, \eta^{x z} = 0, \eta^{y y} = -1, \eta^{y z} = 0, \eta^{z z} = -1''')
ruleEvalEtaDown = Ex(r'''\eta_{t t} = 1, \eta_{t x} = 0, \eta_{t y} = 0, \eta_{t z} = 0, \eta_{x x} = -1, \eta_{x y} = 0, \eta_{x z} = 0, \eta_{y y} = -1, \eta_{y z} = 0, \eta_{z z} = -1''')
ruleEvalH = Ex(r'''h^{t t} = \Phi, h^{t x} = 0, h^{t y} = 0, h^{t z} = 0, h^{x x} = \Phi, h^{x y} = 0, h^{x z} = 0, h^{y y} = \Phi, h^{y z} = 0, h^{z z} = \Phi''')

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

ruleHarmonic1 = Ex(r'''\partial_{a}{h^{a p}} -> 0''')
ruleHarmonic2 = Ex(r'''\partial_{a}{h^{p a}} -> 0''')
ruleHarmonic3 = Ex(r'''\partial_{a p}{h^{a q}} -> 0''')
ruleHarmonic4 = Ex(r'''\partial_{a p}{h^{q a}} -> 0''')
ruleHarmonic5 = Ex(r'''\partial_{p a}{h^{a q}} -> 0''')
ruleHarmonic6 = Ex(r'''\partial_{p a}{h^{q a}} -> 0''')
ruleHarmonic7 = Ex(r'''\partial_{a b}{h^{a b}} -> 0''')
ruleHarmonic8 = Ex(r'''\partial_{a b}{h^{b a}} -> 0''')
