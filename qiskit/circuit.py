import qiskit


class Circuit:
    def __init__(self):
        circuit = qiskit.QuantumCircuit(3)
        circuit.h(0)
        circuit.x(2)

        circuit.ccx(0, 2, 1)
        circuit.h(0)

        self.circuit = circuit
