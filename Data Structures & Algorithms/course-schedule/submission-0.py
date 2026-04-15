class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # If there is a cycle, course cannot be finished
        #Approach is go through each course, check it's prereq, make sure these prereq don't cycle

        # Map each course to its prereq, so it's easier to read from
        # ex.) Course 0: [1, 2, 3] has three prereqs
        preMap = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            preMap[course].append(pre)


        # DFS course set
        visit = set()

        def isCourseNotCycleDFS(course):
            if course in visit:
                #cycle detected, base case
                return False
            if preMap[course] == []:
                #A course can have no prereq, base case
                return True
            
            visit.add(course)
            for pre in preMap[course]:
                # If a cycle is detected, break out of prereq checks asap
                if not isCourseNotCycleDFS(pre): return False

            visit.remove(course)
            preMap[course] = [] #smart way to tell dfs the course is valid by marking it with empty prereq

            return True


        for course in range(numCourses):
            if not isCourseNotCycleDFS(course): return False
        return True

    

        
