import qiskit
import circuit

# run first
# conda activate qiskit_env

q = circuit.Circuit()

q.circuit.measure_all()

# Simulate the circuit and obtain measurement outcomes
simulator = qiskit.Aer.get_backend('qasm_simulator')
result = qiskit.execute(q.circuit, simulator).result()
counts = result.get_counts()

print("Measurement outcomes:", counts)
