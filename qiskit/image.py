
import circuit
from qiskit.visualization import circuit_drawer

# run first
# conda activate qiskit_env
q = circuit.Circuit()
q.circuit.measure_all()
image_path = "qiskit/q_output.png"
circuit_drawer(q.circuit, output='mpl', filename=image_path)
