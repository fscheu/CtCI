"""You are given a list of projects and a list of dependencies (which is a list of pairs of 
projects, where the second project is dependent on the first project). All of a project's dependencies 
must be built before the project is. Find a build order that will allow the projects to be built. If there is no valid build order, return an error. 
EXAMPLE 
Input: 
projects: a, b, c, d, e, f 
dependencies: (a, d), (f, b), (b, d), (f, a), (d, c) 
Output: f, e, a, b, d, c """

def build_order(projects, dependencies):

    unbuild_proj = projects[:]
    unb_deps = { x:[] for x in projects }
    for (dep, proj) in dependencies:
        unb_deps[proj].append(dep)
    
    # builded = []
    # while unbuild_proj:
    #     build_something = False
    #     for proj in unbuild_proj:

def test_build_order():
    projects = ["a", "b", "c", "d", "e", "f" ]
    deps = [("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c") ]
    build_order(projects,deps)

if __name__ == "__main__":
    test_build_order()