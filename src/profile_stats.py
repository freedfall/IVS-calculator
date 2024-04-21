import subprocess
import pstats
import random

def run_profiling(command):
    """Run the cProfile command to generate a stats file."""
    subprocess.run(command, shell=True, check=True)

def generate_numbers(count, filename):
    with open(filename, 'w') as file:
        numbers = (str(random.randint(1, 100)) for _ in range(count))
        file.write(' '.join(numbers))

def analyze_and_write_stats(stats_file, output_file):
    """Analyze the stats file and write the results to the output file."""
    stats = pstats.Stats(stats_file)
    stats.sort_stats('time')  # Sorting by time to see the most expensive functions
    with open(output_file, 'a') as f:  # Append mode to add each result to the same file
        stats.stream = f
        stats.print_stats()
        f.write('\n\n')  # Add spacing between different profile outputs

def main():
    
    generate_numbers(10, 'input_10.txt')
    generate_numbers(1000, 'input_1000.txt')
    generate_numbers(1000000, 'input_1000000.txt')

    # List of profiling commands
    commands = [
        "python3 -m cProfile -o profile_10.stats profile_stddev.py < input_10.txt",
        "python3 -m cProfile -o profile_1000.stats profile_stddev.py < input_1000.txt",
        "python3 -m cProfile -o profile_1000000.stats profile_stddev.py < input_1000000.txt"
    ]

    # Run each profiling command
    for command in commands:
        run_profiling(command)

    # Output file where the analysis results will be stored
    output_file = 'combined_analysis.txt'
    
    # Open the output file to overwrite any existing data
    open(output_file, 'w').close()

    # Analyze each stats file and write the results
    analyze_and_write_stats('profile_10.stats', output_file)
    analyze_and_write_stats('profile_1000.stats', output_file)
    analyze_and_write_stats('profile_1000000.stats', output_file)

    #delete the stats files
    subprocess.run("rm profile_10.stats profile_1000.stats profile_1000000.stats", shell=True, check=True)
    #delete the input files
    subprocess.run("rm input_10.txt input_1000.txt input_1000000.txt", shell=True, check=True)


if __name__ == '__main__':
    main()
