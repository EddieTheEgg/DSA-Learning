class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:

        # Len accounts is max amount of accounts assuming no merge possible
        parentEmails = list(range(len(accounts))) # 0 1 2 3 4...
        # How many accounts share this root email in parentEmails
        rank = [1] * len(accounts)

        #Key email, Value is the index of the account where we first saw email
        #Value cannot be account name since two same names != same account as problem stated, so we must only use index
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

            if rank[root1] > rank[root2]:
                parentEmails[root2] = root1
                rank[root1] += rank[root2]
            else:
                parentEmails[root1] = root2
                rank[root2] += rank[root1]


        # Go through each email of each account and try to union when possible
        # or add to list of emailToAccount to map new emails found to their account index
        for currAccountIndex, account in enumerate(accounts):
            #Exclude account[0] since that's the name
            for email in account[1:]:
                if email in emailToAccount:
                    #The email already exists in another account, try to union
                    union(currAccountIndex, emailToAccount[email])
                else:
                    emailToAccount[email] = currAccountIndex


        emailGroup = defaultdict(list)

        for email, accountIdx in emailToAccount.items():
            root = find(accountIdx)
            emailGroup[root].append(email)
        
        result = []
        for root_idx, emails in emailGroup.items():
            name = accounts[root_idx][0]
            result.append([name] + sorted(emails))
        
        return result

        







            



        