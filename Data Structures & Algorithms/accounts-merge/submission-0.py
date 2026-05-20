class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        #Use union find to group by same root email
        #We'll union account A and account B
        #If the account name share the same email, then they are unionized already

        #First step, is to have a parent array and a rank array

        # Len accounts is max amount of accounts assuming no merge possible
        parentEmails = list(range(len(accounts)))
        rank = [1] * len(accounts)

        #Key email, Value is the index of the account we first saw email
        emailToAccount = {}
        # johndoe@gmail.com : 1
        # abigal@gmail.com : 2

        def find(x):
            if parentEmails[x] != x:
                parentEmails[x] = find(parentEmails[x])
            return parentEmails[x]
        
        def union(idx1, idx2):
            root1, root2 = find(idx1), find(idx2)
            if root1 == root2:
                return
            parentEmails[root1] = root2


        for i, account in enumerate(accounts):
            #Exclude account[0] since that's the name
            for email in account[1:]:
                if email in emailToAccount:
                    union(i, emailToAccount[email])
                else:
                    emailToAccount[email] = i


        emailGroup = defaultdict(list)

        for email, accountIdx in emailToAccount.items():
            root = find(accountIdx)
            emailGroup[root].append(email)
        
        result = []
        for root_idx, emails in emailGroup.items():
            name = accounts[root_idx][0]
            result.append([name] + sorted(emails))
        
        return result

        







            



        