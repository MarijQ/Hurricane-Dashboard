import sys

def main():
    for line in sys.stdin:
        # Process each line outputted by the first reducer
        key, avg_ke = line.strip().split('\t')
        # Extract status from the composite key
        status = key.split('_')[-1]
        # Output the status and average KE for further processing
        print(f'{status}\t{avg_ke}')

if __name__ == "__main__":
    main()

