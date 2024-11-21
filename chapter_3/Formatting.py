
kB = 1.380649e-23 
mu_e = -9.28476377e-24  
N_A = 6.02214076e23  
c = 2.99792458e8  
G = 6.67430e-11  
G_unc = 1.5e-15  
mu_e_unc = 2.3e-31  


kB_units = 'J/K'
mu_e_units = 'J/T'
N_A_units = 'mol^-1'
c_units = 'm/s'
G_units = 'Nm^2/kg^2'


print("kB = {:.4e} {}".format(kB, kB_units))
print("mu_e = {:.4e} {}".format(mu_e, mu_e_units))
print("N_A = {:.4e} {}".format(N_A, N_A_units))
print("c = {:.4e} {}".format(c, c_units))


print("\nkB = {:.4e} {}".format(1.3807e-23, kB_units))
print("mu_e = {:.4e} {}".format(-9.2848e-24, mu_e_units))
print("N_A = {:.4e} {}".format(6.0221e+23, N_A_units))
print("c = {:.4e} {}".format(2.9979e+8, c_units))


print("\nG = {:+.2E} [{}]".format(G, G_units))
print("mu_e = {:+.2E} [{}]".format(mu_e, mu_e_units))


G_value_str = "{:.5f}".format(G)  
G_unc_str = "{:.0f}".format(G_unc * 1e15)  
print("\nG = {}({})e-11 {}".format(G_value_str, G_unc_str, G_units))


mu_e_value_str = "{:.8f}".format(mu_e)
mu_e_unc_str = "{:.0f}".format(mu_e_unc * 1e24)  
print("mu_e = {}({})e-24 {}".format(mu_e_value_str, mu_e_unc_str, mu_e_units))
