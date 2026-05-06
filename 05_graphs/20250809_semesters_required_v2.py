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

    if number_of_courses == 0: 
        return 0
    
    if not prerequisite_map: 
        return 1
    
    # Initialise all courses
    ## Create the graph as a dictionary with a key for each course 0 to n-1 and value as an empty set.
    graph = {course: set() for course in range(number_of_courses)}
    
    ## For each prerequisite pair, add the dependent course to the prerequisite's set
    ## This creates edges: prerequisite → course (can take course after prerequisite)    
    for prerequisite, course in prerequisite_map:
        graph[prerequisite].add(course)

    memo = {} # a dictionary where key = node and value = semesters required to complete
    
    # Pre-compute terminal nodes
    ## We can compute the length of branches with no children nodes without invoking dfs()
    for course in range(number_of_courses):
        if len(graph[course]) == 0:
            memo[course] = 1

    # DEPTH FIRST SEARCH
    def dfs(course):
        if course in memo:
            return memo[course] # return the semesters required to complete if known
        
    # RECURSIVE CASE: We need to figure out this course's depth
    # This line is doing A LOT - let's break it down:
    # 1. graph[course] gives us all courses that depend on this one
    # 2. We recursively call dfs() on each descendant
    # 3. max() finds the longest path among all descendants
    # Note: If graph[course] is empty, max() would fail, but we pre-computed
    # those cases, so this is safe!

        max_descendant_depth = max(dfs(descendant) for descendant in graph[course])
        memo[course] = 1 + max_descendant_depth
        return memo[course]
    
    return max(dfs(course) for course in range(number_of_courses))

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