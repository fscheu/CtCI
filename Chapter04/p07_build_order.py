"""You are given a list of projects and a list of dependencies (which is a list of pairs of
projects, where the second project is dependent on the first project). All of a project's dependencies
must be built before the project is. Find a build order that will allow the projects to be built. If there is no valid build order, return an error.
EXAMPLE
Input:
projects: a, b, c, d, e, f
dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
Output: f, e, a, b, d, c """

def build_order(projects, dependencies):

    unbuild_proj = set(projects)
    dependencies_sets = { x:set() for x in projects }
    for (dep, proj) in dependencies:
        dependencies_sets[proj].add(dep)

    builded = []
    while unbuild_proj:
        build_something = False
        for proj in list(unbuild_proj):
            if not dependencies_sets[proj].intersection(unbuild_proj):
                builded.append(proj)
                build_something = True
                unbuild_proj.remove(proj)
        if not build_something:
            return []
    return builded


def test_build_order():
    projects = ["a", "b", "c", "d", "e", "f" ]
    deps = [("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c") ]
    builded = build_order(projects,deps)
    for dependency, project in deps:
        assert builded.index(dependency) < builded.index(project)

if __name__ == "__main__":
    test_build_order()