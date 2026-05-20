class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        

            # We want to merge accounts via sharing the same root email
            # If same root email, that email should point to same account
            
            # so for example
            # johndoe@gmail.com : Jake
            # johndoe@gmail.com, lester@gmail.com : Bob

            # Should merge together since the two accounts share same email
            # but we cannot rely on the names, same names != same email!

            #Step 1: Same emails should point/group to same account. This means we should be going
            # through each email of each account no matter what at least once.

            # Lets treat each email point to an account index, we want emails share same account if their root is same account index

            emailToAccountIndex = {} # email : accountIndex

            # Each value of parentAccounts is the root account index of that index from accounts
            # So root of parentAccounts[0] = 3 would mean accounts[0] and accounts[3] are grouped/unioned
            parentAccounts = list(range(len(accounts)))
            rank = [1] * len(accounts) # Initial 1 since each account index root is themselves so their group size is 1

            def find(index):
                if parentAccounts[index] != index:
                    parentAccounts[index] = find(parentAccounts[index])
                return parentAccounts[index]

            def union(currAccountIndex, existingAccountIndex):
                root1 = find(currAccountIndex)
                root2 = find(existingAccountIndex)

                if root1 == root2:
                    return

                if rank[root1] > rank[root2]:
                    parentAccounts[root2] = root1
                    rank[root1] += rank[root2]
                else:
                    parentAccounts[root1] = root2
                    rank[root2] += rank[root1]
            
            for i, account in enumerate(accounts):
                #Exclude the first name, we only care about emails
                for email in account[1:]:
                    #This email was found in another account index, let's try to union!
                    if email in emailToAccountIndex:
                        # Union current account index where this email is from
                        # and the account index where that same email already exists in too from a previous iteration
                        # if they unionize, we don't need to explicilty update emailToAccountIndex[email] = i, since
                        # their accountIndex will share the same root in parentAccounts
                        union(i, emailToAccountIndex[email])
                    else:
                        #Never seen the email before, let's add it and index of the account it's from!
                        emailToAccountIndex[email] = i

            #Step 2: We finished going through every email of every account, and ready to start building our result!

            #First, we need to map a key of account index, and their emails (do not use name)

            groupedEmails = defaultdict(set) # Makes { 0:set() }

            for i, account in enumerate(accounts):
                rootAccountIndex = find(i)
                for email in account[1:]:
                    groupedEmails[rootAccountIndex].add(email)

            #Ok we now have groupedEmails, which if we did any merging should
            # be a length shorter than the initial list of accounts since we would have
            # combined emails under one account
            # Now we have two issues: we need the name of those account indexs, and the emails in those account indexs need to be sorted

            #Just easy formatting change

            result = []
            for accountIndex, emails in groupedEmails.items():
                accountName = accounts[accountIndex][0]
                result.append([accountName] + sorted(list(emails)))

            return result