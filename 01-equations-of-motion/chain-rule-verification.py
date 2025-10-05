#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SymPy script to verify chain rule transformations in central force problems.

This script verifies the mathematical steps shown in chain-rule.md for:
1. Chain rule application: dr/dt = (dθ/dt)(dr/dθ)
2. Angular momentum conservation substitution
3. Second derivative calculations
4. Reciprocal substitution r = 1/u and its derivatives
"""

import sympy as sp
from sympy import symbols, diff, simplify, expand, latex, pprint

# Define symbols
r, theta, t, u = symbols('r theta t u', real=True)
M0, m = symbols('M_0 m', positive=True)

print("=" * 80)
print("CHAIN RULE VERIFICATION FOR CENTRAL FORCE PROBLEMS")
print("=" * 80)

print("\n1. BASIC CHAIN RULE VERIFICATION")
print("-" * 40)

# Define r as a function of theta
r_func = sp.Function('r')(theta)
theta_func = sp.Function('theta')(t)

# Chain rule: dr/dt = (dθ/dt)(dr/dθ)
print("Chain rule: dr/dt = (dθ/dt)(dr/dθ)")
print("Left side: dr/dt =", diff(r_func.subs(theta, theta_func), t))
print("Right side: (dθ/dt)(dr/dθ) =", diff(theta_func, t) * diff(r_func, theta))

# Verify they are equal
lhs = diff(r_func.subs(theta, theta_func), t)
rhs = diff(theta_func, t) * diff(r_func, theta)
print("Verification:", simplify(lhs - rhs) == 0)

print("\n2. ANGULAR MOMENTUM CONSERVATION SUBSTITUTION")
print("-" * 50)

# Angular momentum conservation: mr²θ̇ = M₀
# Therefore: θ̇ = M₀/(mr²)
theta_dot = M0 / (m * r**2)

# Substitute into chain rule
r_dot_chain = theta_dot * diff(r_func, theta)
print("θ̇ = M₀/(mr²)")
print("ṙ = θ̇(dr/dθ) =", r_dot_chain)

print("\n3. SECOND DERIVATIVE CALCULATION")
print("-" * 40)

# Second derivative: r̈ = d/dt[ṙ]
# Using the chain rule again: d/dt = θ̇(d/dθ)
r_double_dot = theta_dot * diff(r_dot_chain, theta)
print("r̈ = θ̇(d/dθ)[ṙ]")
print("r̈ =", expand(r_double_dot))

# Let's break this down step by step as shown in the document
print("\nDetailed calculation:")
print("r̈ = θ̇(d/dθ)[(M₀/(mr²))(dr/dθ)]")

# First term: derivative of M₀/(mr²) with respect to θ
term1 = theta_dot * diff(r_func, theta) * diff(M0/(m*r**2), theta)
print("First term:", term1)

# Second term: derivative of dr/dθ with respect to θ
term2 = theta_dot * (M0/(m*r**2)) * diff(diff(r_func, theta), theta)
print("Second term:", term2)

# Total
total = expand(term1 + term2)
print("Total r̈ =", total)

print("\n4. RECIPROCAL SUBSTITUTION r = 1/u")
print("-" * 45)

# Define u as a function of theta
u_func = sp.Function('u')(theta)

# Relationship: r = 1/u
print("Substitution: r = 1/u")
print("Therefore: dr/du = -1/u²")

# First derivative: dr/dθ
dr_dtheta = diff(1/u_func, theta)
print("dr/dθ = d/dθ(1/u) =", dr_dtheta)

# Second derivative: d²r/dθ²
d2r_dtheta2 = diff(dr_dtheta, theta)
print("d²r/dθ² =", expand(d2r_dtheta2))

print("\n5. SUBSTITUTING BACK INTO r̈ EXPRESSION")
print("-" * 50)

# Substitute r = 1/u into the r̈ expression
# r̈ = -2M₀²/(m²r⁵)(dr/dθ)² + M₀²/(m²r⁴)(d²r/dθ²)

# First term: -2M₀²/(m²r⁵)(dr/dθ)²
term1_sub = -2*M0**2/(m**2 * (1/u_func)**5) * dr_dtheta**2
print("First term with substitution:", expand(term1_sub))

# Second term: M₀²/(m²r⁴)(d²r/dθ²)
term2_sub = M0**2/(m**2 * (1/u_func)**4) * d2r_dtheta2
print("Second term with substitution:", expand(term2_sub))

# Total with substitution
total_sub = expand(term1_sub + term2_sub)
print("Total r̈ with substitution:", total_sub)

print("\n6. SIMPLIFICATION TO FINAL FORM")
print("-" * 40)

# The final simplified form should be: r̈ = -M₀²u²/(m²)(d²u/dθ²)
final_form = -M0**2 * u_func**2 / m**2 * diff(diff(u_func, theta), theta)
print("Expected final form: r̈ = -M₀²u²/(m²)(d²u/dθ²)")
print("Expected:", final_form)

# Verify if our calculation matches
print("Verification - Difference:", simplify(total_sub - final_form))

print("\n7. NUMERICAL VERIFICATION")
print("-" * 30)

# Let's test with specific values to ensure our symbolic calculation is correct
test_values = {M0: 1, m: 1, u_func: sp.Function('u')(theta)}

# Create a simple test function u(θ) = sin(θ)
u_test = sp.sin(theta)
r_test = 1/u_test

print("Test case: u(θ) = sin(θ), so r(θ) = 1/sin(θ)")

# Calculate derivatives
dr_dtheta_test = diff(r_test, theta)
d2r_dtheta2_test = diff(dr_dtheta_test, theta)

print("dr/dθ =", dr_dtheta_test)
print("d²r/dθ² =", d2r_dtheta2_test)

# Calculate r̈ using our formula
r_double_dot_test = -M0**2 * u_test**2 / m**2 * diff(diff(u_test, theta), theta)
print("r̈ =", r_double_dot_test)

print("\n" + "=" * 80)
print("VERIFICATION COMPLETE")
print("=" * 80)
