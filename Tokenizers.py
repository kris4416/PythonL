# Create a list of three strings.
incoming_reports = ["We are attacking on their left flank but are losing many men.",
               "We cannot see the enemy army. Nothing else to report.",
               "We are ready to attack but are waiting for your orders."]

# import word tokenizer
from nltk.tokenize import word_tokenize

tokenized_report = [word_tokenize(i) for i in incoming_reports]

print(tokenized_report)

#test changes
