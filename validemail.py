class ValidEmail:
    def validmail(self, emails):

        validSet = set()
        for mail in emails:
            l = 0
            first = ""
            while mail[l] not in ['+', '.']:
                first += mail[l]
                l += 1

            while mail[l] != "@":
                l += 1
            last = mail[l + 1:]
            validSet.add(first + "@" + last)
        return validSet


emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
obj = ValidEmail()
print(obj.validmail(emails))
