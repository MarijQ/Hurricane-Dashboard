import sys


def main():
    # Create a dictionary to store KE for each status
    status_energies = {}

    for line in sys.stdin:
        # Read key-value pairs (status -> average KE)
        status, avg_ke = line.strip().split('\t')
        avg_ke = float(avg_ke)  # Convert KE to a floating-point number

        if status not in status_energies:
            # For a new status, initialize the list to hold KEs
            status_energies[status] = []

        # Add the current average KE to the list for this status
        status_energies[status].append(avg_ke)

    # Process the KE lists for each status
    for status, energies in status_energies.items():
        # Calculate the average of the average KEs for each status
        avg_of_avgs = sum(energies) / len(energies) if energies else 0
        # Print the final average KE for each status
        print(f'{status}\t{avg_of_avgs}')


if __name__ == "__main__":
    main()

