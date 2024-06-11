from python.bankaccount.branch import Branch

class BranchFinder:
    def __init__(self):
        self.branch = Branch()

    def find_branch_for_town(self, town: str) -> Branch:
        # in a real system it would look in a database for this information
        return self.branch
