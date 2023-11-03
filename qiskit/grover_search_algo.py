import numpy as np
from qiskit import QuantumCircuit, Aer, transpile, execute
from qiskit.visualization import plot_histogram


# Helper function to apply H gate to n qubits


def apply_h_gate(circuit, n):
    for qubit in range(n):
        circuit.h(qubit)

# Helper function to apply a series of X gates to implement the oracle


def apply_oracle(circuit, search_term):
    # Apply X gate to qubits where the search_term is 1
    for qubit in range(len(search_term)):
        if search_term[qubit] == '1':
            circuit.x(qubit)

    # Apply multi-controlled Z gate (the oracle)
    circuit.h(len(search_term) - 1)
    circuit.mct(list(range(len(search_term) - 1)),
                len(search_term) - 1)  # Multi-controlled Toffoli
    circuit.h(len(search_term) - 1)

    # Uncompute X gates
    for qubit in range(len(search_term)):
        if search_term[qubit] == '1':
            circuit.x(qubit)

# Helper function to apply diffusion operator


def apply_diffusion(circuit, n):
    # Apply H to each qubit
    apply_h_gate(circuit, n)

    # Apply X to each qubit
    for qubit in range(n):
        circuit.x(qubit)

    # Apply multi-controlled Z gate (diffusion)
    circuit.h(n - 1)
    circuit.mct(list(range(n - 1)), n - 1)  # Multi-controlled Toffoli
    circuit.h(n - 1)

    # Uncompute X from each qubit
    for qubit in range(n):
        circuit.x(qubit)

    # Uncompute H from each qubit
    apply_h_gate(circuit, n)

# Function to implement Grover's search algorithm


def grover_search(search_term):
    # Determine the number of qubits needed based on the search term length
    n = len(search_term)

    # Initialize quantum circuit
    circuit = QuantumCircuit(n)

    # Step 1: Apply H gates to all qubits
    apply_h_gate(circuit, n)

    # Step 2: Apply the oracle
    apply_oracle(circuit, search_term)

    # Step 3: Apply the diffusion operator
    apply_diffusion(circuit, n)

    circuit.measure_all()

    return circuit


# Define the search term (an example: searching for '1101')
search_term = '01000110'

# Create the circuit for Grover's algorithm
grover_circuit = grover_search(search_term)

# Simulate the circuit and obtain measurement outcomes
simulator = Aer.get_backend('qasm_simulator')
result = execute(grover_circuit, simulator).result()
counts = result.get_counts()

print("Measurement outcomes:", counts)
