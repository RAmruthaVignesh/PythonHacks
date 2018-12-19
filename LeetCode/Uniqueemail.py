class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        total_mails = []
        for email in emails:
            email = email.split('@')
            domain = email[1]
            email = email[0]
            email_without_plus = email.split('+')
            email = email_without_plus[0]
            email = ''.join(email.split('.'))
            email = email+'@'+domain
            total_mails.append(email)
        total_mails = set(total_mails)
        num_total_mails = len(total_mails)
        return num_total_mails

mysol =Solution()
input= ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
unique_addresses = mysol.numUniqueEmails(input)
print(unique_addresses)