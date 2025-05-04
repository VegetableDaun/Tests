import re
from pprint import pprint
text = '''
    Software testing is the act of checking whether software satisfies expectations.
Software testing can provide objective, independent information about the quality of software and the risk of its failure to a user or sponsor.
Software testing can determine the correctness of software for specific scenarios but cannot determine correctness for all scenarios.It cannot find all bugs.
Based on the criteria for measuring correctness from an oracle, software testing employs principles and mechanisms that might recognize a problem. Examples of oracles include specifications, contracts, comparable products, past versions of the same product, inferences about intended or expected purpose, user or customer expectations, relevant standards, and applicable laws.
Software testing is often dynamic in nature; running the software to verify actual output matches expected. It can also be static in nature; reviewing code and its associated documentation.
Software testing is often used to answer the question: Does the software do what it is supposed to do and what it needs to do?
Information learned from software testing may be used to improve the process by which software is developed.
Software testing should follow a "pyramid" approach wherein most of your tests should be unit tests, followed by integration tests and finally end-to-end (e2e) tests should have the lowest proportion.
Software consists of computer programs that instruct the execution of a computer. Software also includes design documents and specifications. The history
'''

text = text.lower()
text = re.sub(r'[,!?".;:_()-]', '', text)

words_list = text.split()
words_dict = {}

for word in words_list:
    words_dict[word] = words_dict.get(word, 0) + 1

sorted_dict = dict(
    sorted(words_dict.items(), key=lambda x: x[0])
)

pprint(sorted_dict)
print(len(sorted_dict))