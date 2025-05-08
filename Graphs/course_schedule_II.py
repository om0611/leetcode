'''
210. Course Schedule II

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must 
take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid 
answers, return any of them. If it is impossible to finish all courses, return an empty array.
'''

# Key Ideas:
# This is a topological sort problem. 
# Run DFS on each course, from 0 to numCourses - 1. Once we reach a course which has no prerequisites
# or only prerequisites that are already completed, add the course to the ordering. To detect cycles, 
# we store the vertices we have seen along the current path, and if we encounter a course that we
# have already seen on this path, we return False.

# Runtime: O(numCourses + len(prerequisites)). We visit each edge (course-preq pair) through DFS, which
# is O(len(prerequisites)). We also visit each vertex (course) through the for loop, which is O(numCourses).
# Therefore, the runtime is O(numCourses + len(prerequisites)).


from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        preqDict = defaultdict(list)
        for course, preq in prerequisites:
            preqDict[course].append(preq)

        completed = set()
        ordering = []

        def dfs(course, visit):
            if course in completed:
                return True
            if course in visit:
                return False
            visit.add(course)
            for preq in preqDict[course]:
                if preq not in completed:
                    if not dfs(preq, visit):
                        return False
            completed.add(course)
            ordering.append(course)
            visit.remove(course)
            return True
            

        for course in range(numCourses):
            if course not in completed:
                if not dfs(course, set()):
                    return []
        
        return ordering