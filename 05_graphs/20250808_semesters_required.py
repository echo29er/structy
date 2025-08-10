from test_runner import test_runner

def semesters_required(number_of_courses: int, prerequisite_map: list[tuple[int, int]]) -> int:

    """
    Function Purpose:
        Write a function, semesters_required, that takes in a number of courses (n) and a list of prerequisites as arguments. Courses have ids ranging from 0 through n - 1. A single prerequisite of (A, B) means that course A must be taken before course B. Return the minimum number of semesters required to complete all n courses. There is no limit on how many courses you can take in a single semester, as long as the prerequisites of a course are satisfied before taking it.

    Constraints: 
        * Given prerequisite (A, B), you cannot take course A and course B concurrently in the same semester. You must take A in some semester before B.
    
    Assumptions:
        * You can assume that it is possible to eventually complete all courses.

    Parameters:
        * number_of_courses - the number of courses to complete.
        * prerequisite_map - a list of tuples where each tuple is a map defining an antecdent and its decendent. 

    Returns:
        * int: the number of semesters required to complete all the courses given the prerequisite map. 

    Time complexity:
        O(tbd) # 

    Space Complexity:
        O(tbd) # 
    """

    """
    # Analysis
    ## Edge cases
    1. where prerequisite_map is empty and number of courses is 0 then return 0
    2. where prerequisite_map is empty and there are courses return 1 as there's no limit to the number of course to take in one semester

    ## Main analysis
    Taking test_00 we can construct the graph
    0->5
    1->2->4
    3->5

    From this analysis, we can see that:
    1. we have three unconnected graphs
    2. as there's no limit to courses taken concurrently, the length of the longest path in this Directed Acyclic Graph is the number of semesters required to complete all the courses. Given we want to find the depth of a path, it's best to use the depth first search as this will track the length of the path. We explore the first branch, and compare the length of that to subsequent branches.
    """

    """ 
    # Implementation
    1. Return 0 for an empty prerequisite_map and where courses is 0 or empty.
    2. Return 1 where prerequisite_map is empty and there is more than 0 courses.
    3. Main logic: 
    A) Develop an adjacency list. Initialise an empty set in the adjacency list for the tuples values being visited. Ensure that only descendants are added to antecedents so that the direction of the graph is kept i.e. we keep the order the modules must be completed in.
    B) Depth first search. 
    """

    # BASE CASES

    if not prerequisite_map and not number_of_courses or number_of_courses == 0: 
        return 0
    
    if not prerequisite_map and number_of_courses > 0: 
        return 1
    
    # ADJACENCY LIST
    adjacency_list = {}

    for pair in prerequisite_map: 
        antecedent, descendant = pair 
    
        # Create empty sets for the antecedent and the decendent to ensure that all nodes exists in the adjacency list. 
        if antecedent not in adjacency_list: 
            adjacency_list[antecedent] = set()
        if descendant not in adjacency_list: 
            adjacency_list[descendant] = set()
        
        # Only add the descendant to the antecedent set to keep the direction of the set. 
        adjacency_list[antecedent].add(descendant)

    # DEPTH FIRST SEARCH
    memo = {} # a dictionary where key = node and value = semesters required to complete

    def dfs(course):
        if course in memo:
            return memo[course] # return the semesters required to complete if known
        
        # base case, if course has no descendant, add one sememster
        if course not in adjacency_list: 
            memo[course]=1
            return 1

        # recursive case: 1 + max depth of all descendants
        max_descendant_depth = 0 
        for descendant in adjacency_list[course]:
            max_descendant_depth = max(max_descendant_depth, dfs(descendant))

        depth = 1 + max_descendant_depth
        memo[course] = depth
        return depth
    
    # Find tha maximum depth across all courses 
    max_semesters = 0
    for course in range(number_of_courses):
        max_semesters = max(max_semesters, dfs(course))
    
    return max_semesters

    ### TEST CASES
def test_00():
    number_of_courses = 6
    prerequisite_map = [
    (1, 2),
    (2, 4),
    (3, 5),
    (0, 5),
    ]
    return semesters_required(number_of_courses, prerequisite_map) # -> 3

def test_01():
    number_of_courses = 7
    prerequisite_map = [
    (4, 3),
    (3, 2),
    (2, 1),
    (1, 0),
    (5, 2),
    (5, 6),
    ]
    return semesters_required(number_of_courses, prerequisite_map) # -> 5

def test_02():
    number_of_courses = 5
    prerequisite_map = [
    (1, 0),
    (3, 4),
    (1, 2),
    (3, 2),
    ]
    return semesters_required(number_of_courses, prerequisite_map) # -> 2

def test_03():
    number_of_courses = 12
    prerequisite_map = []
    return semesters_required(number_of_courses, prerequisite_map) # -> 1


def test_04():
    number_of_courses = 3
    prerequisite_map = [
    (0, 2),
    (0, 1),
    (1, 2),
    ]
    return semesters_required(number_of_courses, prerequisite_map) # -> 3

def test_05():
    number_of_courses = 6
    prerequisite_map = [
    (3, 4),
    (3, 0),
    (3, 1),
    (3, 2),
    (3, 5),
    ]
    return semesters_required(number_of_courses, prerequisite_map) # -> 2

### EXECUTE TESTS
print(test_runner(test_00, 3))
print(test_runner(test_01, 5))
print(test_runner(test_02, 2))
print(test_runner(test_03, 1))
print(test_runner(test_04, 3))
print(test_runner(test_05, 2))