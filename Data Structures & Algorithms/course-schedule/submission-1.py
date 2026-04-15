class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # If there is a cycle, course cannot be finished
        #Approach is go through each course, and if any prereq ever gets visited again for that course, there's a cycle

        # Map each course to its prereq, so it's easier to read from
        # ex.) Course 0: [1, 2, 3] has three prereqs, this is an adj list
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
                # If a cycle is detected among the prereqs of current course, break out of prereq checks asap
                if not isCourseNotCycleDFS(pre): return False

            visit.remove(course)
       

            return True


        for course in range(numCourses):
            if not isCourseNotCycleDFS(course): return False
        return True

######
    #def dfs(node, visited):
    # BASE CASE: Already visited or null
    #if not node or node in visited:
        #return
    
    # MARK AS VISITED (prevent revisiting)
    #visited.add(node)  # or visited[node] = something
    
    # PROCESS CURRENT NODE
    # ... do whatever you need with this node ...
    
    # RECURSIVE CASE: Visit neighbors
    #for neighbor in node.neighbors:
        #dfs(neighbor, visited)
    
    # Optional: BACKTRACK or post-processing

        
