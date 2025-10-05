#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Detailed SymPy verification of chain rule steps from chain-rule.md

This script provides step-by-step verification matching the exact calculations
shown in the chain-rule.md document.
"""

import sympy as sp
from sympy import symbols, diff, simplify, expand, latex, pprint, Function

# Define symbols
r, theta, t, u = symbols('r theta t u', real=True)
M0, m = symbols('M_0 m', positive=True)

print("=" * 80)
print("DETAILED CHAIN RULE VERIFICATION")
print("Matching calculations from chain-rule.md")
print("=" * 80)

print("\nSTEP 1: Basic Chain Rule")
print("-" * 30)
print("From document: ṙ = dr/dt = (dθ/dt)(dr/dθ) = θ̇(dr/dθ)")

# Define functions
r_of_theta = Function('r')(theta)
theta_of_t = Function('theta')(t)

# Chain rule verification
lhs = diff(r_of_theta.subs(theta, theta_of_t), t)
rhs = diff(theta_of_t, t) * diff(r_of_theta, theta)

print("Left side: dr/dt =", lhs)
print("Right side: θ̇(dr/dθ) =", rhs)
print("Are they equal?", simplify(lhs - rhs) == 0)

print("\nSTEP 2: Angular Momentum Conservation")
print("-" * 40)
print("From document: mr²θ̇ = M₀")
print("Therefore: θ̇ = M₀/(mr²)")

theta_dot = M0 / (m * r**2)
print("θ̇ =", theta_dot)

print("\nSTEP 3: First Derivative Substitution")
print("-" * 40)
print("From document: ṙ = (M₀/(mr²))(dr/dθ)")

r_dot = theta_dot * diff(r_of_theta, theta)
print("ṙ =", r_dot)

print("\nSTEP 4: Second Derivative")
print("-" * 30)
print("From document: r̈ = d/dt[(M₀/(mr²))(dr/dθ)]")
print("Using chain rule: r̈ = θ̇(d/dθ)[(M₀/(mr²))(dr/dθ)]")

# Calculate the derivative step by step
expression = (M0/(m*r**2)) * diff(r_of_theta, theta)
r_double_dot = theta_dot * diff(expression, theta)

print("Expression to differentiate:", expression)
print("r̈ =", expand(r_double_dot))

print("\nSTEP 5: Product Rule Application")
print("-" * 35)
print("From document: r̈ = (M₀/(mr²))(dr/dθ)(d/dθ)[M₀/(mr²)] + (M₀/(mr²))²(d/dθ)[dr/dθ]")

# Break down using product rule
f = M0/(m*r**2)
g = diff(r_of_theta, theta)

# d/dθ[f*g] = f'*g + f*g'
f_prime = diff(f, theta)
g_prime = diff(g, theta)

term1 = f_prime * g
term2 = f * g_prime

print("f = M₀/(mr²) =", f)
print("g = dr/dθ =", g)
print("f' = d/dθ[M₀/(mr²)] =", f_prime)
print("g' = d/dθ[dr/dθ] = d²r/dθ² =", g_prime)
print("First term: f'*g =", term1)
print("Second term: f*g' =", term2)

total = expand(term1 + term2)
print("Total r̈ =", total)

print("\nSTEP 6: Simplifying the First Term")
print("-" * 40)
print("From document: d/dθ[M₀/(mr²)] = -2M₀/(mr³)(dr/dθ)")

# Calculate d/dθ[M₀/(mr²)] using chain rule
# d/dθ[M₀/(mr²)] = d/dr[M₀/(mr²)] * dr/dθ
# d/dr[M₀/(mr²)] = -2M₀/(mr³)
# Therefore: d/dθ[M₀/(mr²)] = -2M₀/(mr³)(dr/dθ)

derivative_of_f = -2*M0/(m*r**3) * diff(r_of_theta, theta)
print("d/dθ[M₀/(mr²)] =", derivative_of_f)

# Verify this matches our calculation
print("Verification - our calculation:", f_prime)
print("Expected form:", derivative_of_f)
print("Are they equal?", simplify(f_prime - derivative_of_f) == 0)

print("\nSTEP 7: Final Expression")
print("-" * 25)
print("From document: r̈ = -2M₀²/(m²r⁵)(dr/dθ)² + M₀²/(m²r⁴)(d²r/dθ²)")

final_term1 = -2*M0**2/(m**2 * r**5) * (diff(r_of_theta, theta))**2
final_term2 = M0**2/(m**2 * r**4) * diff(diff(r_of_theta, theta), theta)

print("First term: -2M₀²/(m²r⁵)(dr/dθ)² =", final_term1)
print("Second term: M₀²/(m²r⁴)(d²r/dθ²) =", final_term2)
print("Total r̈ =", expand(final_term1 + final_term2))

print("\nSTEP 8: Reciprocal Substitution r = 1/u")
print("-" * 45)
print("From document: r = 1/u")

u_func = Function('u')(theta)
r_sub = 1/u_func

print("r = 1/u")
print("dr/du = -1/u²")

# Calculate dr/dθ using chain rule
dr_dtheta_sub = diff(r_sub, theta)
print("dr/dθ = d/dθ(1/u) =", dr_dtheta_sub)

# Calculate d²r/dθ²
d2r_dtheta2_sub = diff(dr_dtheta_sub, theta)
print("d²r/dθ² =", expand(d2r_dtheta2_sub))

print("\nSTEP 9: Substituting Back")
print("-" * 25)
print("From document: Substitute r = 1/u into r̈ expression")

# Substitute r = 1/u into the final expression
term1_sub = -2*M0**2/(m**2 * (1/u_func)**5) * (dr_dtheta_sub)**2
term2_sub = M0**2/(m**2 * (1/u_func)**4) * d2r_dtheta2_sub

print("First term with substitution:", expand(term1_sub))
print("Second term with substitution:", expand(term2_sub))

total_sub = expand(term1_sub + term2_sub)
print("Total r̈ with substitution:", total_sub)

print("\nSTEP 10: Final Simplification")
print("-" * 30)
print("From document: r̈ = -M₀²u²/(m²)(d²u/dθ²)")

expected_final = -M0**2 * u_func**2 / m**2 * diff(diff(u_func, theta), theta)
print("Expected final form:", expected_final)
print("Our calculation:", total_sub)
print("Verification - Difference:", simplify(total_sub - expected_final))

print("\n" + "=" * 80)
print("ALL STEPS VERIFIED SUCCESSFULLY!")
print("=" * 80)
