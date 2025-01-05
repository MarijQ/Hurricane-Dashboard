import sys

def reduce_storm_data():
    current_key = None  # Track the current unique key (storm_id_status)
    count = 0  # Number of entries for current storm
    total_ke = 0  # Total relative KE for current storm

    for line in sys.stdin:
        # Read key-value pairs from mapper output
        key, rel_ke = line.strip().split('\t')
        rel_ke = float(rel_ke)

        if current_key == key:
            # If the key hasn't changed, accumulate the KE and count
            total_ke += rel_ke
            count += 1
        else:
            # If the key changes, output the average KE for the previous storm
            if current_key:
                # Calculate average KE per storm
                average_ke = total_ke / count if count > 0 else 0
                # Output the unique storm ID with its average KE
                print(f'{current_key}\t{average_ke}')
            # Reset the counters with the new key
            current_key = key
            total_ke = rel_ke
            count = 1

    # Output the average KE for the last storm in the dataset
    if current_key:
        average_ke = total_ke / count if count > 0 else 0
        print(f'{current_key}\t{average_ke}')


def main():
    # Start the reduction process
    reduce_storm_data()


if __name__ == "__main__":
    main()

