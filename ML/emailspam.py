
total_emails = int(input("Total emails: "))
emails_with_free = int(input("Emails containing 'free': "))
spam_emails = int(input("Spam emails: "))
spam_and_free = int(input("Spam emails containing 'free': "))


P_spam = spam_emails / total_emails
P_free = emails_with_free / total_emails
P_free_given_spam = spam_and_free / spam_emails

P_spam_given_free = (P_free_given_spam * P_spam) / P_free
print(f"P(Spam | Email contains 'free') = {P_spam_given_free:.4f}")
