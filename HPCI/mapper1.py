import sys


def map_storm_data(line):
    # Extracting the relevant fields from the CSV line
    parts = line.strip().split(',')

    try:
        # Extracted fields
        name = parts[1].strip()  # Storm name
        year = int(parts[2].strip())  # Year of the storm

        # Apply the filter for the year being 2004 or later
        if year >= 2004:
            status = parts[8].strip().lower()  # Storm status (depression, storm, hurricane)
            diameter = float(parts[12].strip())  # Reported tropical storm diameter
            wind_speed = float(parts[10].strip())  # Wind speed

            # Calculate relative kinetic energy using the formula
            rel_ke = diameter ** 2 * wind_speed ** 3

            # Concatenate name and year to create a unique storm identifier
            unique_id = f'{name}_{year}'

            # Output the calculated relative KE with a composite key of unique storm identifier and status
            print(f'{unique_id}_{status}\t{rel_ke}')
    except (IndexError, ValueError):
        # Skip any lines with missing data or erroneous values
        pass


def main():
    # Skip the header row from the CSV
    next(sys.stdin)
    for line in sys.stdin:
        # For each line of data, apply the mapping function
        map_storm_data(line)


if __name__ == "__main__":
    main()

