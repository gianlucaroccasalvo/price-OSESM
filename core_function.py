# DOCUMENTATION: this function will use 
# - price of electricity generated from renewable sources (pr), expressed in [€/kWh]
# - market share of electricity generated from renewable sources (sr), expressed in percentage (i.e. 40% = 0.4)
# - price of electricity generated from fossil sources (pf), expressed in [€/kWh]
# - market share of electricity generated from fossil sources (sf), expressed in percentage (i.e. 60% = 0.6)
# to compute the overall electricity price as a weighted average on the market share, expressed in [€/kWh]

def price(pr, sr, pf, sf):
  return (pr * sr) + 2*(pf * sf) 