import numpy as np
import matplotlib.pyplot as plt
def detect_turning_points(signal, filename="turning_points.pdf"):
    if len(signal) < 3:
        turning_indices = np.array([])
        plt.figure()
        plt.plot(signal)
        plt.title("Signal (no turning points possible)")
        plt.savefig(filename)
        plt.close()
        return turning_indices
    diffs = np.diff(signal)
    signs = np.sign(diffs)
    turning_indices = []
    for i in range(1, len(signs)):
        prev_sign = signs[i-1]
        curr_sign = signs[i]
        if prev_sign * curr_sign < 0:
            turning_indices.append(i + 1)
        elif prev_sign == 0 and curr_sign != 0:
           j = i - 1
           while j >= 0 and signs[j] == 0:
               j -= 1
           if j >= 0 and signs[j] * curr_sign < 0:
               turning_indices.append(i + 1)
        elif prev_sign != 0 and curr_sign == 0:
           j = i + 1
           while j < len(signs) and signs[j] == 0:
               j += 1
           if j < len(signs) and prev_sign * signs[j] < 0:
               turning_indices.append(j + 1)
    turning_indices = sorted(list(set(turning_indices)))
    turning_indices = np.array(turning_indices)
    plt.figure(figsize=(10, 6))
    plt.plot(signal, 'b-', label='Signal')
    if len(turning_indices) > 0:
      plt.plot(turning_indices, signal[turning_indices], 'ro', markersize=8, label='Turning points')  
    plt.xlabel('Index')
    plt.ylabel('Signal value')
    plt.title('Signal with Turning Points')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.savefig(filename)
    plt.close()    
    return turning_indices
if __name__ == "__main__":
    signal = np.array([1, 3, 2, 4, 3, 5, 1])
    detect_turning_points(signal)