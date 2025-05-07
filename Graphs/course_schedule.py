'''
207. Course Schedule

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an 
array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want 
to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

Return true if you can finish all courses. Otherwise, return false.
'''

# Key Ideas:
# This is a standard topological sort problem. We need to check if a topological ordering exists.
# Run DFS on each course, from 0 to numCourses - 1. Once we reach a course which has no prerequisites
# or only prerequisites that can be completed, add the course to a completed set. To detect cycles, 
# we keep a visit set for each DFS run, and if we encounter an edge to a course that is already in the
# visit set, we return False.

# Runtime: O(numCourses + len(prerequisites)). We visit each edge (course-preq pair) at most once through DFS, which
# is O(len(prerequisites)). In the case of a sparse graph, we still visit every vertex (course), which is O(numCourses).


from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        preqDict = defaultdict(list)
        for course, preq in prerequisites:
            preqDict[course].append(preq)

        completed = set()

        def dfs(course, visit):
            if course in completed:
                return

            visit.add(course)
            for preq in preqDict[course]:
                if preq in visit:
                    return False
                if preq not in completed:
                    if not dfs(preq, visit):
                        return False

            completed.add(course)
            visit.remove(course)
            return True
        
        for course in range(numCourses):
            if course not in completed:
                if not dfs(course, set()):
                    return False

        return True