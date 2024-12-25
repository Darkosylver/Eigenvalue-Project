import numpy as np
import matplotlib.pyplot as plt
import time

# Generate a large, stiff matrix
def generate_stiff_matrix(size):
    A = np.random.rand(size, size) * 10
    A = (A + A.T) / 2  # Make the matrix symmetric (ensures real eigenvalues)
    A += size * np.eye(size)  # Add diagonal dominance to make it stiff
    return A

# Power Iteration method
def power_iteration(A, max_iterations=1000, tolerance=1e-10):
    n = A.shape[0]
    b = np.random.rand(n)
    b = b / np.linalg.norm(b)
    convergence_rates = []

    for _ in range(max_iterations):
        b_next = np.dot(A, b)
        b_next = b_next / np.linalg.norm(b_next)

        convergence_rate = np.linalg.norm(b_next - b)
        convergence_rates.append(convergence_rate)

        if convergence_rate < tolerance:
            break
        b = b_next

    eigenvalue = np.dot(b.T, np.dot(A, b))
    eigenvector = b
    return eigenvalue, eigenvector, convergence_rates


# Second largest eigenvalue using deflation
def second_largest_eigenvalue(A, largest_eigenvalue, largest_eigenvector, max_iterations=5, tolerance=1e-3):
    A_deflated = A - largest_eigenvalue * np.outer(largest_eigenvector, largest_eigenvector)
    return power_iteration(A_deflated, max_iterations, tolerance)


# QR Decomposition method
def qr_algorithm(A, max_iterations=5, tolerance=1e-3):
    n = A.shape[0]
    Ak = A.copy()
    Q_total = np.eye(n)

    for _ in range(max_iterations):
        Q, R = np.linalg.qr(Ak)
        Ak = np.dot(R, Q)
        Q_total = np.dot(Q_total, Q)

        off_diagonal_norm = np.linalg.norm(Ak - np.diag(np.diagonal(Ak)))
        if off_diagonal_norm < tolerance:
            break

    eigenvalues = np.diag(Ak)
    eigenvectors = Q_total
    return eigenvalues, eigenvectors


# Comparison of methods
def compare_methods(A):
    # Power Iteration for largest eigenvalue
    start_time = time.time()
    largest_eigenvalue, largest_eigenvector, largest_convergence = power_iteration(A)
    power_time_largest = time.time() - start_time

    # Power Iteration for second largest eigenvalue
    start_time = time.time()
    second_eigenvalue, second_eigenvector, second_convergence = second_largest_eigenvalue(A, largest_eigenvalue,
                                                                                          largest_eigenvector)
    power_time_second = time.time() - start_time

    # QR Decomposition
    start_time = time.time()
    qr_eigenvalues, qr_eigenvectors = qr_algorithm(A)
    qr_time = time.time() - start_time

    # Exact Solution
    exact_eigenvalues, exact_eigenvectors = np.linalg.eig(A)

    # Results
    print("Power Iteration Results:")
    print(f"Largest Eigenvalue: {largest_eigenvalue}")
    print(f"Second Largest Eigenvalue: {second_eigenvalue}")
    print(f"Time Taken (Largest): {power_time_largest:.4f} seconds")
    print(f"Time Taken (Second Largest): {power_time_second:.4f} seconds")

    print("\nQR Decomposition Results:")
    print(f"Eigenvalues: {sorted(qr_eigenvalues)}")
    print(f"Time Taken: {qr_time:.4f} seconds")

    print("\n Exact Solution Result:")
    print(f"Eigenvalues: {sorted(exact_eigenvalues)}")
    print(f"Eigenvectors: {exact_eigenvectors}")

    # Visualizations
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(qr_eigenvalues)), qr_eigenvalues, alpha=0.7, label='QR Eigenvalues')
    plt.axhline(y=largest_eigenvalue, color='r', linestyle='--', label='Power Iteration Largest Eigenvalue')
    plt.axhline(y=second_eigenvalue, color='g', linestyle='--', label='Power Iteration Second Largest Eigenvalue')
    plt.xlabel('Index')
    plt.ylabel('Eigenvalue')
    plt.title('Eigenvalue Comparison')
    plt.legend()
    plt.show()

    # Convergence Rates
    plt.figure(figsize=(10, 6))
    plt.plot(largest_convergence, label='Largest Eigenvalue Convergence')
    plt.plot(second_convergence, label='Second Largest Eigenvalue Convergence')
    plt.yscale('log')
    plt.xlabel('Iteration')
    plt.ylabel('Convergence Rate')
    plt.title('Convergence Rates of Power Iteration')
    plt.legend()
    plt.show()


# Experiment with user-provided matrix and size
def experiment():
    # size = int(input("Enter the size of the matrix: "))
    # print("Enter the elements of the matrix row by row (space-separated):")
    # matrix = []
    # for _ in range(size):
    #     row = list(map(float, input().split()))
    #     matrix.append(row)
    # A = np.array(matrix)
    #
    # print(f"\nMatrix (Size: {A.shape[0]}):")
    A = generate_stiff_matrix(500)
    compare_methods(A)


# Run the experiment
if __name__ == "__main__":
    experiment()
