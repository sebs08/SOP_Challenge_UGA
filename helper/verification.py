# verification of given solutions
from helper.parser import parser, filenames


def check_solution(arcs, solution):
    """

    :param arcs: weights of arcs of the graph - 2 dim numpy array
    :param solution: solution vector - 1 dim numpy array
    :return: value of the solution; if -1 gets returned, solution is not valid

    Method to check whether a solution is valid in terms of length, precedence constraints and permutation property.
    Returns the value of the Solution.
    """

    value = 0

    # check if shapes coincide
    if solution.shape[0] != arcs.shape[0]:
        return -1

    # check if values are in valid range
    if solution.max() >= solution.shape[0]:
        return -1

    # check that all solution is a permutation (no value is allowed twice)
    if len(set(solution)) != solution.shape[0]:
        return -1

    for i in range(solution.shape[0]-1):  # cycle through solution and check constraints
        arc_weight = arcs[solution[i], solution[i+1]]

        # check if arc_weight is valid value
        if arc_weight == -1 or arc_weight >= 500000:
            return -1

        for j in range(arcs.shape[0]):
            # check precedence constraints
            if arcs[solution[i], j] == -1:  # check row i for constraints
                if j not in solution[:i]:
                    # if constraint is not satisfied in solution
                    return -1

        value += arc_weight

    return value

if __name__ == "__main__":

    # directory paths
    sol_path = "../Data/solutions/"
    sop_path = "../Data/course_benchmark_instances/"

    # get filenames (files where solutions are given)
    sop_files, sol_files = filenames([sol_path, sop_path])

    # initialize array arcs and solutions
    instances = []

    # fill arrays
    for i in range(len(sop_files)):
        arcs = parser(sop_files[i], True)
        solution = parser(sol_files[i], True)
        instances += [(arcs, solution)]
        value = check_solution(arcs, solution)
        print("The solution value is: " + str(int(value)) + "\n")

    print("")
