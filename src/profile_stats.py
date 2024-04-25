##
# @file profiling_script.py
#
# @brief Script for profiling data using cProfile and generating a profiling report
#
# @author Artem Dvorychanskyi
##

import subprocess
import pstats
import random
import io 
import cProfile
import profile_stddev

def generate_data(n):
    """
    Generate random data for profiling.

    Args:
        n (int): The number of data points to generate.

    Returns:
        list: A list of randomly generated integers.

    """
    return [random.randint(0, 100) for _ in range(n)]

def profile_data(data):
    """
    Profile the data using the profile_stddev module.

    Args:
        data (list): The data to profile.

    Returns:
        float: The result of profiling.

    """
    # Directly call the function and profile it
    result = profile_stddev.result(data)
    return result

def main():
    """
    Main function to run the profiling experiments.
    """
    data_10 = generate_data(10)
    data_1000 = generate_data(1000)
    data_1000000 = generate_data(1000000)

    
    profiler_10 = cProfile.Profile()
    profiler_1000 = cProfile.Profile()
    profiler_1000000 = cProfile.Profile()

   
    profiler_10.runctx('profile_data(data_10)', globals(), locals())
    result_10 = profile_data(data_10)

    profiler_1000.runctx('profile_data(data_1000)', globals(), locals())
    result_1000 = profile_data(data_1000)

    profiler_1000000.runctx('profile_data(data_1000000)', globals(), locals())
    result_1000000 = profile_data(data_1000000)

    with open("../profiling/vystup.txt", "w") as f:
        p = pstats.Stats(profiler_10, stream=f)
        f.write(f"Result of 10 inputs: {result_10}\n\n")
        p.strip_dirs().sort_stats("cumulative").print_stats()

        p = pstats.Stats(profiler_1000, stream=f)
        f.write(f"Result of 1000 inputs: {result_1000}\n\n")
        p.strip_dirs().sort_stats("cumulative").print_stats()

        p = pstats.Stats(profiler_1000000, stream=f)
        f.write(f"Result of 1000000 inputs: {result_1000000}\n\n")
        p.strip_dirs().sort_stats("cumulative").print_stats()

if __name__ == '__main__':
    main()
