
import circuit
import grover_search_algo as gsa
from qiskit.visualization import circuit_drawer

# q = circuit.Circuit()
q = gsa.grover_search("111")
q.measure_all()
image_path = "qiskit/q_output.png"
circuit_drawer(q, output='mpl', filename=image_path)
