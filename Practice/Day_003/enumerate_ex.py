langs_list = 'python java c# scalar'.split()
# Bad
for idx in range(len(langs_list)):
    print(f'idx = {idx}, value = {langs_list[idx]}')

# Good -enumerate() function
for idx, lang in enumerate(langs_list):
    print(f'idx = {idx}, value = {lang}')


# This is pretty awesome i think
my_dict = {i : j for i, j in enumerate(
                "Yesterday, all my troubles seemed so far away".split())}
print(my_dict)
