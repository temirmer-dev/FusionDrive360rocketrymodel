import matplotlib.pyplot as plt

g0 = 9.81  # m/s^2

def fusion_electric_engine(P_MW, efficiency, mdot, exhaust_velocity):
    P = P_MW * 1e6 * efficiency  # power in watts
    thrust = mdot * exhaust_velocity
    isp = exhaust_velocity / g0
    return thrust, isp, P

# Example parameters
P_MW = 50          # reactor power, MW
efficiency = 0.35  # efficiency 35%
mdot = 0.5         # kg/s
Ve = 30000         # m/s exhaust velocity

thrust, isp, P = fusion_electric_engine(P_MW, efficiency, mdot, Ve)

print(f"Power delivered: {P/1e6:.2f} MW")
print(f"Thrust: {thrust:.2f} N")
print(f"Isp: {isp:.2f} s")

# sweep by exhaust velocity
velocities = [v for v in range(10000, 80000, 5000)]
thrusts = [mdot * v for v in velocities]
isps = [v/g0 for v in velocities]

plt.figure()
plt.plot(velocities, thrusts)
plt.xlabel("Exhaust velocity (m/s)")
plt.ylabel("Thrust (N)")
plt.title("Thrust vs Exhaust Velocity")
plt.savefig("../plots/thrust_curve.png")
plt.close()

